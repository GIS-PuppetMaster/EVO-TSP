from GA1 import *
from GA2 import *
from GA3 import *

POPULATION_LIST = [10, 20, 50, 100]
p_list = ['eil51', 'eil76', 'eil101', 'kroA100']
a_list = [1, 2, 3]
for problem in p_list:
    for a in a_list:
        for population in POPULATION_LIST:
            if a == 1:
                ga1(problem, population)
            elif a == 2:
                ga2(problem, population)
            elif a == 3:
                ga3(problem, population)
