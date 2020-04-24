x = int(input())
z = x
numeros =  0
soma = 0
while z<=x:
    z = int(input())
for i in range(x,100000):
    soma +=i
    numeros+=1
    if soma >z:
        break
print(numeros)

