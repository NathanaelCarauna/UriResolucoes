nEntradas = int(input())

for i in range(nEntradas):
    x,y = map(int, input().split())
    soma = 0
    if x%2 == 0:
            x +=1
    for n in range(y):        
        soma += x
        x+=2
    print(soma)
