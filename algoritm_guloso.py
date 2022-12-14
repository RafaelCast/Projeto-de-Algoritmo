import math
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
import os.path

def read_file(): 
    pathR = os.path.abspath('instance_100.txt')
    path = os.path.join(os.path.dirname(pathR),'Instances', 'instance_100.txt')
    file = open(path, "r")
    
    content = file.read()
    file.close()
    return content

def init_matrix(nLins, nCols):
    D = [None] * nLins
    for i in range(nLins):
        D[i] = [0] * nCols
        for j in range(nCols):
            D[i][j] = 0
    return D

def linearize(N, nLin, nCol):
    l = 0
    D = init_matrix(nLin, nLin)
    for i in range(nLin, 0, -1):
        for j in range(l, nLin, 1):
            aux = 0

            for k in range(0, nCol, 1):
                aux += (N[nLin-i][k]-N[j][k])**2
            
            aux = math.sqrt(aux)
            #aux= "{:.2f}".format(aux)
            D[j][l] = aux
            D[l][j] = aux
        
        l += 1 

    return D

def where_in_matrix(D, index, nCol, value):
    for j in range(nCol):
        if D[index][j] == value:
            return j
    return -1

def where_in_aux(aux, index, nCol, value):
    for j in range(nCol):
        if aux[index][j] == value:
            return j
    return -1

def bigger_side(D, n, l):
    max = 0
    for i in range(len(D[0])):
        if D[n][i] > max and i != l:
            max = D[n][i]
            side = n
    for i in range(len(D[0])):
        if D[l][i] > max and i != n:
            max = D[l][i]
            side = l

    return side
    

def greedy(D, m):
    max_div = [0,0]
    array = [-1 for i in range(m)]
    n = l = 0
    sum = 0
    i = 0
    for j in range(len(D)):
        for k in range(len(D)):
            if D[j][k] > sum:
                sum = D[j][k]
                n = j
                l = k
    i = 2
    aux = [0 for j in range(m)]
    bigger = bigger_side(D, n, l)
    if(bigger == n):
        array[0] = l
        array[1] = n
        aux[0] = D[l].copy()
        aux[1] = D[n].copy()
    else:
        array[0] = n
        array[1] = l
        aux[0] = D[n].copy()
        aux[1] = D[l].copy()

    aux[0].sort(reverse = True)
    aux[1].sort(reverse = True)
    aux[0][0] = -1
    aux[1][0] = -1
    aux[0].sort(reverse = True)
    aux[1].sort(reverse = True)

        
    j = 0
    while i < m:
        j = aux[i-1][0]
        l = where_in_matrix(D, array[i-1], len(D), j)
        if l in array:
            l = where_in_matrix(D, array[i-1], len(D), j)
        aux[i-1][0] = -1
        aux[i-1].sort(reverse = True)
        if l not in array:
            array[i] = l
            aux[i] = D[l].copy()
            sum += j 
            aux[i].sort(reverse = True)

            l = where_in_aux(aux, i, len(aux[0]), j)

            aux[i][l] = -1
            aux[i].sort(reverse = True)
            i += 1
        else:
            aux[i-1][0] = -1
            aux[i-1].sort(reverse = True)
        j = 0
    max_div[0] = array.copy()
    max_div[1] = sum
    return max_div

def get_sum(D, array):
    sum = 0
    for i in range(0, len(array)-1, 1):
        sum += D[array[i]][array[i+1]]
    return sum

def sum_one(D, array, first):
    firstP = 0
    k = 0
    for i in range(len(array)):
        if array[i] == len(D)-1 and firstP == 0 and i != 0:
            k = i
            array[i] = 0
            firstP = 1

        elif array[i] == len(D)-1 and i != 0:
            array[i] = 0
    
    k -= 1
    if k >= 0:
        if k == 0 and array[k] == len(D)-1:
            array[k] = len(D)
            return array
        #if array[k] + 1 != len(D):
        #    array[k] += 1
        else:
            #array[k] = 0
            if k != 0 and first[k] != 1:
                array[k] += 1
                array = sum_one(D, array, first)
            elif k != 0 and first[k] == 1:
                array[k] = 0
                first[k] = 0
                array = sum_one(D, array, first)
        return array

    return array

def PDM(D, N):
    max_div = [None for i in range(4)]
    i = 0
    sum = list()
    for m in range(int(0.1*len(N)), int(0.5*len(N)), int(0.1*len(N))):
        max_div[i] = greedy(D,m)
        i += 1

    return max_div
    
'''
content = read_file()
N = eval(content)
m = 10
D = linearize(N, len(N), len(N[0]))
pdm = greedy(D, m)
print(pdm)
pdm = PDM(D, N)
for i in range(len(pdm)):
    print(pdm[i])
'''