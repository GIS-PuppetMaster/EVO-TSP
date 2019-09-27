from math import *
import random
import copy

def fitnessproportional():
    # TODO
    pass


def fitness(problem, individual):
    """
    calculate fitness
    :param problem: problem graph
    :param individuals: an individual
    :return: fitness
    """
    graph = problem.getGraph()
    last_city = None
    dis = 0
    for city in individual.solution:
        if last_city is not None:
            cor1 = graph[city]
            cor2 = graph[last_city]
            dis += sqrt(pow((cor1[0] - cor2[0]), 2) + pow((cor1[1] - cor2[1]), 2))
        last_city = city
    # calculate go back distance
    cor1 = graph[last_city]
    cor2 = graph[individual.solution[0]]
    dis += sqrt(pow((cor1[0] - cor2[0]), 2) + pow((cor1[1] - cor2[1]), 2))
    return dis


def tournamentSelection(problem, population, unit, number):
    """
    :param problem: the problem to solve
    :param population: the population for selection ,[Individuals]
    :param unit: how many individuals to sample at once
    :param number: how many individuals to return
    :return: new population
    """
    new_population = []
    i = 1
    while i < number:
        samples = random.sample(population, unit)
        min_fitness = 1e20
        best_sample = None
        for sample in samples:
            f = fitness(problem, sample)
            if f < min_fitness:
                min_fitness = f
                best_sample = sample
        if best_sample not in new_population:
            new_population.append(best_sample)
        else:
            # prevent repeat reference
            new_population.append(copy.deepcopy(best_sample))
        i += 1
    return new_population


def elitismSelection(problem, population):
    """
    return the best fitness individual, which won't mutate and cross
    :param problem: the problem to solve
    :param population: the population for selection ,[Individuals]
    :return: the best fitness individual
    """
    best = None
    min_fitness = 1e20
    for individual in population:
        f = fitness(problem, individual)
        if f <= min_fitness:
            min_fitness = f
            best = individual
    return best