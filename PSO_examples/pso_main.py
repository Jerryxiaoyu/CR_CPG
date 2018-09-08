import os
import random
import argparse

from deap import base
from deap import creator
from deap import tools
from utils import log, logging_output,configure_log_dir,IO,LoggerCsv


from scoop import futures
import math
import gym
from my_gym_envs.mujoco import *
import operator
import random

import numpy

from deap import base
from deap import benchmarks
from deap import creator
from deap import tools

from scoop import futures
from functools import partial

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Particle", list, fitness=creator.FitnessMax, speed=list,
               smin=None, smax=None, best=None)


parser = argparse.ArgumentParser(description='DeepPILCO')
parser.add_argument('--seed', type=int, default=1)
parser.add_argument('--env_name', type=str, default= 'CellrobotEnv-v0')  #  'CellrobotEnv-v0','Cellrobot2Env-v0','CellrobotSnakeEnv-v0' , 'CellrobotSnake2Env-v0','CellrobotButterflyEnv-v0'
parser.add_argument('--pop_size', type=int, default=8)   # 32
parser.add_argument('--max_gen', type=int, default=1 )  #1000
parser.add_argument('--phi1', type=float, default=2.0)
parser.add_argument('--phi2', type=float, default=2.0)

parser.add_argument('--speed_max', type=float, default=2.0)

parser.add_argument('--task_mode', type=str, default='2_sin' ) # 2, 3, 4, 5
parser.add_argument('--max_time', type=float, default=10.0 )
parser.add_argument('--fitness_mode', type=int, default=6 )
parser.add_argument('--exp_group_dir', type=str, default= None )

parser.add_argument('--gain_max', type=float, default=2.0)
parser.add_argument('--bias_max', type=float, default=90.0) #angle
parser.add_argument('--phase_max', type=float, default=45.0)  #angle

args = parser.parse_args()

print(args)
env_name  = args.env_name
task_mode = args.task_mode


if env_name == 'CellrobotEnv-v0' or env_name == 'Cellrobot2Env-v0' or env_name == 'CellrobotEnv_r-v0':
    CPG_parm_num = 13
    if task_mode == '2':
        from CPG_core.quadruped_osc.oscillator_2 import oscillator_nw
        
        particles_num = 27
        parm_list_key = ['kf','gain', 'bias']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num]
    elif task_mode == '3':
        from CPG_core.quadruped_osc.oscillator_3 import oscillator_nw
        
        particles_num = 27
        parm_list_key = ['kf','gain', 'bias']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num]
    elif task_mode == '4':
        from CPG_core.quadruped_osc.oscillator_4 import oscillator_nw
        
        particles_num = 40
        parm_list_key = ['kf', 'gain', 'bias', 'w']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num, CPG_parm_num]
    elif task_mode == '5':
        from CPG_core.quadruped_osc.oscillator_5 import oscillator_nw
        
        particles_num = 27
        parm_list_key = ['kf','gain', 'w']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num ]
    elif task_mode == '2_sin':
        from CPG_core.quadruped_osc.oscillator_2_sin import oscillator_nw
        
        particles_num = 40
        parm_list_key = ['kf', 'gain', 'bias', 'phase']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num, CPG_parm_num]
    elif task_mode == '5_sin':
        from CPG_core.quadruped_osc.oscillator_5_sin import oscillator_nw
        
        particles_num = 53
        parm_list_key = ['kf', 'gain', 'bias', 'phase', 'w']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num, CPG_parm_num, CPG_parm_num]
    
    elif task_mode == '5g':
        from CPG_core.quadruped_osc.oscillator_5g import oscillator_nw
        
        particles_num = 43
        parm_list_key = ['kf', 'gain', 'phase', 'w']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num, CPG_parm_num ]
    
    else:
        assert print('task mode does not exist')
elif env_name == 'CellrobotSnakeEnv-v0' or env_name == 'CellrobotSnake2Env-v0':
    CPG_parm_num = 9
    if task_mode == '2':
        from CPG_core.snake_osc.snake_oscillator_2 import oscillator_nw
        
        particles_num = 19
        parm_list_key = ['kf', 'gain', 'bias']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num ]
    elif task_mode == '2_sin':
        from CPG_core.snake_osc.snake_oscillator_2_sin import oscillator_nw
        
        particles_num = 28
        parm_list_key = ['kf', 'gain', 'bias', 'phase']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num, CPG_parm_num ]
    elif task_mode == '5_sin':
        from CPG_core.snake_osc.snake_oscillator_5_sin import oscillator_nw
        
        particles_num = 37
        parm_list_key = ['kf', 'gain', 'bias', 'phase', 'w']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num, CPG_parm_num, CPG_parm_num]
    elif task_mode == '2_sin_gb':
        from CPG_core.snake_osc.snake_oscillator_2_sin_gb import oscillator_nw
        
        particles_num = 19
        parm_list_key = ['kf', 'gain', 'bias']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num ]
    else:
        assert print('task mode does not exist')
