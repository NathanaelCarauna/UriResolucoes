entrada = list(map(int, input().split()))
a = entrada[0]
soma = 0
for i in entrada[1:]:
    if i >0:
        n = i
        break
for i in range(n):
    soma+= a+i
print(soma)
