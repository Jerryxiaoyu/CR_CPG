# Script with no feedback
# This script is used for evaluating the gait
# 将权值函数修改为优化参数, 相邻驱动 与构型文件相同

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

import os
import gym
from CPG_core.CPG_osillator import matsuoka_oscillator
from fitness import calc_fitness
from gait_eval_result import GaitEvalResult



def oscillator_nw(position_vector, max_time=10.0, fitness_option=6, plot = False, log_dis = False, render = False, monitor_path=None, save_plot_path = None, env_name =None):
    
    if log_dis:
        log.infov('[OSC]-------------------------------------------------------------')
        log.infov('[OSC] Run in multiprocessing({})'.format(os.getpid()))
        
        log.infov('[OSC] Running oscillator_2.oscillator_nw')
        log.info('[OSC] Printing chromosome')
        log.info('[OSC] {0}'.format(position_vector))
        log.info('[OSC] Started monitoring thread')
        
    # Start the monitoring thread
    if env_name is None:
        env = gym.make('CellrobotEnv-v0')
    else:
        env = gym.make(env_name)
        # print(env.env.spec.id)
    CPG_node_num = 13
    

    # Extract the elements from the position vector
    kf = position_vector[0]
    GAIN0 = position_vector[1]
    GAIN1 = position_vector[2]
    GAIN2 = position_vector[3]
    GAIN3 = position_vector[4]
    GAIN4 = position_vector[5]
    GAIN5 = position_vector[6]
    GAIN6 = position_vector[7]
    GAIN7 = position_vector[8]
    GAIN8 = position_vector[9]
    GAIN9 = position_vector[10]
    GAIN10 = position_vector[11]
    GAIN11 = position_vector[12]
    GAIN12 = position_vector[13]

    BIAS0 = position_vector[14]
    BIAS1 = position_vector[15]
    BIAS2 = position_vector[16]
    BIAS3 = position_vector[17]
    BIAS4 = position_vector[18]
    BIAS5 = position_vector[19]
    BIAS6 = position_vector[20]
    BIAS7 = position_vector[21]
    BIAS8 = position_vector[22]
    BIAS9 = position_vector[23]
    BIAS10 = position_vector[24]
    BIAS11 = position_vector[25]
    BIAS12 = position_vector[26]
    
    W1 = position_vector[27]
    W2 = position_vector[28]
    W3 = position_vector[29]
    W4 = position_vector[30]
    W5 = position_vector[31]
    W6 = position_vector[32]
    W7 = position_vector[33]
    W8 = position_vector[34]
    W9 = position_vector[35]
    W10 = position_vector[36]
    W11 = position_vector[37]
    W12 = position_vector[38]
    W13 = position_vector[39]
   
    
    

    osillator = matsuoka_oscillator(kf)
    osillator_fun = osillator.oscillator_fun

    # Variables
    # Oscillator 1 (pacemaker)
    u1_1, u2_1, v1_1, v2_1, y1_1, y2_1, o_1, gain_1, bias_1 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0
    # Oscillator 2 --cell0
    u1_2, u2_2, v1_2, v2_2, y1_2, y2_2, o_2, gain_2, bias_2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN0, BIAS0
    # Oscillator 3 --cell1
    u1_3, u2_3, v1_3, v2_3, y1_3, y2_3, o_3, gain_3, bias_3 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN1, BIAS1
    # Oscillator 4 --cell2
    u1_4, u2_4, v1_4, v2_4, y1_4, y2_4, o_4, gain_4, bias_4 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN2, BIAS2
    # Oscillator 5 --cell3
    u1_5, u2_5, v1_5, v2_5, y1_5, y2_5, o_5, gain_5, bias_5 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN3, BIAS3
    # Oscillator 6 --cell4
    u1_6, u2_6, v1_6, v2_6, y1_6, y2_6, o_6, gain_6, bias_6 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN4, BIAS4
    # Oscillator 7 --cell5
    u1_7, u2_7, v1_7, v2_7, y1_7, y2_7, o_7, gain_7, bias_7 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN5, BIAS5
    # Oscillator 8 --cell6
    u1_8, u2_8, v1_8, v2_8, y1_8, y2_8, o_8, gain_8, bias_8 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN6, BIAS6
    # Oscillator 9 --cell7
    u1_9, u2_9, v1_9, v2_9, y1_9, y2_9, o_9, gain_9, bias_9 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN7, BIAS7
    # Oscillator 10 --cell8
    u1_10, u2_10, v1_10, v2_10, y1_10, y2_10, o_10, gain_10, bias_10 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN8, BIAS8
    # Oscillator 11 --cell9
    u1_11, u2_11, v1_11, v2_11, y1_11, y2_11, o_11, gain_11, bias_11 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN9, BIAS9
    # Oscillator 12 --cell10
    u1_12, u2_12, v1_12, v2_12, y1_12, y2_12, o_12, gain_12, bias_12 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN10, BIAS10
    # Oscillator 13 --cell11
    u1_13, u2_13, v1_13, v2_13, y1_13, y2_13, o_13, gain_13, bias_13 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN11, BIAS11
    # Oscillator 14 --cell12
    u1_14, u2_14, v1_14, v2_14, y1_14, y2_14, o_14, gain_14, bias_14 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN12, BIAS12

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
        o10_list = list()
        o11_list = list()
        o12_list = list()
        o13_list = list()
        t_list = list()

 
    # Set the joints to the initial bias positions - use slow angle setter
    initial_bias_angles = {'cell0':BIAS0, 'cell1':BIAS1,'cell2':BIAS2,'cell3':BIAS3,'cell4':BIAS4,
                        'cell5':BIAS5, 'cell6':BIAS6,'cell7':BIAS7,'cell8':BIAS8,'cell9':BIAS9,
                        'cell10':BIAS10, 'cell11':BIAS11,'cell12':BIAS12
                       }
    
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
    #robot_handle.set_angles_slow(target_angles=initial_bias_angles, duration=5.0, step=0.01)

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

        #-----------------------------------------------------------------------------------------------------
        # ---------------------------------------NETWORK START-----------------------------------------------
        # -----------------------------------------------------------------------------------------------------
        # Calculate next state of oscillator 1 (pacemaker)
        f1_1, f2_1 = 0.0, 0.0
        s1_1, s2_1 = 0.0, 0.0
        u1_1, u2_1, v1_1, v2_1, y1_1, y2_1, o_1 = osillator_fun(u1=u1_1, u2=u2_1, v1=v1_1, v2=v2_1, y1=y1_1, y2=y2_1,
                                                                f1=f1_1, f2=f2_1, s1=s1_1, s2=s2_1,
                                                                bias=bias_1, gain=gain_1, )

        # center
        # Calculate next state of oscillator 2  --cell0
        # w_ij -> j=1 (oscillator 1) is master, i=2 (oscillator 2) is slave
        w_21 = float(W1)
        f1_2, f2_2 = 0.0, 0.0
        s1_2, s2_2 = w_21 * u1_1, w_21 * u2_1
        u1_2, u2_2, v1_2, v2_2, y1_2, y2_2, o_2 = osillator_fun(u1=u1_2, u2=u2_2, v1=v1_2, v2=v2_2, y1=y1_2, y2=y2_2,
                                                                f1=f1_2, f2=f2_2, s1=s1_2, s2=s2_2,
                                                                bias=bias_2, gain=gain_2)

        # Left forward 1
        # Calculate next state of oscillator 3 --cell1
        # w_ij -> j=1 (oscillator 2) is master, i=3 (oscillator 3) is slave
        w_32 = float(W2)
        f1_3, f2_3 = 0.0, 0.0
        s1_3, s2_3 = w_32 * u1_1, w_32 * u2_1
        u1_3, u2_3, v1_3, v2_3, y1_3, y2_3, o_3 = osillator_fun(u1=u1_3, u2=u2_3, v1=v1_3, v2=v2_3, y1=y1_3, y2=y2_3,
                                                                f1=f1_3, f2=f2_3, s1=s1_3, s2=s2_3,
                                                                bias=bias_3, gain=gain_3)

        # Left back 1
        # Calculate next state of oscillator 4 --cell2
        # w_ij -> j=2 (oscillator 2) is master, i=4 (oscillator 4) is slave
        w_42 = float(W3)
        f1_4, f2_4 = 0.0, 0.0
        s1_4, s2_4 = w_42 * u1_2, w_42 * u2_2  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_4, u2_4, v1_4, v2_4, y1_4, y2_4, o_4 = osillator_fun(u1=u1_4, u2=u2_4, v1=v1_4, v2=v2_4, y1=y1_4, y2=y2_4,
                                                                f1=f1_4, f2=f2_4, s1=s1_4, s2=s2_4,
                                                                bias=bias_4, gain=gain_4)

        # Right forward 1
        # Calculate next state of oscillator 5 --cell3
        # w_ij -> j=3 (oscillator 3) is master, i=5 (oscillator 5) is slave
        w_52 = float(W4)
        f1_5, f2_5 = 0.0, 0.0
        s1_5, s2_5 = w_52 * u1_3, w_52 * u2_3  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_5, u2_5, v1_5, v2_5, y1_5, y2_5, o_5 = osillator_fun(u1=u1_5, u2=u2_5, v1=v1_5, v2=v2_5, y1=y1_5, y2=y2_5,
                                                                f1=f1_5, f2=f2_5, s1=s1_5, s2=s2_5,
                                                                bias=bias_5, gain=gain_5)

        # Right back1
        # Calculate next state of oscillator 6 --cell4
        # w_ij -> j=2 (oscillator 2) is master, i=6 (oscillator 6) is slave
        w_62 = float(W5)
        f1_6, f2_6 = 0.0, 0.0
        s1_6, s2_6 = w_62 * u1_2, w_62 * u2_2  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_6, u2_6, v1_6, v2_6, y1_6, y2_6, o_6 = osillator_fun(u1=u1_6, u2=u2_6, v1=v1_6, v2=v2_6, y1=y1_6, y2=y2_6,
                                                                f1=f1_6, f2=f2_6, s1=s1_6, s2=s2_6,
                                                                bias=bias_6, gain=gain_6)

        # Left forward 2
        # Calculate next state of oscillator 7 --cell5
        # w_ij -> j=3 (oscillator 3) is master, i=7 (oscillator 7) is slave
        w_73 = float(W6)
        f1_7, f2_7 = 0.0, 0.0
        s1_7, s2_7 = w_73 * u1_3, w_73 * u2_3  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_7, u2_7, v1_7, v2_7, y1_7, y2_7, o_7 = osillator_fun(u1=u1_7, u2=u2_7, v1=v1_7, v2=v2_7, y1=y1_7, y2=y2_7,
                                                                f1=f1_7, f2=f2_7, s1=s1_7, s2=s2_7,
                                                                bias=bias_7, gain=gain_7)

        # Left foward 3
        # Calculate next state of oscillator 8 --cell6
        # w_ij -> j=1 (oscillator 7) is master, i=8 (oscillator 8) is slave
        w_87 = float(W7)
        f1_8, f2_8 = 0.0, 0.0
        s1_8, s2_8 = w_87 * u1_1, w_87 * u2_1  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_8, u2_8, v1_8, v2_8, y1_8, y2_8, o_8 = osillator_fun(u1=u1_8, u2=u2_8, v1=v1_8, v2=v2_8, y1=y1_8, y2=y2_8,
                                                                f1=f1_8, f2=f2_8, s1=s1_8, s2=s2_8,
                                                                bias=bias_8, gain=gain_8)

        # Left back 2
        # Calculate next state of oscillator 9 --cell7
        # w_ij -> j=8 (oscillator 4) is master, i=9 (oscillator 9) is slave
        w_94 = float(W8)
        f1_9, f2_9 = 0.0, 0.0
        s1_9, s2_9 = w_94 * u1_8, w_94 * u2_8  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_9, u2_9, v1_9, v2_9, y1_9, y2_9, o_9 = osillator_fun(u1=u1_9, u2=u2_9, v1=v1_9, v2=v2_9, y1=y1_9, y2=y2_9,
                                                                f1=f1_9, f2=f2_9, s1=s1_9, s2=s2_9,
                                                                bias=bias_9, gain=gain_9)

        # Left back 3
        # Calculate next state of oscillator 10 --cell8
        # w_ij -> j=1 (oscillator 9) is master, i=10 (oscillator 10) is slave
        w_109 = float(W9)
        f1_10, f2_10 = 0.0, 0.0
        s1_10, s2_10 = w_109 * u1_1, w_109 * u2_1  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_10, u2_10, v1_10, v2_10, y1_10, y2_10, o_10 = osillator_fun(u1=u1_10, u2=u2_10, v1=v1_10, v2=v2_10, y1=y1_10,
                                                                       y2=y2_10,
                                                                       f1=f1_10, f2=f2_10, s1=s1_10, s2=s2_10,
                                                                       bias=bias_10, gain=gain_10)

        # Right forward 2
        # Calculate next state of oscillator 11 --cell9
        # w_ij -> j=10 (oscillator 5) is master, i=11 (oscillator 11) is slave
        w_115 = float(W10)
        f1_11, f2_11 = 0.0, 0.0
        s1_11, s2_11 = w_115 * u1_10, w_115 * u2_10  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_11, u2_11, v1_11, v2_11, y1_11, y2_11, o_11 = osillator_fun(u1=u1_11, u2=u2_11, v1=v1_11, v2=v2_11, y1=y1_11,
                                                                       y2=y2_11,
                                                                       f1=f1_11, f2=f2_11, s1=s1_11, s2=s2_11,
                                                                       bias=bias_11, gain=gain_11)

        # Right forward 3
        # Calculate next state of oscillator 12 --cell10
        # w_ij -> j=1 (oscillator 11) is master, i=12 (oscillator 12) is slave
        w_1211 = float(W11)
        f1_12, f2_12 = 0.0, 0.0
        s1_12, s2_12 = w_1211 * u1_1, w_1211 * u2_1  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_12, u2_12, v1_12, v2_12, y1_12, y2_12, o_12 = osillator_fun(u1=u1_12, u2=u2_12, v1=v1_12, v2=v2_12, y1=y1_12,
                                                                       y2=y2_12,
                                                                       f1=f1_12, f2=f2_12, s1=s1_12, s2=s2_12,
                                                                       bias=bias_12, gain=gain_12)

        # Right back 2
        # Calculate next state of oscillator 13 --cell11
        # w_ij -> j=1 (oscillator 6) is master, i=13 (oscillator 13) is slave
        w_136 = float(W12)
        f1_13, f2_13 = 0.0, 0.0
        s1_13, s2_13 = w_136 * u1_1, w_136 * u2_1  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_13, u2_13, v1_13, v2_13, y1_13, y2_13, o_13 = osillator_fun(u1=u1_13, u2=u2_13, v1=v1_13, v2=v2_13, y1=y1_13,
                                                                       y2=y2_13,
                                                                       f1=f1_13, f2=f2_13, s1=s1_13, s2=s2_13,
                                                                       bias=bias_13, gain=gain_13)

        # Right back 3
        # Calculate next state of oscillator 14 --cell11
        # w_ij -> j=1 (oscillator 6) is master, i=14 (oscillator 14) is slave
        w_1413 = float(W13)
        f1_14, f2_14 = 0.0, 0.0
        s1_14, s2_14 = w_1413 * u1_1, w_1413 * u2_1  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_14, u2_14, v1_14, v2_14, y1_14, y2_14, o_14 = osillator_fun(u1=u1_14, u2=u2_14, v1=v1_14, v2=v2_14, y1=y1_14,
                                                                       y2=y2_14,
                                                                       f1=f1_14, f2=f2_14, s1=s1_14, s2=s2_14,
                                                                       bias=bias_14, gain=gain_14)

        # -----------------------------------------------------------------------------------------------------
        # ---------------------------------------NETWORK END--------------------------------------------------
        # -----------------------------------------------------------------------------------------------------

        # Set the joint positions
        current_angles = {'cell0':o_2, 'cell1':o_3,'cell2':o_4,'cell3':o_5,'cell4':o_6,
                        'cell5':o_7, 'cell6':o_8,'cell7':o_9,'cell8':o_10,'cell9':o_11,
                        'cell10':o_12, 'cell11':o_13,'cell12':o_14
                       }
        robot_handle.set_angles(current_angles)

        time.sleep(dt)

        # Check if the robot has fallen
        if monitor_thread.fallen:
            break

        # For plots - not needed now
        if plot:
            o1_list.append(o_1)
            o2_list.append(o_2)
            o3_list.append(o_3)
            o4_list.append(o_4)
            o5_list.append(o_5)
            o6_list.append(o_6)
            o7_list.append(o_7)
            o8_list.append(o_8)
            o9_list.append(o_9)
            o10_list.append(o_10)
            o11_list.append(o_11)
            o12_list.append(o_12)
            o13_list.append(o_13)
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
    
        ax5 = plt.subplot(615, sharex=ax1, sharey=ax1)
        plt.plot(t_list, o1_list, color='red', label='o_1')
        plt.plot(t_list, o10_list, color='orange', ls='--', label='o_10')
        plt.plot(t_list, o11_list, color='orange', label='o_11')
        plt.grid()
        plt.legend()
    
        ax6 = plt.subplot(616, sharex=ax1, sharey=ax1)
        plt.plot(t_list, o1_list, color='red', label='o_1')
        plt.plot(t_list, o12_list, color='brown', ls='--', label='o_12')
        plt.plot(t_list, o13_list, color='brown', label='o_13')
        plt.grid()
        plt.legend()
        if save_plot_path is not None:
            plt.savefig(save_plot_path)
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
#
# position_vector = np.zeros(27)
# position_vector[0]=1
# for i in range(1,14):
#     position_vector[i] = 1
#
#
#
# oscillator_nw(position_vector,plot=True)