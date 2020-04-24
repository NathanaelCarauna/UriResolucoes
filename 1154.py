media = 0
soma = 0
n = 0
while True:
    idade = int(input())
    if idade<0:
        break
    soma +=idade
    n+=1
media = soma/n

print("%.2f" %(media))