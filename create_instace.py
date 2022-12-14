import os.path

def create_random_matriz(nLins, nCols):
    from random import randint
    vals = [None] * nLins
    for i in range(nLins):
        vals[i] = [0] * nCols
        for j in range(nCols):
            vals[i][j] = randint(0, 10)
    return vals

nCols = 10
nLins = 200
matriz = create_random_matriz(nLins, nCols)
pathR = os.path.abspath('instance-100.txt')
path = os.path.join(os.path.dirname(pathR),'Instances', 'instance_200.txt')
file = open(path, "w+")

content = str(matriz)
file.write(content)
file.close()
