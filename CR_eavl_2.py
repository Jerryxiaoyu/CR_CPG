import os

root_path = '/home/drl/PycharmProjects/DeployedProjects/CR_CPG'
os.chdir(root_path)
from utils import IO
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

env_name = 'CellrobotSnakeEnv-v0'
task_mode = '2'
results_path = os.path.join(root_path,
                            'Hyper_lab/log-files')
if env_name == 'CellrobotEnv-v0' or env_name == 'Cellrobot2Env-v0':
    CPG_parm_num = 13
    if task_mode == '2':
        from CPG_core.quadruped_osc.oscillator_2 import oscillator_nw
        
        particles_num = 27
    
    elif task_mode == '3':
        from CPG_core.quadruped_osc.oscillator_3 import oscillator_nw
        
        particles_num = 27
    
    elif task_mode == '4':
        from CPG_core.quadruped_osc.oscillator_4 import oscillator_nw
        
        particles_num = 40
    
    elif task_mode == '5':
        from CPG_core.quadruped_osc.oscillator_5 import oscillator_nw
        
        particles_num = 27
    
    elif task_mode == '2_sin':
        from CPG_core.quadruped_osc.oscillator_2_sin import oscillator_nw
        
        particles_num = 40
    
    elif task_mode == '5_sin':
        from CPG_core.quadruped_osc.oscillator_5_sin import oscillator_nw
        
        particles_num = 53
    
    else:
        raise print('task mode does not exist')
elif env_name == 'CellrobotSnakeEnv-v0' or env_name == 'CellrobotSnake2Env-v0':
    CPG_parm_num = 9
    if task_mode == '2':
        from CPG_core.snake_osc.snake_oscillator_2 import oscillator_nw
        
        particles_num = 19
    
    elif task_mode == '2_sin':
        from CPG_core.snake_osc.snake_oscillator_2_sin import oscillator_nw
        
        particles_num = 28
    
    elif task_mode == '5_sin':
        from CPG_core.snake_osc.snake_oscillator_5_sin import oscillator_nw
        
        particles_num = 37
    
    else:
        raise print('task mode does not exist')
elif env_name == 'CellrobotButterflyEnv-v0':
    CPG_parm_num = 7
    if task_mode == '2':
        from CPG_core.butterfly_osc.butterfly_oscillator_2 import oscillator_nw
        
        particles_num = 15
    
    
    elif task_mode == '2_sin':
        from CPG_core.butterfly_osc.butterfly_oscillator_2_sin import oscillator_nw
        
        particles_num = 22
    
    elif task_mode == '5_sin':
        from CPG_core.butterfly_osc.butterfly_oscillator_5_sin import oscillator_nw
        
        particles_num = 29
    
    else:
        raise print('task mode does not exist')
else:
    raise print("env :{} task does not implemented.".format(env_name))

results_dir = os.path.join(results_path, 'results')
monitor_dir = os.path.join(results_dir, 'monitor')
results = IO(os.path.join(results_path, 'results.pkl')).read_pickle()


#plot
# gen = len(results)
# fitness =[]
# for g in range (1, gen+1):
#     fitness.append(results['gen{}'.format(g)]['best_fitness'])
#
# fitness =np.array(fitness)
# gen_x = np.linspace(1,30,30)
# plt.plot(gen_x, fitness)
# plt.show()
#
# if not os.path.isdir(results_dir):
#         os.makedirs(results_dir)  # create path
# if not os.path.isdir(monitor_dir):
#         os.makedirs(monitor_dir)  # create path



#
# for g in range (gen, gen+1):
#     if not os.path.isdir(os.path.join(monitor_dir,'gen{}_best.mp4'.format(g))):
#         pram_vector = results['gen{}'.format(g)]['best_params']
#         oscillator_nw(pram_vector, max_time=10.0,
#                       fitness_option=6, plot = True, log_dis = False, render=True,
#                       monitor_path=os.path.join(monitor_dir,'gen{}_best.mp4'.format(g)),
#                       save_plot_path =None)

pram_vector = results['gen60']['best_params']
# pram_vector = [ 0.99505076,  0.17096604,  1.64309921, -1.64309921, -1.24526202,
#         1.24526202, -1.68959029, -1.20905305,  1.68959029,  1.20905305,
#         0.74654568, -1.40122398,  1.40122398, -1.40122398, -0.56530573,
#        -1.64309921, -0.60423997, -0.37295423, -1.24526202,  1.68959029,
#         1.20905305, -1.1026008 , -0.35349152, -0.96666956,  1.07138776,
#        -1.40122398,  1.40122398,  0.51084239, -1.64309921,  2.76258325,
#        -0.34463933, -1.24526202,  1.68959029,  1.20905305,  0.29542242,
#         0.0029865 ,  0.38054916,  2.82743961, -1.40122398,  1.40122398,
#         1.        , -1.64309921,  1.        ,  1.        , -1.24526202,
#         1.68959029,  1.20905305, -1.        , -1.        , -1.        ,
#        -1.        , -1.40122398,  1.40122398]
oscillator_nw(pram_vector, max_time=10.0,
              fitness_option=6, plot = True, log_dis = False, render=True,
              monitor_path= None,
              save_plot_path =None)