elif env_name == 'CellrobotButterflyEnv-v0':
    CPG_parm_num = 7
    if task_mode == '2':
        from CPG_core.butterfly_osc.butterfly_oscillator_2 import oscillator_nw
        
        particles_num = 15
        parm_list_key = ['kf', 'gain', 'bias']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num ]
    
    elif task_mode == '2_sin':
        from CPG_core.butterfly_osc.butterfly_oscillator_2_sin import oscillator_nw
        
        particles_num = 22
        parm_list_key = ['kf', 'gain', 'bias', 'phase']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num, CPG_parm_num ]
    elif task_mode == '5_sin':
        from CPG_core.butterfly_osc.butterfly_oscillator_5_sin import oscillator_nw
        
        particles_num = 29
        parm_list_key = ['kf', 'gain', 'bias', 'phase', 'w']

        parm_list_num = [1, CPG_parm_num, CPG_parm_num, CPG_parm_num, CPG_parm_num]
    else:
        assert print('task mode does not exist')
elif env_name == 'CellrobotBigdog2Env-v0':
    CPG_parm_num = 14
    if task_mode == '2':
        from CPG_core.bigdog2_osc.bigdog2_oscillator_2 import oscillator_nw
        
        particles_num = 29
        parm_list_key = ['kf', 'gain', 'bias']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num, ]
    
    elif task_mode == '2_sin':
        from CPG_core.bigdog2_osc.bigdog2_oscillator_2_sin import oscillator_nw
        
        particles_num = 43
        parm_list_key = ['kf', 'gain', 'bias', 'phase']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num, CPG_parm_num ]
    elif task_mode == '5_sin':
        from CPG_core.bigdog2_osc.bigdog2_oscillator_5_sin import oscillator_nw
        
        particles_num = 57
        parm_list_key = ['kf', 'gain', 'bias', 'phase', 'w']

        parm_list_num = [1, CPG_parm_num, CPG_parm_num, CPG_parm_num, CPG_parm_num]
    else:
        assert print('task mode does not exist')
elif env_name == 'CellrobotBigSnakeEnv-v0':
    CPG_parm_num = 16
    if task_mode == '5_singb':
        from CPG_core.snake_osc.bigsnake_oscillator_5_sin_gb import oscillator_nw
        
        particles_num = 33
        parm_list_key = ['kf', 'phase', 'w']

        parm_list_num = [1, CPG_parm_num, CPG_parm_num ]
    elif task_mode == '2_singb':
        from CPG_core.snake_osc.bigsnake_oscillator_2_sin_gb import oscillator_nw
        
        particles_num = 17
        parm_list_key = ['kf', 'phase']
        parm_list_num = [1, CPG_parm_num ]
    elif task_mode == '3_singb':
        from CPG_core.snake_osc.bigsnake_oscillator_3_sin_gb import oscillator_nw
        
        particles_num = 33
        parm_list_key = ['kf', 'gain', 'phase']
        parm_list_num = [1, CPG_parm_num, CPG_parm_num, ]
else:
    assert print("env :{} task does not implemented.".format(args.env_name))


env = gym.make(env_name)
log_name = args.env_name+'_PSO_'+args.task_mode
evaluate_fun = partial(oscillator_nw, env_name=env_name, max_time=args.max_time, fitness_option= args.fitness_mode)


# Create log files
exp_group_dir = args.exp_group_dir
log_dir = configure_log_dir(env_name, txt=log_name,  No_time = False, log_group=  exp_group_dir)
logging_output(log_dir)
logger = LoggerCsv(log_dir, csvname='log_results')
results_IO = IO(os.path.join(log_dir, 'results.pkl'))
args_IO = IO(os.path.join(log_dir, 'args.pkl')).to_pickle(args)

gain_max = args.gain_max
bias_max = args.bias_max
phase_max = args.phase_max

