from Mutation import random_select_gene_sequence
import random
import copy


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
    if parent1 == parent2:
        return
    solution1 = copy.deepcopy(parent1.solution)
    solution2 = copy.deepcopy(parent2.solution)
    start, end = random_select_gene_sequence(solution1)
    # swap gene sequence
    index = start
    while index <= end:
        temp = solution1[index]
        solution1[index] = solution2[index]
        solution2[index] = temp
        index += 1
    # conflict detect
    child1 = solution1[start:end + 1]
    child2 = solution2[start:end + 1]
    # build map
    map = {}
    index = 0
    while index < len(child1):
        map[child1[index]] = child2[index]
        index += 1
    # detect and solve conflict
    for i in range(len(solution1)):
        # detected conflict
        if i < start or i > end:
            gene1 = solution1[i]
            if gene1 in child1:
                solution1[i] = search_map(map, gene1)
    map = {}
    index = 0
    while index < len(child2):
        map[child2[index]] = child1[index]
        index += 1
    for i in range(len(solution2)):
        # detected conflict
        if i < start or i > end:
            gene2 = solution2[i]
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


def edgeRecombination(parent1, parent2):
    # do edgeRecombination between parent1 and parent2
    solution1 = parent1.solution
    solution2 = parent2.solution
    neighbour = []
    child = []
    # get the neighbour list
    for i in range(len(parent1)):
        neighbour[i] = getneighbour(solution1, solution2, i)
    # random select a parent and let the child start with that parent's first gene
    n = random.randint(0, 1)
    if n == 0:
        child[0] = solution1[0]
    else:
        child[0] = solution2[0]
    i = 0
    # interate and get the child
    while len(child) != len(child):
        child[i + 1] = neighbour[child[i]][random.randint(1, len(neighbour[child[i]])) - 1]
        neighbour = removeneighbour(neighbour, child[i + 1])
        i += 1
    parent1.solution = child


def removeneighbour(neighbour, number):
    # remove all the same gene in the list neighbour
    length = len(neighbour)
    for i in range(0, length - 1):
        # remove neighbour[number]
        if i == number:
            neighbour[i] = []
        # remcve the number in the other neighbour
        else:
            neighbour[i].remove()
    return neighbour


def getneighbour(solution1, solution2, number):
    # find the neighbour of a order number
    neighbour = []
    # find gene's index
    index = solution1.index(number)
    if index == 0:
        neighbour.append(solution1[1])
        neighbour.append(solution1[len(solution1)])
    elif index == len(solution1):
        neighbour.append(solution1[0])
        neighbour.append(solution1[index - 1])
    else:
        neighbour.append(solution1[index + 1])
        neighbour.append(solution1[index - 1])
    # find gene's index
    index = solution2.index(number)
    if index == 0:
        a1 = solution2[1]
        a2 = solution2[len(solution2)]
    elif index == len(solution1):
        a1 = solution2[0]
        a2 = solution2[index - 1]
    else:
        a1 = solution2[index + 1]
        a2 = solution2[index - 1]
    # remove the repeated neighbour
    if a1 not in neighbour:
        neighbour.append(a1)
    if a2 not in neighbour:
        neighbour.append(a2)
    return neighbour
