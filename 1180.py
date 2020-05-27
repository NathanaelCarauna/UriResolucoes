n = int(input())
x = list(map(int,input().split()))
menorValor = 10000
posicao = 0
for i in range(n):
    if x[i] < menorValor:
        menorValor = x[i]
        posicao = i
print("Menor valor: %d" %menorValor)
print("Posicao: %d" %posicao)