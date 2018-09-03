
from robot_mujoco.robots import Robot

import math

import time
import numpy as np
import gym

joint_name_motor_tab ={'cell0':0, 'cell1':1,'cell2':2,'cell3':3,'cell4':4,
                        'cell5':5, 'cell6':6,'cell7':7,'cell8':8,'cell9':9,
                        'cell10':10, 'cell11':11,'cell12':12
                       }

class CRbot(Robot):
    """
    This class encapsulates the methods and properties for interacting with the nao robot
    It extends the abstract class 'Robot'
    """

    sync_sleep_time = None
    robot_handle = None
    interpolation = None
    fraction_max_speed = None
    wait = None

    def __init__(self,env, monitor_thread, sync_sleep_time, interpolation=False, fraction_max_speed=0.01, wait=False,
                   ):

        """
        The constructor of the class. Class properties should be set here
        The robot handle should be created here
        Any other initializations such as setting angles to particular values should also be taken care of here

        :type sync_sleep_time: float
        :param sync_sleep_time: Time to sleep to allow the joints to reach their targets (in seconds)
        :type interpolation: bool
        :param interpolation: Flag to indicate if intermediate joint angles should be interpolated
        :type fraction_max_speed: float
        :param fraction_max_speed: Fraction of the maximum motor speed to use
        :type wait: bool
        :param wait: Flag to indicate whether the control should wait for each angle to reach its target
        :type motor_config: str
        :param motor_config: json configuration file
        :type vrep: bool
        :param vrep: Flag to indicate if VREP is to be used
        :type vrep_host: str
        :param vrep_host: IP address of VREP server
        :type vrep_port: int
        :param vrep_port: Port of VREP server
        :type vrep_scene: str
        :param vrep_scene: VREP scene to load
        """

        super(CRbot, self).__init__()

        # Set the properties
        self.sync_sleep_time = sync_sleep_time
        self.interpolation = interpolation
        self.fraction_max_speed = fraction_max_speed
        self.wait = wait
        
        
        self.env = env
        self.monitor_thread = monitor_thread

        # List of all joint names
        self.all_joint_names = joint_name_motor_tab.keys()
    
        

    def set_angles_slow(self, target_angles, duration, step=0.01):
        """
        Sets the angles over the specified duration using linear interpolation

        :param target_angles:
        :param duration:
        :param step:
        :return:
        """

        # Retrieve the start angles
        start_angles = self.get_angles(joint_names=target_angles.keys())

        # Calculate the slope for each joint
        angle_slopes = dict()
        for joint_name in target_angles.keys():
            start = start_angles[joint_name]
            end = target_angles[joint_name]
            angle_slopes[joint_name] = (end - start)/duration

        # t starts from 0.0 and goes till duration
        for t in np.arange(0.0, duration+0.01, step):
            current_angles = dict()
            # Calculate the value of each joint angle at time t
            for joint_name in target_angles.keys():
                current_angles[joint_name] = start_angles[joint_name] + angle_slopes[joint_name]*t

            # Set the current angles
            self.set_angles(current_angles)

            # Sleep for the step time
            time.sleep(step)

    def set_angles(self, joint_angles, duration=None, joint_velocities=None):
        """
        Sets the joints to the specified angles (in radians   )

        :type joint_angles: dict
        :param joint_angles: Dictionary of joint_names: angles (in radians)
        :type duration: float
        :param duration: Time to reach the angular targets (in seconds)
        :type joint_velocities: dict
        :param joint_velocities: dict of joint angles and velocities
        :return: None
        """
        angles = np.zeros(len(joint_angles))
        for joint_name in joint_angles.keys():
            
            angles[joint_name_motor_tab[joint_name]] = joint_angles[joint_name]
            
            
 
        self.monitor_thread.target_joint_angles = angles
        self.monitor_thread.target_joint_velocities = self.fraction_max_speed
 

        # Sleep to allow the motors to reach their targets
        if duration is not None:
            time.sleep(self.sync_sleep_time)

    def get_angles(self, joint_names=None):
        """
        Gets the angles of the specified joints and returns a dict of joint_names: angles (in radians)
        If joint_names=None then the values of all joints are returned

        :type joint_names: list(str)
        :param joint_names: List of joint names
        :rtype: dict
        """

        # Create the dict to be returned
        joint_angles = dict()

        # If joint names are not provided, get values of all joints
        if joint_names is None:
            # Call the nicomotion api function to get list of joint names
            joint_names = self.all_joint_names

        angles = self.monitor_thread.cur_angles
        
        for n_name in joint_names:
            joint_angles[n_name] = angles[joint_name_motor_tab[n_name]]
        
        
        

        return joint_angles

    def cleanup(self):
        """
        Cleans up the current connection to the robot
        :return: None
        """
        #self.robot_handle.cleanup()
        pass