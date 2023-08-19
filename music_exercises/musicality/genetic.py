from deap import creator, base, tools
def genetic(initial_melody, scale):
    from musicality.constants import NGEN, PARENTS_TO_OFFSPRING, OFFSPRING_TO_NEXT_GEN, CONVERGE_LIMIT
    from musicality.helpers import printProgressBar

    toolbox = _initialize_genetic(initial_melody, scale)
    print('Creating initial population for GA...')
    #create initial population
    pop = toolbox.population()
    fitnesses = list(toolbox.map(toolbox.evaluate, pop))
    # print()
    print('GA optimization in progress...')
    for ind, fit in zip(pop, fitnesses):
        # ind.fitness.values = fit
        ind.fitness.values = (fit[0],)

    for g in range(NGEN):
        print(g)
        printProgressBar(g, NGEN, decimals=0, length=50)

        offspring = toolbox.select(pop)
        offspring = list(toolbox.map(toolbox.clone, offspring))
# check if apply crosover mutate etc happen in place and return is not required
        # Apply crossover on the offspring
        offspring = _apply_crossover(offspring, toolbox)
        # Apply mutation on the offspring
        offspring = _apply_mutate(offspring, toolbox)
        # Evaluate the individuals with an invalid fitness
        offspring = _compute_invalid_fitnesses(offspring, toolbox)
        # The population is entirely replaced by the offspring
        offspring.extend(tools.selBest(pop, PARENTS_TO_OFFSPRING))
        selected = tools.selBest(offspring, OFFSPRING_TO_NEXT_GEN)
        pop[:] = selected

        res = [x.fitness.values for x in tools.selBest(selected, CONVERGE_LIMIT)] # extra termination condition. if first 100 are the same break and return
        if res.count(res[0]) == len(res):
            break

        #print([x.string for x in res])
    print()
    [winner] = tools.selBest(selected, 1)
    return winner, g  


def _initialize_genetic(initial_melody, scale):   
    from musicality.constants import INITIAL_POP_SIZE, NO_OF_PARENTS, TOURNSIZE
    from musicality.genetic_helper import mutate, evaluate
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("random_melody", mutate, initial_melody)
    toolbox.register("individual", tools.initIterate, creator.Individual,
                        toolbox.random_melody)

    toolbox.register("evaluate", evaluate, scale=scale)

    toolbox.register("population", tools.initRepeat, list, toolbox.individual, INITIAL_POP_SIZE)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", mutate)
    toolbox.register("select", tools.selTournament, k=NO_OF_PARENTS, tournsize=TOURNSIZE)#, #tournsize=3)
    toolbox.register("map", map) # windows workarround. Cant use multiprocessing at the moment


    return toolbox


def _apply_crossover(offspring, toolbox):
    from random import random
    from musicality.constants import CXPB
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random() < CXPB:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values
    return offspring

def _apply_mutate(offspring, toolbox):
    from random import random
    from musicality.constants import MUTPB
    for mutant in offspring:
        if random() < MUTPB:
            toolbox.mutate(mutant)
            del mutant.fitness.values
    return offspring


def _compute_invalid_fitnesses(offspring, toolbox):
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit[0]
    return offspring


def _compute_invalid_fitnesses(offspring, toolbox):

    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
            # NOTE: ask stef why
            # ind.fitness.values = fit
        ind.fitness.values = (fit[0],)
    return offspring