




matriz = create_random_matriz()
file = open("myfile.txt", "w+")
  
content = str(matriz)
file.write(content)
file.close()
print(matriz)
