# coding=utf-8
"""
elitismSelection
cycleCrossover
insert mutation
"""
import Config
from TSPProblem import TSPProblem
from Individual import Individual
from Selection import *
from Crossover import *
from Mutation import *


def ga3(problem_name, population_size, generation=20000, path="Experiment1.txt"):
    # 要解决的问题名称
    PROBLEM_NAME = problem_name
    # 种群大小
    POPULATION_SIZE = population_size
    # 锦标赛选择中随机采样进行比赛的个体数目
    UNIT = Config.UNIT
    # 交叉概率和变异概率
    # the probability of crossover and mutation
    CROSSOVER_PRO = Config.CROSSOVER_PRO
    MUTATION_PRO = Config.MUTATION_PRO
    # 总迭代进化次数
    # generation of evolution
    GENERATION = generation

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
        print("问题:{0},算法:GA3,种群大小:{1},第{2}次".format(PROBLEM_NAME, POPULATION_SIZE, g))
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
        for i in range(len(population)):
            individual = population[i]
            f = fitness(problem, individual)
            if f > max_fitness:
                max_fitness = f
                worst_index = i
        population[worst_index] = best_individual
        # calculate fitness
        if g == 5000 - 1 or g == 10000 - 1 or g == 20000 - 1:
            min_fitness = 1e20
            for i in population:
                f = fitness(problem, i)
                min_fitness = f if f < min_fitness else min_fitness
            best_fitness.append("   第{0}次最优适应度：{1}\n".format(g + 1, min_fitness))

    # get result
    total_fitness = []
    for i in population:
        total_fitness.append(fitness(problem, i))
    total_fitness = np.array(total_fitness)
    mean = np.mean(total_fitness)
    var = np.var(total_fitness)
    std = np.std(total_fitness)

    res = "Problem:{0}\nPopulation Size:{1}\nAlgorithm:{2}\n".format(PROBLEM_NAME, POPULATION_SIZE, "GA3")
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

    with open(path, "a") as f:
        f.write(res)
