import gym
import numpy as np
import matplotlib.pyplot as plt
import os

from my_gym_envs.mujoco import *

env = gym.make('CellrobotEnv-v0')



obs = env.reset()

for _ in range(1000):
    
    action = env.action_space.sample()
    #action = controller_PID_tracking(obs, qt[i], qdt[i])
    # for j in range(12):
    #     action[j] = 0
    
    

    # print(obs[12])
    next_obs, reward, done, _ = env.step(action)

    
    obs = next_obs
    
    env.render()