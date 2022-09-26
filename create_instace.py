def create_random_matriz(nLins, nCols):
    from random import randint
    vals = [None] * nLins
    for i in range(nLins):
        vals[i] = [0] * nCols
        for j in range(nCols):
            vals[i][j] = randint(0, 10)
    return vals

nLins = 20
nCols = 10
matriz = create_random_matriz(nLins, nCols)
file = open("/home/rafael/alg/instances/instance-200.txt", "w+")

content = str(matriz)
file.write(content)
file.close()
