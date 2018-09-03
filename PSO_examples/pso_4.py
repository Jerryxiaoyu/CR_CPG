import os
import random
import argparse

from deap import base
from deap import creator
from deap import tools
from utils import log, logging_output,configure_log_dir,IO,LoggerCsv
from CPG_core.quadruped_osc.oscillator_2 import oscillator_nw

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
from CPG_core.quadruped_osc.oscillator_4 import oscillator_nw
from scoop import futures


creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Particle", list, fitness=creator.FitnessMax, speed=list,
               smin=None, smax=None, best=None)


parser = argparse.ArgumentParser(description='DeepPILCO')
parser.add_argument('--seed', type=int, default=1)
parser.add_argument('--env_name', type=str, default='CellrobotEnv-v0')  #  Ant2-v2  HalfCheetah-v2  ArmReacherEnv-v0  Hopper2-v2: Swimmer2-v2
parser.add_argument('--pop_size', type=int, default=8)
parser.add_argument('--max_gen', type=int, default=1000)
parser.add_argument('--CXPB', type=float, default=0.8)
parser.add_argument('--MUTPB', type=float, default=0.1)
parser.add_argument('--gain_max', type=float, default=2.0)
parser.add_argument('--speed_max', type=float, default=2.0)
args = parser.parse_args()


env_name  = args.env_name
env = gym.make(env_name)
log_name = 'PSO4_open'


# Set the logging variables
# This also creates a new log file
# Create log files
log_dir = configure_log_dir(env_name, txt=log_name,  No_time = False)
logging_output(log_dir)
logger = LoggerCsv(log_dir, csvname='log_results')
results_IO = IO(os.path.join(log_dir, 'results.pkl'))
args_IO = IO(os.path.join(log_dir, 'args.pkl')).to_pickle(args)




def parmeter_generate(pmin,pmax):
    parm_list = [random.uniform(pmin,pmax) for _ in range(27)]
 
    return parm_list

def generate(size, pmin, pmax, smin, smax):
    part = creator.Particle(parmeter_generate(pmin, pmax))
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
toolbox.register("particle", generate, size=27, pmin=-1 *args.gain_max, pmax=1 *args.gain_max, smin=-1 *args.speed_max, smax=1 *args.speed_max)
toolbox.register("population", tools.initRepeat, list, toolbox.particle)
toolbox.register("update", updateParticle, phi1=2.0, phi2=2.0)
toolbox.register("evaluate", oscillator_nw)  #oscillator_nw

# Size of the population
POP_SIZE = args.pop_size

# Set scoop multiprocessing map
toolbox.register("map", futures.map)

def main():
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
        print(logbook.stream)

        result = {'gen{}'.format(g): {
            'best_params': [best[i] for i in range(len(best))],
            'best_fitness':best.fitness.values[0] , }}
        if g == 0:
            results = result
        else:
            results.update(result)
        results_IO.to_pickle(results)

    print('best = ',best.fitness.values[0])
    print('best parm :', [best[i] for i in range(len(best))])

    return pop, logbook, best


if __name__ == "__main__":
    main()