log.info('[System] parmeters: {}'.format(args))
log.info('*********************************************')
log.info('ENV : {}     task_mode: {}'.format(env_name, task_mode) )
log.info('ENV : {}     fitness: {}'.format(env_name, args.fitness_mode) )
log.info('ENV : {}     gain_max: {}'.format(env_name, gain_max) )
log.info('ENV : {}     bias_max: {}'.format(env_name, bias_max ) )
log.info('ENV : {}     phase_max: {}'.format(env_name, phase_max) )

log.info('ENV : {}'.format(env_name) )
log.info('*********************************************')

KEY_RANGE ={
    'kf':   [0,1],
    'gain': [-1 * gain_max, 1 * gain_max],
    'bias': [-math.radians(bias_max), math.radians(bias_max)],
    'phase':[-math.radians(phase_max), math.radians(phase_max)],
    'w':   [-1,1]
}



def parmeter_generate( ):
    parm_list =[]
    
    
    for i, key in enumerate(parm_list_key):
        num = parm_list_num[i]
    
        for j in range(num):
            if key == 'w':
                parm_list.append(random.choice(KEY_RANGE[key]))
            else:
                parm_list.append(random.uniform(KEY_RANGE[key][0], KEY_RANGE[key][1]))

    #parm_list = [random.uniform(pmin,pmax) for _ in range(particles_num)]
 
    return parm_list

def generate(size,   smin, smax, ):
    part = creator.Particle(parmeter_generate())
    part.speed = [random.uniform(smin, smax) for _ in range(size)]
    part.smin = smin
    part.smax = smax
    return part


def updateParticle(part, best, phi1, phi2):
    u1 = (random.uniform(0, phi1) for _ in range(len(part)))
    u2 = (random.uniform(0, phi2) for _ in range(len(part)))
    v_u1 = map(operator.mul, u1, map(operator.sub, part.best, part))
    v_u2 = map(operator.mul, u2, map(operator.sub, best, part))
    part.speed = list(map(operator.add, part.speed, map(operator.add, v_u1, v_u2)))
    for i, speed in enumerate(part.speed):
        if speed < part.smin:
            part.speed[i] = part.smin
        elif speed > part.smax:
            part.speed[i] = part.smax
    part[:] = list(map(operator.add, part, part.speed))


toolbox = base.Toolbox()
toolbox.register("particle", generate, size= particles_num,   smin=-1 *args.speed_max, smax=1 *args.speed_max)
toolbox.register("population", tools.initRepeat, list, toolbox.particle)
toolbox.register("update", updateParticle, phi1= args.phi1, phi2= args.phi2)
toolbox.register("evaluate", evaluate_fun)  #oscillator_nw

# Size of the population
POP_SIZE = args.pop_size

# Set scoop multiprocessing map
toolbox.register("map", futures.map)

def main():
    log.infov('[PSO] Starting PSO algorithm')
    
    pop = toolbox.population(n=POP_SIZE)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    logbook = tools.Logbook()
    logbook.header = ["gen", "evals"] + stats.fields

    # Maximum generations
    MAX_GEN = args.max_gen
    best = None

    
    
    for g in range(MAX_GEN):
        
        fitnesses = toolbox.map(toolbox.evaluate, pop)
        for part, fit in zip(pop, fitnesses):
            part.fitness.values = (fit['fitness'],)
   
            if not part.best or part.best.fitness < part.fitness:
                part.best = creator.Particle(part)
                part.best.fitness.values = part.fitness.values
            if not best or best.fitness < part.fitness:
                best = creator.Particle(part)
                best.fitness.values = part.fitness.values
        for part in pop:
            toolbox.update(part, best)
        
        # Gather all the fitnesses in one list and print the stats
        logbook.record(gen=g, evals=len(pop), **stats.compile(pop))
        log.info(logbook.stream)

        result = {'gen{}'.format(g): {
            'best_params': [best[i] for i in range(len(best))],
            'best_fitness':best.fitness.values[0] , }}
        if g == 0:
            results = result
        else:
            results.update(result)
        results_IO.to_pickle(results)
        

        logger.log({'generation':g,
                   'best_params':[best[i] for i in range(len(best))],
                   'best_fitness':best.fitness.values[0],
                    })
        logger.write(display=False)

    log.infov('best ={}'.format(best.fitness.values[0]))
    log.infov('best parm :{}'.format([best[i] for i in range(len(best))]))

    return pop, logbook, best


if __name__ == "__main__":
    main()