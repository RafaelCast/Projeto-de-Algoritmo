def create_random_list():
    import random
    return [random.randint(0, 9) for i in range(100)]

def create_instance():
    j = []
    for i in range(4):
        j += create_random_list()
    return j
        
j = create_instance()
print(j)