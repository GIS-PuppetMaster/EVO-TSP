import os
import tsplib95 as ts
import random
import numpy as np


class TSPProblem:
    def __init__(self, problem):
        # parse .TSP file
        self.problem = ts.parser.parse("data/" + problem + ".tsp")


class Individual:
    def __init__(self, problem):
        self.problem = problem
        # create solution
        self.solution = []
        self.generate_random_solution()

    def generate_random_solution(self):
        """
        O(n) generate_random_solution and assign it to self.problem.solution
        :return: None
        """
        len = dict(self.problem.problem.get("NODE_COORD_SECTION")).__len__()
        a = [i + 1 for i in range(len)]
        for i in range(len):
            index = random.randint(0, len - 1)
            self.solution.append(a[index])
            a[index] = a[len - 1]
            len -= 1
        # not contain path back to start point
        # self.solution.append(self.solution[0])


def random_select_gene_sequence(solution):
    """
    random_select_gene_sequence
    :param solution: individual
    :return: individual after operation
    """
    start = random.randint(0, len(solution) - 1)
    end = random.randint(0, len(solution) - 1)
    # make sure start <= end
    if start > end:
        temp = start
        start = end
        end = temp
    return start, end


def insert(individual):
    """
    random select a gene and change it's position
    :param individual: a possible solution
    """
    # random select gene to insert
    solution = individual.solution
    op = random.randint(0, len(solution) - 1)
    gene = solution.pop(solution[op])
    # random select position to insert
    target = random.randint(0, len(solution) - 2)
    solution.insert(target, gene)
    individual.solution = solution


def swap(individual):
    """
    random swap 2 genes in solution
    :param individual: a possible solution
    """
    solution = individual.solution
    op1 = random.randint(0, len(solution) - 1)
    op2 = random.randint(0, len(solution) - 1)
    temp = solution[op2]
    solution[op2] = solution[op1]
    solution[op1] = temp
    individual.solution = solution


def swap(individual, op1, op2):
    """
    swap 2 genes in solution
    :param individual: a possible solution
    :param op1: target to swap
    :param op2: target to swap
    """
    solution = individual.solution
    if op1 != op2:
        temp = solution[op2]
        solution[op2] = solution[op1]
        solution[op1] = temp
    individual.solution = solution


def inversion(individual):
    """
    random select a sequence of gene and reverse it
    :param individual: a possible solution
    """
    solution = individual.solution
    start, end = random_select_gene_sequence(solution)
    # reverse
    i = start
    j = end
    while i < j:
        swap(solution, i, j)
        i += 1
        j -= 1
    individual.solution = solution


def scramble(individual):
    solution = individual.solution
    start, end = random_select_gene_sequence(solution)
    temp = np.array(solution[start:end + 1])
    np.random.shuffle(temp)
    i = start
    j = 0
    while i <= end:
        solution[i] = temp[j]
        j += 1
        i += 1
    individual.solution = solution


def orderCrossoverTool(parent1, parent2):
    # do OC to parent1
    # random select a sequence of gene in parent1
    solution1 = parent1.solution
    solution2 = parent2.solution
    start, end = random_select_gene_sequence(solution1)
    child = solution1[start:end + 1]
    index = 0
    for g in solution2:
        if index == start:
            index = end + 1
        if g not in child:
            child.insert(index, g)
            index += 1
    parent1.solution = child


def orderCrossover(parent1, parent2):
    p1 = parent1
    orderCrossoverTool(parent1, parent2)
    orderCrossoverTool(parent2, p1)


def search_map(map, start):
    # search map to solve conflict
    while start in map.keys():
        start = map[start]
    return start


def PMXCrossover(parent1, parent2):
    solution1 = parent1.solution
    solution2 = parent2.solution
    start, end = random_select_gene_sequence(solution1)
    # swap gene sequence
    i = start
    while i <= end:
        temp = solution1[i]
        solution1[i] = solution2[i]
        solution2[i] = temp
        i += 1
    # conflict detect
    child1 = solution1[start:end + 1]
    child2 = solution2[start:end + 1]
    # build map
    map = {}
    i = 0
    while i < len(child1):
        map[child1[i]] = child2[i]
        i += 1
    # detect and solve conflict
    for i in range(len(solution1)):
        # detected conflict
        if i < start or i > end:
            gene1 = solution1[i]
            gene2 = solution2[i]
            if gene1 in child1:
                solution1[i] = search_map(map, gene1)
            if gene2 in child2:
                solution2[i] = search_map(map, gene2)
    parent1.solution = solution1
    parent2.solution = solution2


def cycleCrossoverTool(parent1, parent2):
    # random select a start position
    solution1 = parent1.solution
    solution2 = parent2.solution
    index = random.randint(0, len(solution1) - 1)
    gene_list = []
    start = solution1[index]
    temp = solution2[index]
    index = solution1.index(temp)
    gene_list.append(start)
    end = -1
    while start != end:
        end = solution1[index]
        temp = solution2[index]
        index = solution1.index(temp)
        gene_list.append(end)
    child = []
    for i in range(len(solution1)):
        if solution1[i] in gene_list:
            child.append(solution1[i])
        else:
            child.append(None)

    for i in range(len(solution2)):
        if child[i] is None:
            child[i] = solution2[i]
    parent1.solution = child




def cycleCrossover(parent1, parent2):
    pa1 = parent1
    cycleCrossoverTool(parent1, parent2)
    cycleCrossoverTool(parent2, pa1)


def edgeRecombination(parent1,parent2):
    pass


p = TSPProblem("st70")
s1 = Individual(p)
s2 = Individual(p)
print(str(s1.solution))
print(str(s2.solution))
# cycleCrossover(s1,s2)
# PMXCrossover(s1,s2)
# orderCrossover(s1,s2)
# test
t = [0 for i in range(len(s1.solution))]
for gene in s1.solution:
    t[gene-1] += 1
print(t)

print(str(s1.solution))
