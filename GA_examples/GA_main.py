import os
import random
import argparse

from deap import base
from deap import creator
from deap import tools
from utils import log, logging_output,configure_log_dir,IO,LoggerCsv
from CPG_core.quadruped_osc.oscillator_2_sin import oscillator_nw
from CPG_core.my_GA import MYmutGaussian
from scoop import futures
import math
import gym
from my_gym_envs.mujoco import *
from functools import partial

parser = argparse.ArgumentParser(description='DeepPILCO')
parser.add_argument('--seed', type=int, default=1)
parser.add_argument('--env_name', type=str, default='CellrobotBigdog2Env-v0')  #  'CellrobotEnv-v0', 'Cellrobot2Env-v0','CellrobotSnakeEnv-v0' , 'CellrobotSnake2Env-v0','CellrobotButterflyEnv-v0'
parser.add_argument('--pop_size', type=int, default=1) #
parser.add_argument('--max_gen', type=int, default=3)
parser.add_argument('--CXPB', type=float, default=0.8)
parser.add_argument('--MUTPB', type=float, default=0.1)
parser.add_argument('--gain_max', type=float, default=2.0)

parser.add_argument('--task_mode', type=str, default='2' ) # 2, 3, 4, 5
parser.add_argument('--max_time', type=float, default=10.0 )
parser.add_argument('--fitness_mode', type=int, default=6 )
parser.add_argument('--exp_group_dir', type=str, default= None )
args = parser.parse_args()


print(args)
env_name  = args.env_name
task_mode = args.task_mode
if env_name == 'CellrobotEnv-v0' or env_name == 'Cellrobot2Env-v0' or env_name == 'CellrobotEnv_r-v0':
    CPG_parm_num = 13
    if task_mode == '2':
        from CPG_core.quadruped_osc.oscillator_2 import oscillator_nw
        particles_num = 27
        parm_list_key = ['gain', 'bias']
        mutate_fun = tools.mutGaussian
    elif task_mode =='3':
        from CPG_core.quadruped_osc.oscillator_3 import oscillator_nw
        particles_num = 27
        parm_list_key = ['gain', 'bias']
        mutate_fun = tools.mutGaussian
    elif task_mode == '4':
        from CPG_core.quadruped_osc.oscillator_4 import oscillator_nw
        particles_num = 40
        parm_list_key = ['gain', 'bias','w']
        mutate_fun = tools.mutGaussian
    elif task_mode == '5':
        from CPG_core.quadruped_osc.oscillator_5 import oscillator_nw
        particles_num = 27
        parm_list_key = ['gain', 'w']
        mutate_fun = tools.mutGaussian
    elif task_mode == '2_sin':
        from CPG_core.quadruped_osc.oscillator_2_sin import oscillator_nw
        particles_num = 40
        parm_list_key = ['gain', 'bias','phase']
        mutate_fun = tools.mutGaussian
    elif task_mode == '5_sin':
        from CPG_core.quadruped_osc.oscillator_5_sin import oscillator_nw
        particles_num = 53
        parm_list_key = ['gain', 'bias', 'phase','w']
        mutate_fun = MYmutGaussian
    else:
        assert print('task mode does not exist')
elif env_name == 'CellrobotSnakeEnv-v0' or env_name == 'CellrobotSnake2Env-v0':
    CPG_parm_num = 9
    if task_mode == '2':
        from CPG_core.snake_osc.snake_oscillator_2 import oscillator_nw
        particles_num = 19
        parm_list_key = ['gain', 'bias' ]
        mutate_fun = tools.mutGaussian
    elif task_mode == '2_sin':
        from CPG_core.snake_osc.snake_oscillator_2_sin import oscillator_nw
        particles_num = 28
        parm_list_key = ['gain', 'bias', 'phase']
        mutate_fun = tools.mutGaussian
    elif task_mode == '5_sin':
        from CPG_core.snake_osc.snake_oscillator_5_sin import oscillator_nw
        particles_num = 37
        parm_list_key = ['gain', 'bias', 'phase', 'w']
        mutate_fun = MYmutGaussian
    else:
        assert print('task mode does not exist')
elif env_name == 'CellrobotButterflyEnv-v0'  :
    CPG_parm_num = 7
    if task_mode == '2':
        from CPG_core.butterfly_osc.butterfly_oscillator_2 import oscillator_nw
        particles_num = 15
        parm_list_key = ['gain', 'bias']
        mutate_fun = tools.mutGaussian
        
    elif task_mode == '2_sin':
        from CPG_core.butterfly_osc.butterfly_oscillator_2_sin import oscillator_nw
        particles_num = 22
        parm_list_key = ['gain', 'bias', 'phase']
        mutate_fun = tools.mutGaussian
    elif task_mode == '5_sin':
        from CPG_core.butterfly_osc.butterfly_oscillator_5_sin import oscillator_nw
        particles_num = 29
        parm_list_key = ['gain', 'bias', 'phase', 'w']

        mutate_fun = MYmutGaussian
    else:
        assert print('task mode does not exist')
