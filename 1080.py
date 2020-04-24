x = 0
for i in range(1,101):
    n = int(input())
    if n>x:
        x = n
        posicao = i
print(x)
print(posicao)