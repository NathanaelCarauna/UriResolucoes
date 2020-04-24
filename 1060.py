resposta = "%d valores positivos"
inteiros = 0

for x in range(6):
    entrada = float(input())
    if entrada >0:
        inteiros += 1


print(resposta %(inteiros))
