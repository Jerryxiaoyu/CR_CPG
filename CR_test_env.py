import gym
import numpy as np

from my_gym_envs.mujoco import *



env = gym.make('Cellrobot2Env-v0')  # Swimmer2-v2  SpaceInvaders-v0  CellrobotSnakeEnv-v0  CellrobotTrackEnv-v0 CellrobotButterflyEnv-v0


# env = gym.make('FetchPickAndPlace-v1')



action = env.action_space.sample()
print('state: ', env.observation_space)
print('action: ', env.action_space)
q_dim = 1
obs = env.reset()
action = np.zeros(q_dim)

T = 10000

# while True:
#     env.render()


q_d = 45 * 3.14 / 180.0
qdot_d = 0
Kp = 1
Kv = 1
# action[-1] = 1
# action[-2] = 1
action[0] = 1
q = []
qacc = []
print(action)

act_force = []



for i in range(T):
    #action = env.action_space.sample()
    # action = disable_action(action,6)
    # print(action)
    # action = np.zeros(5)
    # # a = np.random.uniform(low=-1, high=1.0, size=1)
    # action[0] = 0.5
    # #action[-2] = -0.2
    # action[-3] = -0.3

    # action[12] = Kp*(q_d - obs[12]) + Kv *(qdot_d - obs[12+13])
    # q.append(obs[:q_dim])
    # qacc.append(np.concatenate([env.env.data.qacc.flat]))
    #
    #next_obs, reward, done, _ = env.step(action)
    #env.env.sim.step()
    print(env.env.sim.data.qpos)
    #obs = next_obs
    
    env.render()
# env.close()

print('inertial = ', 1 / 12.0 * 100 * (2 ** 2 + 1 ** 2))
print('inertial = ', 1 / 12.0 * 100 * (1 ** 2 + 1 ** 2))

print(qacc[0:10])

# inertial =  41.66666666666666
# inertial =  16.666666666666664
# [array([0.]), array([0.02399136]), array([0.02398848]), array([0.02398561]), array([0.02398273]), array([0.02397985]), array([0.02397698]), array([0.0239741]), array([0.02397122]), array([0.02396835])]

# q = np.array(q)
#
# t = np.linspace(0,T,T)
# import matplotlib.pyplot as plt
# plt.figure(figsize=(20, 10))
# for i in range(q_dim):
#     plt.subplot(4, 4, i + 1)
#     plt.title('q{}'.format(i))
#     plt.plot(t * 0.001, q[:, i], label='q')
#     plt.plot(t * 0.001, q_d * np.ones_like(t), label='q_d')
#
# plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
#                     wspace=0.35)
# plt.suptitle('Cell joint angle', fontsize=14)
# plt.legend()
# plt.show()


# for itr in range(1):
# 	env.reset( )
#
# 	for i in range(500):
# 		action = env.action_space.sample()
# 		#action = disable_action(action,6)
# 		#print(action)
# 		next_obs, reward, done, _ = env.step(action)
# 		env.render()
# 		if i==100:
# 			break


# 为了修改模型的颜色!
# goal =0
# self.model.geom_rgba[3+goal,:] =np.array([1,0,0,1])

#
# <torque name ="torque1" site="cell1_1"  />
#         <torque name ="torque2" site="cell2_1"  />
#         <torque name ="torque3" site="cell3_1"  />
#         <torque name ="torque4" site="cell4_1"  />