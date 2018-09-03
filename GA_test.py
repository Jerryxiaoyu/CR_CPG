from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from deap import creator, base, tools, algorithms
import random
import os
from utils import log
def fitness_function(parm):
    return  -(parm[0]**2 + parm[1]**3)

from itertools import repeat
from collections import Sequence

def MYmutGaussian(individual, mu, sigma, indpb):
    """This function applies a gaussian mutation of mean *mu* and standard
    deviation *sigma* on the input individual. This mutation expects a
    :term:`sequence` individual composed of real valued attributes.
    The *indpb* argument is the probability of each attribute to be mutated.

    :param individual: Individual to be mutated.
    :param mu: Mean or :term:`python:sequence` of means for the
               gaussian addition mutation.
    :param sigma: Standard deviation or :term:`python:sequence` of
                  standard deviations for the gaussian addition mutation.
    :param indpb: Independent probability for each attribute to be mutated.
    :returns: A tuple of one individual.

    This function uses the :func:`~random.random` and :func:`~random.gauss`
    functions from the python base :mod:`random` module.
    """
    size = len(individual)
    if not isinstance(mu, Sequence):
        mu = repeat(mu, size)
    elif len(mu) < size:
        raise IndexError("mu must be at least the size of individual: %d < %d" % (len(mu), size))
    if not isinstance(sigma, Sequence):
        sigma = repeat(sigma, size)
    elif len(sigma) < size:
        raise IndexError("sigma must be at least the size of individual: %d < %d" % (len(sigma), size))
    
    for i, m, s in zip(range(size), mu, sigma):
        if random.random() < indpb:
            if isinstance(individual[i],int):
                individual[i] = random.choice([-1, 1])
            else:
                individual[i] += random.gauss(m, s)
    
    return individual,

# Create the parmeters bounds of the individual
FLT_MIN_X, FLT_MAX_X = -1, 2
FLT_MIN_Y, FLT_MAX_Y = -1, 2

# Define a custom class named `FitnessMax`
# Single objective function is specified by the tuple `weights=(1.0,)`
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# Create a class named `Individual` which inherits from the class `list` and has `FitnessMax` as an attribute
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox = base.Toolbox()

# Attribute generator - specify how each single gene is to be created
toolbox.register("x_fit", random.randrange, FLT_MIN_X, FLT_MAX_X)
toolbox.register("y_fit", random.randrange, FLT_MIN_Y, FLT_MAX_Y)


# Specify the structure of an individual chromosome
N_CYCLES=1 # Number of times to repeat this pattern

# Specify the sequence of genes in an individual chromosome
toolbox.register("individual", tools.initCycle, creator.Individual,
                 (toolbox.x_fit,
                  toolbox.y_fit),
                 n=N_CYCLES)

# Define the population to be a list of individuals
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Register the goal / fitness function
toolbox.register("evaluate", fitness_function)
# Register the crossover operator - 2 point crossover is used here
toolbox.register("mate", tools.cxTwoPoint)

toolbox.register("mutate", MYmutGaussian, mu=0.0, sigma=0.01, indpb=0.05)

# drawn randomly from the current generation.
toolbox.register("select", tools.selTournament, tournsize=3)

# Size of the population
POP_SIZE = 200

# Maximum generations
MAX_GEN = 31


# Create an initial population of `POP_SIZE` individuals (where each individual is a list of floats)
pop = toolbox.population(n=POP_SIZE)

# CXPB  is the probability with which two individuals are crossed
# MUTPB is the probability for mutating an individual
CXPB, MUTPB = 0.8, 0.1

log.infov('[GA] Starting genetic algorithm')

# Evaluate the entire population and store the fitness of each individual
log.infov('[GA] Finding the fitness of individuals in the initial generation')
fitnesses = list(map(toolbox.evaluate, pop))
for ind, fit in zip(pop, fitnesses):
    print(ind, fit)
    ind.fitness.values = (fit,)

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
    log.infov('[GA] Running generation {0}'.format(g))

    # Select the next generation individuals
    log.infov('[GA] Selecting the next generation')
    offspring = toolbox.select(pop, len(pop))
    # Clone the selected individuals
    offspring = list(map(toolbox.clone, offspring))

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
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = (fit,)

    log.infov('[GA] Evaluated {0} individuals (invalid fitness)'.format(len(invalid_ind)))

    # The population is entirely replaced by the offspring
    pop[:] = offspring

    # Gather all the fitnesses in one list and print the stats
    fits = [ind.fitness.values[0] for ind in pop]

    length = len(pop)
    mean = sum(fits) / length
    sum2 = sum(x * x for x in fits)
    std = abs(sum2 / length - mean ** 2) ** 0.5

    log.info('[GA] Results for generation {0}'.format(g))
    log.info('[GA] Min %s' % min(fits))
    log.info('[GA] Max %s' % max(fits))
    log.info('[GA] Avg %s' % mean)
    log.info('[GA] Std %s' % std)

    best_ind_g = tools.selBest(pop, 1)[0]

    # Store the best individual over all generations
    if best_ind_g.fitness.values[0] > best_fitness_ever:
        best_fitness_ever = best_ind_g.fitness.values[0]
        best_ind_ever = best_ind_g

    log.info('[GA] Best individual for generation {0}: {1}, {2}'.format(g, best_ind_g, best_ind_g.fitness.values[0]))
    log.info('[GA] Best individual ever till now: %s, %s' % (best_ind_ever, best_fitness_ever))

    log.infov('[GA] ############################# End of generation {0} #############################'.format(g))

log.infov('[GA] ===================== End of evolution =====================')

best_ind = tools.selBest(pop, 1)[0]
log.infov('[GA] Best individual in the population: %s, %s' % (best_ind, best_ind.fitness.values[0]))
log.infov('[GA] Best individual ever: %s, %s' % (best_ind_ever, best_fitness_ever))