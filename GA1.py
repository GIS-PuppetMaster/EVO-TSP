# coding=utf-8
"""
tournamentSelection
PMXCrossover
swap mutation
"""
from TSPProblem import TSPProblem
from Individual import Individual
from Selection import *
from Crossover import *
from Mutation import *



# 要解决的问题名称
PROBLEM_NAME = 'pcb442'
# 种群大小
POPULATION_SIZE = 20
# 锦标赛选择中随机采样进行比赛的个体数目
UNIT = 2
# 交叉概率和变异概率
# the probability of crossover and mutation
CROSSOVER_PRO = 0.9
MUTATION_PRO = 0.5
# 总迭代进化次数
# generation of evolution
GENERATION = 100



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
    # calculate fitness
    if g != 0 and g % (GENERATION / 10) == 0:
        min_fitness = 1e20
        for i in population:
            f = fitness(problem, i)
            min_fitness = f if f < min_fitness else min_fitness
        best_fitness.append("   第{0}次最优适应度：{1}\n".format(g, min_fitness))

# get result
total_fitness = []
for i in population:
    total_fitness.append(fitness(problem, i))
total_fitness = np.array(total_fitness)
mean = np.mean(total_fitness)
var = np.var(total_fitness)
std = np.std(total_fitness)

res = "Problem:{0}\nPopulation Size:{1}\nAlgorithm{2}\n".format(PROBLEM_NAME, POPULATION_SIZE, "GA1")
res += "随机初始化的个体适应度平均值：" + str(raw_mean) + "\n"
res += "随机初始化的个体适应度方差：" + str(raw_var) + "\n"
res += "随机初始化的个体适应度标准差: " + str(raw_std) + "\n"
res += "最终种群适应度平均值：" + str(mean) + "\n"
res += "最终适应度方差：" + str(var) + "\n"
res += "最终适应度标准差: " + str(std) + "\n"
res += "训练历史\n"
for i in best_fitness:
    res += i

res += "\n \n \n"
with open("Experiment1.txt", "a") as f:
    f.write(res)


