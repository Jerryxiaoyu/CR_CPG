import os
root_path = '/home/drl/PycharmProjects/DeployedProjects/CR_CPG'

from utils import IO
from CPG_core.quadruped_osc.oscillator_2 import oscillator_nw

results_path = os.path.join(root_path,'log-files/CellrobotEnv-v0/Aug-23_22:14:55GA4_open+weight' )
results_dir = os.path.join(results_path, 'results')
monitor_dir = os.path.join(results_dir, 'monitor')
results = IO(os.path.join(results_path, 'results.pkl')).read_pickle()


gen =30

if not os.path.isdir(results_dir):
        os.makedirs(results_dir)  # create path
if not os.path.isdir(monitor_dir):
        os.makedirs(monitor_dir)  # create path
for g in range (1, gen+1):
    if not os.path.isdir(os.path.join(monitor_dir,'gen{}_best.mp4'.format(g))):
        pram_vector = results['gen{}'.format(g)]['best_params']
        oscillator_nw(pram_vector, max_time=20.0,
                      fitness_option=6, plot = True, log_dis = False, render=False,
                      monitor_path=os.path.join(monitor_dir,'gen{}_best.mp4'.format(g)),
                      save_plot_path =os.path.join(monitor_dir,'gen{}_best.jpg'.format(g)))
    if g ==  gen+1:
        pram_vector = results['gen{}'.format(g)]['best_iparams_ever']
        oscillator_nw(pram_vector, max_time=20.0,
                      fitness_option=6, plot = True, log_dis = False, render=False,
                      monitor_path=os.path.join(monitor_dir,'gen{}_everbest.mp4'.format(g)),
                     save_plot_path =os.path.join(monitor_dir,'gen{}_everbest.jpg'.format(g)))