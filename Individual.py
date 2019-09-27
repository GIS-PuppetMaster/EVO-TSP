import random


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