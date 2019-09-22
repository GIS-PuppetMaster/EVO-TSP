import os
import tsplib95 as ts
import random


class TSPProblem:
    def __init__(self, problem):
        # parse .TSP file
        self.problem = ts.parser.parse("data/" + problem + ".tsp")
        # create solution
        self.solution = []


class Individual:
    def __init__(self, problem):
        self.problem = problem

    def generate_random_solution(self):
        """
        O(n) generate_random_solution and assign it to self.problem.solution
        :return: None
        """
        len = dict(self.problem.problem.get("NODE_COORD_SECTION")).__len__()
        a = [i + 1 for i in range(len)]
        for i in range(len):
            index = random.randint(0, len - 1)
            self.problem.solution.append(a[index])
            a[index] = a[len - 1]
            len -= 1
        # back to start point
        self.problem.solution.append(self.problem.solution[0])


p = TSPProblem("eil101")
s = Individual(p)
s.generate_random_solution()
print(str(p.solution))
