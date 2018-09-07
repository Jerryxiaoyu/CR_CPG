import time
from threading import Thread
import gym
import numpy as np
from gym.wrappers.monitoring.video_recorder import VideoRecorder

def Angle_PID(cur_angles, target_angles, target_velocities=0.1):
    target_angles = target_angles.reshape((-1, 1))
    
    q = cur_angles.reshape((-1, 1))
    
    kp = 5
    
    Kp = np.diag(np.ones(q.shape[0]) * kp)
    
    action = Kp.dot(target_angles - q)
    
    action = np.clip(action, -1, 1)
    action = np.array(action)

    return action.reshape((1, -1))[0]

class RecordMonitor(Thread):
    def __init__(self, env, monitor_path):
        Thread.__init__(self)
        # The starting time
 
        self.rec = VideoRecorder(env, path=monitor_path )
        
    def reset_timer(self):
        self.start_time = time.time()
        
    def get_rec(self):
        self.rec.capture_frame()  # 放在底层会使得控制不准!

    def stop(self):
        self.rec.close()
    
        

class RobotMonitorThread(Thread):
    """
    Class for monitoring objects in VREP simulator.
    This class extends the Thread class and will run as in parallel to the main simulation.
    Only one monitoring thread is enough for monitoring a simulation.
    """
    
    def __init__(self, env , render =False, monitor_path=None, memory =None, running_state=None):
        """
        Initializes the RobotMonitorThread thread

        :param portnum: Port number on which the VREP remote API is listening on the server
        (different than the one used to run the main robot simulation)
        :param objname: Object name which is to be monitored
        :height_threshold: If the object's height is lower than this value, the robot is considered to have falen
        """

        # cellrobot13  6,19
        # snake9 6, 15
        # butterfly7, 6,13
        # ant   7,15
        
        if env.env.spec.id == 'CellrobotEnv-v0' or env.env.spec.id == 'Cellrobot2Env-v0'or env.env.spec.id == 'CellrobotEnv_r-v0' :
            self.obs_low = 6
            self.obs_high = self.obs_low + 13

            self.height_threshold = 0.1
        elif env.env.spec.id == 'CellrobotSnakeEnv-v0' or env.env.spec.id == 'CellrobotSnake2Env-v0' :
            self.obs_low = 6
            self.obs_high = self.obs_low + 9

            self.height_threshold = 0.0
            
        elif env.env.spec.id == 'CellrobotButterflyEnv-v0':
            self.obs_low = 6
            self.obs_high = self.obs_low + 7

            self.height_threshold = 0.00
        elif env.env.spec.id == 'CellrobotBigdog2Env-v0':
            self.obs_low = 6
            self.obs_high = self.obs_low + 17
    
            self.height_threshold = 0.10
        elif env.env.spec.id == 'CellrobotBigSnakeEnv-v0':
            self.obs_low = 6
            self.obs_high = self.obs_low + 16
    
            self.height_threshold = 0.0
        else:
            assert 'ENV error!'
 
        
        # Call init of super class
        Thread.__init__(self)
        
        # Create a VrepIO object using a different port number than the one used to run the main robot simulation
        # Make sure that the VREP remote api on the server is listening on this port number
        # Additional ports for listening can be set up on the server side by editing the file remoteApiConnections.txt
        self.env = env
        
       # self.env =   gym.wrappers.Monitor(env, monitor_path, force=True)
        
        # The object to be monitored
        action_dim = env.action_space.shape[0]
        self.obs = self.env.reset()
        
        self.target_joint_angles = self.get_cur_angles()
        self.cur_angles = self.get_cur_angles()
        self.target_joint_velocities = None
        
        self.ctrl_init = np.zeros(action_dim)
        self.ctrl = self.ctrl_init
        
        # The starting time
        self.start_time = time.time()
        self.up_time = 0.0
        
        # A flag which can stop the thread
        self.stop_flag = False
        
        # A flag to indicate if the robot has fallen
        self.fallen = False
        
        # Set up the ROS listener
        # rospy.init_node('nico_feet_force_listener', anonymous=True)
        # rospy.Subscriber("/nico_feet_forces", String, force_sensor_callback)
        self.action = None
        
        self.x = self.obs[0]
        self.y = self.obs[1]
        self.z = self.obs[2]
        
        # The average height of the robot
        self.avg_z = 0.0

        # A list to store the height at each second
        self.z_list = list()
        
        
        self.render = render
        
        self.monitor_path =  monitor_path
        if self.monitor_path is not None:
           #self.rec = VideoRecorder(env, path=monitor_path )
           self.monitor_thread = RecordMonitor(env, monitor_path)
        self.t =0
        
        
        # store memory
        if memory is not None:
            self.obs1, self.obs2, self.rewards, self.dones, self.actions = [], [], [], [], []
            self.reward_episode=0
            self.memory = memory
        self.running_state = running_state
        
        
    def reset_timer(self):
        self.start_time = time.time()
    
    def run(self):
        """
        The monitoring logic is implemented here. The self.objpos is updated at a preset frequency with the latest
        object positions.

        :return: None
        """
        
        while not self.stop_flag:
            
            
            # Update the time
            self.up_time = time.time() - self.start_time
            
            # PD
            self.cur_angles = self.get_cur_angles()
            action = Angle_PID(self.cur_angles, self.target_joint_angles )
            
            #action = self.env.action_space.sample()
            action += np.random.normal(0, 0.005, size =action.shape)
            # execute action
            self.next_state, self.reward, self.done, _ = self.env.step(action)
            
            # Sleep
            # time.sleep(0.01)  # if ignored, may cause unstalbe
            
            # update param.
            self.x = self.next_state[0]
            self.y = self.next_state[1]
            self.z = self.next_state[2]
            
            
            self.avg_z = self.next_state[2]

            # Append the current height to the height list
            self.z_list.append(self.z)

            if self.z < self.height_threshold:
                # Set the flag which indicates that the robot has fallen
                self.fallen = True
                # Calculate the average height
                self.avg_z = sum(self.z_list) / float(len(self.z_list))
            # render
            if self.render:
                self.env.render()

            if self.t == 10:
                
                    
                if self.monitor_path is not None:
                    #self.rec.capture_frame()   # 放在底层会使得控制不准!
                    self.monitor_thread.get_rec()
                self.t =0
            else:
                self.t += 1

            #time.sleep(0.01)
            # if self.memory is not None:
            #     self.obs2.append(next_state.reshape((1, -1)))  # for storage
            #     self.obs1.append(next_state.reshape((1, -1)))  # for storage
            #     self.actions.append(action.reshape((1, -1)))
            #     self.reward_episode += reward
            #     if self.running_state is not None:
            #         next_state = running_state(next_state, update=update_rs)
            #
            #     if custom_reward is not None:
            #         reward = custom_reward(state, action)
            #         total_c_reward += reward
            #         min_c_reward = min(min_c_reward, reward)
            #         max_c_reward = max(max_c_reward, reward)
            #
            #     rewards.append(reward)  # for storage
            #     dones.append(done)  # for storage
            #     mask = 0 if done else 1
            #
            #     self.memory.push(self.obs, action, mask, next_state, reward)
            
            self.obs = self.next_state
    
    def stop(self):
        """
        Sets the flag which will stop the thread
        :return: None
        """
        # Flag to stop the monitoring thread
        self.stop_flag = True
        
        # Close the monitoring vrep connection
        self.env.close()
        if self.monitor_path is not None:
            #self.rec.close()
            self.monitor_thread.stop()
    
    def get_cur_angles(self):
        
        
        return self.obs[self.obs_low:self.obs_high]