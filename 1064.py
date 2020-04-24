inteiros = soma = 0
for i in range(6):
    entrada = float(input())
    if entrada > 0:
        soma += entrada
        inteiros +=1
        

media = soma/ inteiros
print("%d valores positivos" %(inteiros))
print("%.1f" %(media))