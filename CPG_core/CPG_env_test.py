import gym
import numpy as np
import matplotlib.pyplot as plt
import os

from my_envs.mujoco import *
import math
from CPG_core.CPG_controller import CPG_network

# CellrobotArmEnv-v0
#
# UR5Env-v0HalfCheetah2-v2
env = gym.make('CellrobotEnv-v0')

action_dim = env.action_space.shape[0]
state_dim = env.observation_space.shape[0]
T = 2000
q_dim = 13
itr_N = 10000


qdot_d = np.ones((q_dim, 1)) * 0
# q_d[q_dim-1][0] = 45.0*3.1415/180.0



monitor_path = None #'tmp/test.mp4'

print('state_dim = ', state_dim)
print('action_dim = ', action_dim)




def Angle_PID(cur_angles, target_angles, target_velocities=0.1):
    target_angles = target_angles.reshape((-1, 1))
    
    q = cur_angles.reshape((-1, 1))
    
    kp = 5
    
    Kp = np.diag(np.ones(q.shape[0]) * kp)
    
    action = Kp.dot(target_angles - q)
    
    action = np.clip(action, -1, 1)
    action = np.array(action)
    
    return action.reshape((1, -1))[0]

obs_low = 6
obs_high = 19
def get_cur_angles():
    return obs[obs_low:obs_high]
    

obs = env.reset()

from gym.wrappers.monitoring.video_recorder import VideoRecorder

if monitor_path is not None:
    rec = VideoRecorder(env, path=monitor_path)


# for store
actions = []
states = []

position_vector = np.zeros(27)
position_vector[0]=1
for i in range(1,14):
    position_vector[i] = 1
CPG_controller  = CPG_network(position_vector)


for itr in range(itr_N):
 
        # action = env.action_space.sample()
        # action = controller_PID(obs)

        output_list = CPG_controller.output(state=None)
        target_joint_angles = np.array(output_list[1:])
        cur_angles =  get_cur_angles()
        
        action = Angle_PID(cur_angles,  target_joint_angles)
        
        
        
        
        actions.append(action)
        states.append(obs)

        # print(obs[12])
        next_obs, reward, done, _ = env.step(action)
        
        # q.append(np.concatenate([env.env.data.qpos.flat]))
        # q_dot.append(np.concatenate([env.env.data.qvel.flat]))
        # act_force.append(np.concatenate([env.env.data.actuator_force.flat]))
        # torque.append(np.concatenate([env.env.data.sensordata.flat]))
        # act_length.append(np.concatenate([env.env.data.actuator_length.flat]))
        # act_velocity.append(np.concatenate([env.env.data.actuator_velocity.flat]))
        # q_acc.append(np.concatenate([env.env.data.qacc.flat]))
        
        obs = next_obs
        
        env.render()
        
        if monitor_path is not None:
            rec.capture_frame()

if monitor_path is not None:
    rec.close()
 