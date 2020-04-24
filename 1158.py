nEntradas = int(input())
soma = 0
for i in range(nEntradas):
    x,y = map(int, input().split())
    for j in range(x,y):
        if j %2 != 0:
            soma+=j
    print(soma)

