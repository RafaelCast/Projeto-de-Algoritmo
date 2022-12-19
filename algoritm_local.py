from algoritm_guloso import *


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


def cut_bad_branches(D, array, first):
    j = 0

    while j < len(array):
        aux = array[j]

        for i in range(j+1, len(array), 1):
            if aux == array[i] and i != j:
                if array[i]+1 < len(array):
                    array[i] = array[i] + 1
                else:
                    aux = sum_one(D, array, first)
                    if array[0] == 100:
                        return array
        j += 1
    return array



def local_search(D, array, m):
    first = [1 for i in range(len(array))] 
    first[len(array)-1] = 0
    aux = array.copy()
    sum = get_sum(D, array)
    sumAux = 0
    i = m-1
    l = j = 0
    aux[i] = 0
    maior = array.copy()
    while l != m-1:
        print(aux)
        aux[i-l] = j
        j += 1
        sumAux = get_sum(D, aux)
        if j == len(D):
            j = 0

        if sumAux > sum:
            sum = sumAux
            maior = aux.copy()


        if aux[i-l] == len(D)-1:
            aux[i-l] = 0
            j = 0
            l += 1

            while aux[i-l] == len(D)-1 and l < m-1:
                aux[i-l] = 0
                l += 1
                sumAux = get_sum(D, aux)
                aux = cut_bad_branches(D, aux, first)
                if aux[0] == len(D):
                    return maior
                if sumAux > sum:
                    sum = sumAux
                    maior = aux.copy()
                        

            if l == m-1 and aux[i-l] == len(D)-1:
                return maior



            if aux[i-l] == array[i-l] and first[i-l] == 1:
                aux[i-l] = 0
                aux = cut_bad_branches(D, aux, first)
                sumAux = get_sum(D, aux)
                if aux[0] == len(D):
                    return maior
                if sumAux > sum:
                    sum = sumAux
                    maior = aux.copy()
                first[i-l] = 0

            
            else:
                aux[i-l] += 1
                sumAux = get_sum(D, aux)
                aux = cut_bad_branches(D, aux, first)
                if aux[0] == len(D):
                    return maior
                if sumAux > sum:
                    sum = sumAux
                    maior = aux.copy()

            l = 0
            j = 0
                

    return maior

