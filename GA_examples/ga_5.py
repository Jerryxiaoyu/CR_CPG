import os
import random
import argparse

from deap import base
from deap import creator
from deap import tools
from utils import log, logging_output,configure_log_dir,IO,LoggerCsv
from CPG_core.quadruped_osc.oscillator_5 import oscillator_nw
from CPG_core.my_GA import MYmutGaussian
from scoop import futures
import math
import gym
from my_gym_envs.mujoco import *

parser = argparse.ArgumentParser(description='DeepPILCO')
parser.add_argument('--seed', type=int, default=1)
parser.add_argument('--env_name', type=str, default='CellrobotEnv-v0')  #  Ant2-v2  HalfCheetah-v2  ArmReacherEnv-v0  Hopper2-v2: Swimmer2-v2
parser.add_argument('--pop_size', type=int, default=1)
parser.add_argument('--max_gen', type=int, default=3)
parser.add_argument('--CXPB', type=float, default=0.8)
parser.add_argument('--MUTPB', type=float, default=0.1)
parser.add_argument('--gain_max', type=float, default=2.0)
args = parser.parse_args()


env_name  = args.env_name
env = gym.make(env_name)
log_name = 'GA5_open+weight-nobias'


# Set the logging variables
# This also creates a new log file
# Create log files
log_dir = configure_log_dir(env_name, txt=log_name,  No_time = False)
logging_output(log_dir)
logger = LoggerCsv(log_dir, csvname='log_results')
results_IO = IO(os.path.join(log_dir, 'results.pkl'))
args_IO = IO(os.path.join(log_dir, 'args.pkl')).to_pickle(args)


# Create the position bounds of the individual
log.info('[System] parmeters: {}'.format(args))
log.infov('[GA] Running ga_2')
log.infov('[GA] Creating position bounds')
FLT_MIN_KF,    FLT_MAX_KF    = 0.2, 1.0
FLT_MIN_GAIN0, FLT_MAX_GAIN0 = -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_GAIN1, FLT_MAX_GAIN1 =  -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_GAIN2, FLT_MAX_GAIN2 =  -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_GAIN3, FLT_MAX_GAIN3 =  -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_GAIN4, FLT_MAX_GAIN4 =  -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_GAIN5, FLT_MAX_GAIN5 =  -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_GAIN6, FLT_MAX_GAIN6 = -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_GAIN7, FLT_MAX_GAIN7 =  -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_GAIN8, FLT_MAX_GAIN8 =  -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_GAIN9, FLT_MAX_GAIN9 =  -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_GAIN10, FLT_MAX_GAIN10 =  -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_GAIN11, FLT_MAX_GAIN11 =  -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_GAIN12, FLT_MAX_GAIN12 =  -1 *args.gain_max, 1 *args.gain_max
WEIGHTS_LIST =[-1,1]



log.infov('[GA] Logging position bounds')
log.info('[GA] FLT_MIN_KF={0}, FLT_MAX_KF={1}'.format(FLT_MIN_KF, FLT_MAX_KF))
log.info('[GA] FLT_MIN_GAIN0={0}, FLT_MAX_GAIN0={1}'.format(FLT_MIN_GAIN0, FLT_MAX_GAIN0))
log.info('[GA] FLT_MIN_GAIN1={0}, FLT_MAX_GAIN1={1}'.format(FLT_MIN_GAIN1, FLT_MAX_GAIN1))
log.info('[GA] FLT_MIN_GAIN2={0}, FLT_MAX_GAIN2={1}'.format(FLT_MIN_GAIN2, FLT_MAX_GAIN2))
log.info('[GA] FLT_MIN_GAIN3={0}, FLT_MAX_GAIN3={1}'.format(FLT_MIN_GAIN3, FLT_MAX_GAIN3))
log.info('[GA] FLT_MIN_GAIN4={0}, FLT_MAX_GAIN4={1}'.format(FLT_MIN_GAIN4, FLT_MAX_GAIN4))
log.info('[GA] FLT_MIN_GAIN5={0}, FLT_MAX_GAIN5={1}'.format(FLT_MIN_GAIN5, FLT_MAX_GAIN5))
log.info('[GA] FLT_MIN_GAIN6={0}, FLT_MAX_GAIN6={1}'.format(FLT_MIN_GAIN6, FLT_MAX_GAIN6))
log.info('[GA] FLT_MIN_GAIN7={0}, FLT_MAX_GAIN7={1}'.format(FLT_MIN_GAIN7, FLT_MAX_GAIN7))
log.info('[GA] FLT_MIN_GAIN8={0}, FLT_MAX_GAIN8={1}'.format(FLT_MIN_GAIN8, FLT_MAX_GAIN8))
log.info('[GA] FLT_MIN_GAIN9={0}, FLT_MAX_GAIN9={1}'.format(FLT_MIN_GAIN9, FLT_MAX_GAIN9))
log.info('[GA] FLT_MIN_GAIN10={0}, FLT_MAX_GAIN10={1}'.format(FLT_MIN_GAIN10, FLT_MAX_GAIN10))
log.info('[GA] FLT_MIN_GAIN11={0}, FLT_MAX_GAIN11={1}'.format(FLT_MIN_GAIN11, FLT_MAX_GAIN11))
log.info('[GA] FLT_MIN_GAIN12={0}, FLT_MAX_GAIN12={1}'.format(FLT_MIN_GAIN12, FLT_MAX_GAIN12))



