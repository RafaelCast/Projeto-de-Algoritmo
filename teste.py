from random import random, randint
from algoritm_guloso import *
from algoritm_local import *
from algoritm_meta import *



N = [[4,10,1,4,1], [3,0,9,7,2], [1,0,5,6,2], [7,10,4,1,3]]
D = linearize(N, len(N), len(N[0]))
m = 3
greedy = greedy(D, m)
a = local_search(D, greedy[0], m)
b = annealing(D, greedy[0], m)
print(b)
