import tsplib95 as ts


class TSPProblem:
    def __init__(self, problem):
        # parse .TSP file
        self.problem = ts.parser.parse("data/" + problem + ".tsp")
        self.city_num = len(dict(self.problem.get("NODE_COORD_SECTION")))

    def getGraph(self):
        return dict(self.problem.get("NODE_COORD_SECTION"))