# Define a custom class named `FitnessMax`
# Single objective function is specified by the tuple `weights=(1.0,)`
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# Create a class named `Individual` which inherits from the class `list` and has `FitnessMax` as an attribute
creator.create("Individual", list, fitness=creator.FitnessMax)

# Now we will use our custom classes to create types representing our individuals as well as our whole population.
# All the objects we will use on our way, an individual, the population, as well as all functions, operators, and
# arguments will be stored in a DEAP container called `Toolbox`. It contains two methods for adding and removing
# content, register() and unregister().

toolbox = base.Toolbox()

# Attribute generator - specify how each single gene is to be created
toolbox.register("kf_flt", random.uniform, FLT_MIN_KF, FLT_MAX_KF)
toolbox.register("gain0_flt", random.uniform, FLT_MIN_GAIN0, FLT_MAX_GAIN0)
toolbox.register("gain1_flt", random.uniform, FLT_MIN_GAIN1, FLT_MAX_GAIN1)
toolbox.register("gain2_flt", random.uniform, FLT_MIN_GAIN2, FLT_MAX_GAIN2)
toolbox.register("gain3_flt", random.uniform, FLT_MIN_GAIN3, FLT_MAX_GAIN3)
toolbox.register("gain4_flt", random.uniform, FLT_MIN_GAIN4, FLT_MAX_GAIN4)
toolbox.register("gain5_flt", random.uniform, FLT_MIN_GAIN5, FLT_MAX_GAIN5)
toolbox.register("gain6_flt", random.uniform, FLT_MIN_GAIN6, FLT_MAX_GAIN6)
toolbox.register("gain7_flt", random.uniform, FLT_MIN_GAIN7, FLT_MAX_GAIN7)
toolbox.register("gain8_flt", random.uniform, FLT_MIN_GAIN8, FLT_MAX_GAIN8)
toolbox.register("gain9_flt", random.uniform, FLT_MIN_GAIN9, FLT_MAX_GAIN9)
toolbox.register("gain10_flt", random.uniform, FLT_MIN_GAIN10, FLT_MAX_GAIN10)
toolbox.register("gain11_flt", random.uniform, FLT_MIN_GAIN11, FLT_MAX_GAIN11)
toolbox.register("gain12_flt", random.uniform, FLT_MIN_GAIN12, FLT_MAX_GAIN12)




toolbox.register("w1_flt", random.choice, WEIGHTS_LIST)
toolbox.register("w2_flt", random.choice, WEIGHTS_LIST)
toolbox.register("w3_flt", random.choice, WEIGHTS_LIST)
toolbox.register("w4_flt", random.choice, WEIGHTS_LIST)
toolbox.register("w5_flt", random.choice, WEIGHTS_LIST)
toolbox.register("w6_flt", random.choice, WEIGHTS_LIST)
toolbox.register("w7_flt", random.choice, WEIGHTS_LIST)
toolbox.register("w8_flt", random.choice, WEIGHTS_LIST)
toolbox.register("w9_flt", random.choice, WEIGHTS_LIST)
toolbox.register("w10_flt", random.choice, WEIGHTS_LIST)
toolbox.register("w11_flt", random.choice, WEIGHTS_LIST)
toolbox.register("w12_flt", random.choice, WEIGHTS_LIST)
toolbox.register("w13_flt", random.choice, WEIGHTS_LIST)

# Specify the structure of an individual chromosome
N_CYCLES=1 # Number of times to repeat this pattern

# Specify the sequence of genes in an individual chromosome
toolbox.register("individual", tools.initCycle, creator.Individual,
                 (toolbox.kf_flt,toolbox.gain0_flt,
                  toolbox.gain1_flt, toolbox.gain2_flt, toolbox.gain3_flt,
                  toolbox.gain4_flt, toolbox.gain5_flt, toolbox.gain6_flt,
                  toolbox.gain7_flt, toolbox.gain8_flt, toolbox.gain9_flt,
                  toolbox.gain10_flt, toolbox.gain11_flt, toolbox.gain12_flt,
                  toolbox.w1_flt, toolbox.w2_flt, toolbox.w3_flt, toolbox.w4_flt,
                    toolbox.w5_flt, toolbox.w6_flt, toolbox.w7_flt, toolbox.w8_flt,
                    toolbox.w9_flt, toolbox.w10_flt, toolbox.w11_flt, toolbox.w12_flt,
                    toolbox.w13_flt
                  ),
                 n=N_CYCLES)

# Define the population to be a list of individuals
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Register the goal / fitness function
toolbox.register("evaluate", oscillator_nw)

# Register the crossover operator - 2 point crossover is used here
toolbox.register("mate", tools.cxTwoPoint)

