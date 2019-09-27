"""
elitismSelection
cycleCrossover
insert mutation
"""
from TSPProblem import TSPProblem
from Individual import Individual
from Selection import *
from Crossover import *
from Mutation import *

# 要解决的问题名称
PROBLEM_NAME = 'pcb442'
# 种群大小
POPULATION_SIZE = 100
# 锦标赛选择中随机采样进行比赛的个体数目
UNIT = 2
# 交叉概率和变异概率
# the probability of crossover and mutation
CROSSOVER_PRO = 0.9
MUTATION_PRO = 0.5
# 总迭代进化次数
# generation of evolution
GENERATION = 500

# init problem
problem = TSPProblem(PROBLEM_NAME)
# init population
population = []
for i in range(POPULATION_SIZE):
    population.append(Individual(problem))

raw_fitness = []
for i in population:
    raw_fitness.append(fitness(problem, i))
raw_fitness = np.array(raw_fitness)
raw_mean = np.mean(raw_fitness)
raw_var = np.var(raw_fitness)
raw_std = np.std(raw_fitness)
best_fitness = []

for g in range(GENERATION):
    print("第{0}次".format(g))
    # calculate fitness and select
    best_individual = elitismSelection(problem, population)
    # crossover
    random.shuffle(population)
    i = 0
    while i < len(population) - 1:
        r = random.uniform(1, 10)
        if r < CROSSOVER_PRO * 10:
            parent1 = population[i]
            parent2 = population[i + 1]
            cycleCrossover(parent1, parent2)
        i += 2
    # mutation
    for individual in population:
        r = random.uniform(1, 10)
        if r < MUTATION_PRO * 10:
            insert(individual)
    # replace the worst with best
    max_fitness = 0
    worst_index = 0
    for i in population:
        f = fitness(problem, i)
        if f > max_fitness:
            max_fitness = f
            worst_index = i
    population[worst_index] = best_individual
    # calculate fitness
    if g != 0 and g % (GENERATION / 10) == 0:
        min_fitness = 1e20
        for i in population:
            f = fitness(problem, i)
            min_fitness = f if f < min_fitness else min_fitness
        best_fitness.append("第{0}次最优适应度：{1}".format(g, min_fitness))

# get result
total_fitness = []
for i in population:
    total_fitness.append(fitness(problem, i))
total_fitness = np.array(total_fitness)
mean = np.mean(total_fitness)
var = np.var(total_fitness)
std = np.std(total_fitness)
print("随机初始化的个体适应度平均值：" + str(raw_mean))
print("随机初始化的个体适应度方差：" + str(raw_var))
print("随机初始化的个体适应度标准差: " + str(raw_std))
print("最终种群适应度平均值：" + str(mean))
print("最终适应度方差：" + str(var))
print("最终适应度标准差: " + str(std))

print("训练历史")
for i in best_fitness:
    print(i)
