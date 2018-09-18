# Script with no feedback
# This script is used for evaluating the gait
# It is same as oscillator_2_1.py except that here a different monitor is used
# All differences are marked with the tag 'Different from original script'

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
import time
import math
from utils import log

# Different from original script
from robot_mujoco.monitor_thread import  RobotMonitorThread
from robot_mujoco.CRot import CRbot
from my_gym_envs.mujoco import *
#from my_envs.mujoco import *

import os
import gym
from CPG_core.CPG_osillator import matsuoka_oscillator
from fitness import calc_fitness
from gait_eval_result import GaitEvalResult

from math import pi, cos, sin
from CPG_core.controllers.CPG_controller_bigdog2_sin import CPG_network


def oscillator_nw(position_vector, max_time=10.0, fitness_option=6, plot = False, log_dis = False, render = False, monitor_path=None, save_plot_path = None, env_name=None
                  ):
    
    if log_dis:
        log.infov('[OSC]-------------------------------------------------------------')
        log.infov('[OSC] Run in multiprocessing({})'.format(os.getpid()))
        
        log.infov('[OSC] Running oscillator_2.oscillator_nw')
        log.info('[OSC] Printing chromosome')
        log.info('[OSC] {0}'.format(position_vector))
        log.info('[OSC] Started monitoring thread')
        
    # Start the monitoring thread
    # Start the monitoring thread
    if env_name is None:
        env = gym.make('CellrobotBigdog2Env-v0')
    else:
        env = gym.make(env_name)
    CPG_node_num =14 # 17-3

    # For plots - not needed now
    if plot:
        o1_list = list()
        o2_list = list()
        o3_list = list()
        o4_list = list()
        o5_list = list()
        o6_list = list()
        o7_list = list()
        o8_list = list()
        o9_list = list()
        end_pos_x_list = list()
        end_pos_y_list = list()
        end_pos_z_list = list()
        t_list = list()

 
    CPG_controller  = CPG_network(CPG_node_num, position_vector)
    
    # Set monitor thread
    monitor_thread = RobotMonitorThread(env, render, monitor_path=monitor_path)
    
    # Set robot API
    robot_handle = CRbot(env, monitor_thread, sync_sleep_time=0.01, interpolation=False, fraction_max_speed=0.01,
                         wait=False, )
    # Note the current position
    start_pos_x = monitor_thread.x
    start_pos_y = monitor_thread.y
    start_pos_z = monitor_thread.z
    
    # Start the monitoring thread
    monitor_thread.start()
    
    # Set init angles
   # robot_handle.set_angles_slow(target_angles=initial_bias_angles, duration=2.0, step=0.01)

    # Sleep for 2 seconds to let any oscillations to die down
    time.sleep(2.0)

    # Reset the timer of the monitor
    monitor_thread.reset_timer()

    # New variable for logging up time, since monitor thread is not accurate some times
    up_t = 0.0
    dt =0.01

    for t in np.arange(0.0, max_time, dt):

        # Increment the up time variable
        up_t = t

        output_list = CPG_controller.output(state=None)

        # Set the joint positions
        current_angles = {'cell0': 0, 'cell1': 0, 'cell2': 0,
                          'cell3': 0, 'cell4': output_list[2],
                          'cell5': output_list[3], 'cell6': output_list[4], 'cell7': output_list[5],
                          'cell8': 0, 'cell9': output_list[7],'cell10': output_list[8],
                          'cell11': output_list[9],'cell12': output_list[10],'cell13': output_list[11],
                          'cell14': output_list[12], 'cell15': output_list[13], 'cell16': output_list[14],
                          }
        robot_handle.set_angles(current_angles)

        time.sleep(dt)

        # Check if the robot has fallen
        if monitor_thread.fallen:
            break

        # For plots - not needed now
        if plot:
            o1_list.append(output_list[1])
            o2_list.append(output_list[2])
            o3_list.append(output_list[3])
            o4_list.append(output_list[4])
            o5_list.append(output_list[5])
            o6_list.append(output_list[6])
            o7_list.append(output_list[7])
            o8_list.append(output_list[8])
            o9_list.append(output_list[9])
            end_pos_x_list.append(monitor_thread.x)
            end_pos_y_list.append(monitor_thread.y)
            end_pos_z_list.append(monitor_thread.z)
            t_list.append(t)

    if log_dis:
        log.info('[OSC] Accurate up time: {0}'.format(up_t))

    # Outside the loop, it means that either the robot has fallen or the max_time has elapsed
    # Find out the end position of the robot
    end_pos_x = monitor_thread.x
    end_pos_y = monitor_thread.y
    end_pos_z = monitor_thread.z

    # Find the average height
    avg_z = monitor_thread.avg_z

    # Find the up time
    # up_time = monitor_thread.up_time
    up_time = up_t

    # Calculate the fitness
    if up_time == 0.0:
        fitness = 0.0
        if log_dis:
            log('[OSC] up_t==0 so fitness is set to 0.0')
    else:
        fitness = calc_fitness(start_x=start_pos_x, start_y=start_pos_y, start_z=start_pos_z,
                               end_x=end_pos_x, end_y=end_pos_y, end_z=end_pos_z,
                               avg_z=avg_z,
                               up_time=up_time,
                               fitness_option=fitness_option
                               )

    if log_dis:
        if not monitor_thread.fallen:
            log.info("[OSC] Robot has not fallen")
        else:
            log.info("[OSC] Robot has fallen")
    
        log.info('[OSC] Calculated fitness: {0}'.format(fitness))

    

    # Different from original script
    # Fetch the values of the evaluation metrics
    fallen = monitor_thread.fallen
    up = up_time # Using a more accurate up time than monitor_thread.up_time,
    x_distance = end_pos_x - start_pos_x
    abs_y_deviation = end_pos_y
    avg_footstep_x = None
    var_torso_alpha = monitor_thread.obs[3]
    var_torso_beta = monitor_thread.obs[4]
    var_torso_gamma = monitor_thread.obs[5]
    
    
    # Stop the monitoring thread
    monitor_thread.stop()
    # Close the VREP connection
    robot_handle.cleanup()

    # For plots - not needed now
    if plot:
        ax1 = plt.subplot(611)
        plt.plot(t_list, o1_list, color='red', label='o_1')
        plt.plot(t_list, o2_list, color='green', ls='--', label='o_2')
        plt.plot(t_list, o3_list, color='green', label='o_3')
        plt.grid()
        plt.legend()
    
        ax2 = plt.subplot(612, sharex=ax1, sharey=ax1)
        plt.plot(t_list, o1_list, color='red', label='o_1')
        plt.plot(t_list, o4_list, color='blue', ls='--', label='o_4')
        plt.plot(t_list, o5_list, color='blue', label='o_5')
        plt.grid()
        plt.legend()
    
        ax3 = plt.subplot(613, sharex=ax1, sharey=ax1)
        plt.plot(t_list, o1_list, color='red', label='o_1')
        plt.plot(t_list, o6_list, color='black', ls='--', label='o_6')
        plt.plot(t_list, o7_list, color='black', label='o_7')
        plt.grid()
        plt.legend()
    
        ax4 = plt.subplot(614, sharex=ax1, sharey=ax1)
        plt.plot(t_list, o1_list, color='red', label='o_1')
        plt.plot(t_list, o8_list, color='cyan', ls='--', label='o_8')
        plt.plot(t_list, o9_list, color='cyan', label='o_9')
        plt.grid()
        plt.legend()
    
       
        if save_plot_path is not None:
            plt.savefig(save_plot_path+'/fig1.jpg')
        else:
            plt.show()

        plt.Figure(figsize=(15, 10))

        ax1 = plt.subplot(311)
        plt.plot(t_list, end_pos_x_list, color='red', label='x')

        plt.grid()
        plt.legend()

        ax2 = plt.subplot(312, sharex=ax1, sharey=ax1)
        plt.plot(t_list, end_pos_y_list, color='red', label='y')
        plt.grid()
        plt.legend()

        ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
        plt.plot(t_list, end_pos_z_list, color='red', label='z')
        plt.grid()
        plt.legend()
        if save_plot_path is not None:
            plt.savefig(save_plot_path+'/fig1.jpg')
        else:
            plt.show()

    # Different from original script
    # Return the evaluation metrics
    return {'fitness': fitness,
            'fallen': fallen,
            'up': up,
            'x_distance': x_distance,
            'abs_y_deviation': abs_y_deviation,
            'avg_footstep_x': avg_footstep_x,
            'var_torso_alpha': var_torso_alpha,
            'var_torso_beta': var_torso_beta,
            'var_torso_gamma': var_torso_gamma}
    #return fitness


# position_vector = np.zeros(43)
# position_vector[0]=1
# for i in range(1,15):
#     position_vector[i] = 1
#
# print(position_vector)
#
# oscillator_nw(position_vector, plot=True,render=True, monitor_path=None, #'/home/drl/PycharmProjects/DeployedProjects/CR_CPG/tmp/tmp2.mp4'
#               save_plot_path=None) #'/home/drl/PycharmProjects/DeployedProjects/CR_CPG/tmp/tmp.mp4'