# Register a mutation operator
# Mutation is done by adding a float to each gene. This float to be added is randomly selected from a Gaussian
# distribution with mu=0.0 and sigma=0.01
# Probability of mutation is 0.05
toolbox.register("mutate", MYmutGaussian, mu=0.0, sigma=0.01, indpb=0.05, int_list=WEIGHTS_LIST)

# Operator for selecting individuals for breeding the next
# generation: each individual of the current generation
# is replaced by the 'fittest' (best) of 3 individuals
# drawn randomly from the current generation.
# drawn randomly from the current generation.
toolbox.register("select", tools.selTournament, tournsize=3)

# Set scoop multiprocessing map
toolbox.register("map", futures.map)

# Size of the population
POP_SIZE = args.pop_size

# Maximum generations
MAX_GEN = args.max_gen

def main():
    random.seed(64)

    # Create an initial population of `POP_SIZE` individuals (where each individual is a list of floats)
    pop = toolbox.population(n=POP_SIZE)
    
    # CXPB  is the probability with which two individuals are crossed
    # MUTPB is the probability for mutating an individual
    CXPB, MUTPB = args.CXPB, args.MUTPB

    log.infov('[GA] Starting genetic algorithm')

    # Evaluate the entire population and store the fitness of each individual
    log.infov('[GA] Finding the fitness of individuals in the initial generation')
    fitnesses = list(toolbox.map(toolbox.evaluate, pop))
    #log_save_info(fitnesses)
    for ind, fit in zip(pop, fitnesses):
        #print(ind, fit)
        ind.fitness.values = (fit['fitness'],)

    # Extracting all the fitnesses
    fits = [ind.fitness.values[0] for ind in pop]

    # Variable keeping track of the number of generations
    g = 0

    best_ind_ever = None
    best_fitness_ever = 0.0

    # Begin the evolution
    while max(fits) < 100 and g < MAX_GEN:

        # A new generation
        g = g + 1
        log.infov('[GA{}] Running generation {}'.format(g,g))

        # Select the next generation individuals
        log.info('[GA{}] Selecting the next generation'.format(g))
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(toolbox.map(toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            # cross two individuals with probability CXPB
            if random.random() < CXPB:
                toolbox.mate(child1, child2)

                # fitness values of the children
                # must be recalculated later
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            # mutate an individual with probability MUTPB
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Since the content of some of our offspring changed during the last step, we now need to
        # re-evaluate their fitnesses. To save time and resources, we just map those offspring which
        # fitnesses were marked invalid.
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            print(ind, fit)
            ind.fitness.values = (fit['fitness'],)

        log.info('[GA{}] Evaluated {} individuals (invalid fitness)'.format(g,len(invalid_ind)))

        # The population is entirely replaced by the offspring
        pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        std = abs(sum2 / length - mean ** 2) ** 0.5

        log.info('[GA{}] Results for generation {}'.format(g,g))
        log.info('[GA{}] Min {}'.format(g, min(fits)))
        log.info('[GA{}] Max {}'.format(g, max(fits)))
        log.info('[GA{}] Avg {}'.format(g, mean) )
        log.info('[GA{}] Std {}'.format(g, std))
        

        best_ind_g = tools.selBest(pop, 1)[0]

        # Store the best individual over all generations
        if best_ind_g.fitness.values[0] > best_fitness_ever:
            best_fitness_ever = best_ind_g.fitness.values[0]
            best_ind_ever = best_ind_g

        log.info('[GA{}] Best individual for generation {}: {}, {}'.format(g,g, best_ind_g, best_ind_g.fitness.values[0]))
        log.info('[GA{}] Best individual ever till now: {}, {}' .format(g, best_ind_ever, best_fitness_ever))
        
        
        best_pram_list = [ best_ind_g[_] for _ in range(len(best_ind_g))]
        best_pram_ever_list  = [ best_ind_ever[_] for _ in range(len(best_ind_ever))]
        
        result = {'gen{}'.format(g):{
                   'best_params':best_pram_list,
                   'best_fitness':best_ind_g.fitness.values[0],
                   'best_iparams_ever':best_pram_ever_list,
                   'best_fitness_ever':best_fitness_ever,}}
        if g == 1:
            results = result
        else:
            results.update(result)
        results_IO.to_pickle(results)
        
        logger.log({'generation':g,
                   'best_params':best_ind_g,
                   'best_fitness':best_ind_g.fitness.values[0],
                   'best_iparams_ever':best_ind_ever,
                   'best_fitness_ever':best_fitness_ever,})
        logger.write(display=False)

        log.infov('[GA{0}] ############################# End of generation  #############################'.format(g))
        
    log.infov('===================== End of evolution =====================')

    best_ind = tools.selBest(pop, 1)[0]
    log.infov('Best individual in the population: %s, %s' % (best_ind, best_ind.fitness.values[0]))
    log.infov('Best individual ever: %s, %s' % (best_ind_ever, best_fitness_ever))



if __name__ == "__main__":
    main()
