from algoritm_guloso import *
from algoritm_local import *
from random import random, randint

def random_neighbor(D, S, m):
    S = S.copy()
    i = randint(0, m-1)
    j = randint(0, len(D)-1)
    if not j in S:
        S[i] = j
    else:
        S = random_neighbor(D, S, m)

    return S

def annealing(D, greedy, m):
    T0 = 10000
    T = T0
    alpha = 0.999
    Smax = 1000
    S = greedy.copy()
    i=0
    Sexit = S.copy()
    '''while T > 0.1:
        i += 1
        T = alpha*T
'''

    Sbest = greedy.copy()
    while T > 0.1:
        for i in range(Smax):
            S = random_neighbor(D, S, m)
            sum1 = get_sum(D, S)
            sum2 = get_sum(D, Sbest)
            if get_sum(D, S) > get_sum(D, Sbest):
                Sexit = S.copy()
                Sbest = S.copy()
            elif random() < math.exp((get_sum(D, S) - get_sum(D, Sbest))/T):
                Sexit = S.copy()

        T = alpha*T
        print('-----------------')
        print(T)
        print(math.exp((get_sum(D, S) - get_sum(D, Sbest))/T))
    return Sexit


def register_file(content1, content2):
    pathR = os.path.abspath('instance-100.txt')
    path = os.path.join(os.path.dirname(pathR), 'result.txt')
    file = open(path, "w+")
    file.write(content1)
    file.write(content2)
    file.close()

def read_result(): 
    pathR = os.path.abspath('instance_100.txt')
    path = os.path.join(os.path.dirname(pathR), 'result.txt')
    file = open(path, "r")
    
    content = file.read()
    file.close()
    return content


content = read_file()
N = eval(content)
m = 10
D = linearize(N, len(N), len(N[0]))
greedy = greedy(D, m)
S = annealing(D, eval(read_result()), m)
print("Guloso:", greedy[0])
print("Soma:", greedy[1])
print("Annealing:", S)
print("Soma:", get_sum(D, S))
register_file(str(S), str(get_sum(D, S)))