elif env_name == 'CellrobotBigdog2Env-v0':
    CPG_parm_num = 14
    if task_mode == '2':
        from CPG_core.bigdog2_osc.bigdog2_oscillator_2 import oscillator_nw
    
        particles_num = 29
        parm_list_key = ['gain', 'bias']
        mutate_fun = tools.mutGaussian

    elif task_mode == '2_sin':
        from CPG_core.bigdog2_osc.bigdog2_oscillator_2_sin import oscillator_nw
    
        particles_num = 43
        parm_list_key = ['gain', 'bias', 'phase']
        mutate_fun = tools.mutGaussian
    elif task_mode == '5_sin':
        from CPG_core.bigdog2_osc.bigdog2_oscillator_5_sin import oscillator_nw
    
        particles_num = 57
        parm_list_key = ['gain', 'bias', 'phase', 'w']
    
        mutate_fun = MYmutGaussian
    else:
        assert print('task mode does not exist')
    
else:
    assert print("env :{} task does not implemented.".format(args.env_name))


env = gym.make(env_name)
log_name = args.env_name+'_GA_'+args.task_mode
evaluate_fun = partial(oscillator_nw, env_name=env_name, max_time=args.max_time, fitness_option= args.fitness_mode)



# Set the logging variables
# This also creates a new log file
# Create log files
exp_group_dir = args.exp_group_dir
log_dir = configure_log_dir(env_name, txt=log_name,  No_time = False, log_group=  exp_group_dir)
logging_output(log_dir)
logger = LoggerCsv(log_dir, csvname='log_results')
results_IO = IO(os.path.join(log_dir, 'results.pkl'))
args_IO = IO(os.path.join(log_dir, 'args.pkl')).to_pickle(args)

# Create the position bounds of the individual
log.info('[System] parmeters: {}'.format(args))
log.info('*********************************************')
log.info('ENV : {}               task_mode: {}'.format(env_name, task_mode) )
log.info('particles_num : {}   '.format(particles_num ) )
log.info('ENV : {}'.format(env_name) )

log.info('*********************************************')
log.infov('[GA] Running ga_2')
log.infov('[GA] Creating position bounds')
FLT_MIN_KF,    FLT_MAX_KF    = 0.2, 1.0
FLT_MIN_GAIN, FLT_MAX_GAIN = -1 *args.gain_max, 1 *args.gain_max
FLT_MIN_BIAS, FLT_MAX_BIAS = -math.radians(90), math.radians(90)
FLT_MIN_PHASE, FLT_MAX_PHASE = -math.radians(180), math.radians(180)
KEY_RANGE ={
    'gain': [-1 *args.gain_max, 1 *args.gain_max],
    'bias': [-math.radians(90), math.radians(90)],
    'phase':[-math.radians(180), math.radians(180)],
    'w':   [-1,1]
}




log.infov('[GA] Logging position bounds')
log.info('[GA] FLT_MIN_KF={0}, FLT_MAX_KF={1}'.format(FLT_MIN_KF, FLT_MAX_KF))
log.info('[GA] FLT_MIN_GAIN0={0}, FLT_MAX_GAIN0={1}'.format(FLT_MIN_GAIN, FLT_MAX_GAIN))
log.info('[GA] FLT_MIN_BIAS0={0}, FLT_MAX_BIAS0={1}'.format(FLT_MIN_BIAS, FLT_MAX_BIAS))
log.info('[GA] FLT_MIN_PHASE={0}, FLT_MAX_PHASE={1}'.format(FLT_MIN_PHASE, FLT_MAX_PHASE))



# Define a custom class named `FitnessMax`
# Single objective function is specified by the tuple `weights=(1.0,)`
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# Create a class named `Individual` which inherits from the class `list` and has `FitnessMax` as an attribute
creator.create("Individual", list, fitness=creator.FitnessMax)

# Now we will use our custom classes to create types representing our individuals as well as our whole population.
# All the objects we will use on our way, an individual, the population, as well as all functions, operators, and
# arguments will be stored in a DEAP container called `Toolbox`. It contains two methods for adding and removing
# content, register() and unregister().

# Attribute generator - specify how each single gene is to be created

toolbox = base.Toolbox()
toolbox.register("kf_flt", random.uniform, FLT_MIN_KF, FLT_MAX_KF)


for i in range(CPG_parm_num):
        for key in parm_list_key:
            toolbox.register(key+"{}_flt".format(i), random.uniform, KEY_RANGE[key][0], KEY_RANGE[key][1])
            if key == 'w':
                toolbox.register(key + "{}_flt".format(i), random.choice, KEY_RANGE[key])
         
toolbox_parm_list = []
toolbox_parm_list.append(getattr(toolbox, 'kf_flt'))

for key in parm_list_key:
    for i in range(CPG_parm_num):
        toolbox_parm_list.append(getattr(toolbox, key+'{}_flt'.format(i)))
 
if len(toolbox_parm_list) != particles_num:
    assert "Parmeter num does not match"
    
    
# Specify the structure of an individual chromosome
N_CYCLES=1 # Number of times to repeat this pattern



toolbox.register("individual", tools.initCycle, creator.Individual,
                 toolbox_parm_list,
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
if 'w' in parm_list_key:
    toolbox.register("mutate", mutate_fun , mu=0.0, sigma=0.01, indpb=0.05,  int_list=KEY_RANGE['w'])
else:
    toolbox.register("mutate", mutate_fun , mu=0.0, sigma=0.01, indpb=0.05 )
    
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
