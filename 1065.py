pares = 0
for i in range(5):
    entrada = float(input())
    if entrada %2 == 0:
        pares+=1
print("%d valores pares" %(pares))