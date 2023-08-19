INSTRUMENT_RANGE = (40, 80)
HAS_SUBTONIC_REWARD = 4
IN_SCALE_REWARD_FACTOR = 2/3
SEMITONE_EXTENSION_REWARD_FACTOR = 10
LARGE_INTERVAL_SCORE_FACTOR = 1

NOTE_MUTATION_RATE = 0.3
RANDOM_MELODY_MUTATION_RATE = 0.2
# Scale patterns


# GENETIC ALGORITHM CONSTANTS
# Number of parents to select for crossover
NO_OF_PARENTS = 2
# Tournament size for selection
TOURNSIZE = 3
# Initial population size
INITIAL_POP_SIZE = 10000
# Number of generations
NGEN = 100
# Crossover probability
CXPB = 0.5
# Mutation probability
MUTPB = 0.2
# Number of parents to select for next generation
PARENTS_TO_OFFSPRING = INITIAL_POP_SIZE // 3
# Number of offspring to select for next generation
OFFSPRING_TO_NEXT_GEN = INITIAL_POP_SIZE
# Extra stop condition: When the first {{ CONVERGE_LIMIT }} individuals in the population are the same, the algorithm stops
CONVERGE_LIMIT = 100

SCALES = {
'MAJOR_SCALE': [0, 2, 4, 5, 7, 9, 11],
'MINOR_SCALE': [0, 2, 3, 5, 7, 8, 10],
'HARMONIC_MINOR_SCALE': [0, 2, 3, 5, 7, 8, 11]
}