import random
import numpy as np


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
    individual is mutable
    random swap 2 genes in solution
    :param individual: a possible solution
    """
    solution = individual.solution
    op1 = random.randint(0, len(solution) - 1)
    op2 = random.randint(0, len(solution) - 1)
    swapTool(individual, op1, op2)


def swapTool(individual, op1, op2):
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
        swapTool(solution, i, j)
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
