from math import *
import random

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
    for i in range(number):
        samples = random.sample(population, unit)
        max_fitness = 0
        best_sample = None
        for sample in samples:
            f = fitness(problem, sample)
            if f > max_fitness:
                max_fitness = f
                best_sample = sample
        new_population.append(best_sample)
    return new_population


def elitismSelection(problem, population):
    """
    return the best fitness individual, which won't mutate and cross
    :param problem: the problem to solve
    :param population: the population for selection ,[Individuals]
    :return: the best fitness individual
    """
    best = None
    max_fitness = 0
    for individual in population:
        f = fitness(problem,individual)
        if f > max_fitness:
            max_fitness = f
            best = individual
    return best