"""
tournamentSelection
PMXCrossover
"""
from TSPProblem import TSPProblem
from Individual import Individual
from Selection import *
from Crossover import *
from Mutation import *



PROBLEM_NAME = 'st70'
POPULATION_SIZE = 20
UNIT = 2
# the probability of crossover and mutation
CROSSOVER_PRO = 0.6
MUTATION_PRO = 0.1
# generation of evolution
GENERATION = 20



# init problem
problem = TSPProblem(PROBLEM_NAME)
# init population
population = []
for i in range(POPULATION_SIZE):
    population.append(Individual(problem))
for g in range(GENERATION):
    print("第{0}次".format(g))
    # calculate fitness and select
    population = tournamentSelection(problem, population, UNIT, POPULATION_SIZE)
    # crossover
    random.shuffle(population)
    i = 0
    while i < len(population)-1:
        r = random.uniform(1, 10)
        if r < CROSSOVER_PRO * 10:
            parent1 = population[i]
            parent2 = population[i + 1]
            PMXCrossover(parent1, parent2)
        i += 2
    # mutation
    for individual in population:
        r = random.uniform(1, 10)
        if r < MUTATION_PRO * 10:
            swap(individual)

# get result
total_fitness = []
for i in population:
    total_fitness.append(fitness(problem, i))
total_fitness = np.array(total_fitness)
mean = np.mean(total_fitness)
var = np.var(total_fitness)
std = np.std(total_fitness)
print("平均值："+str(mean))
print("方差："+str(var))
print("标准差: "+str(std))

