valor = int(input())
valorO= valor
n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0
if valor >= 100:
    n100 = valor//100
    valor = valor % 100
if valor >= 50:
    n50 = valor//50
    valor = valor % 50
if valor >= 20:
    n20 = valor//20
    valor = valor % 20
if valor >= 10:
    n10 = valor//10
    valor = valor % 10
if valor >= 5:
    n5 = valor//5
    valor = valor % 5
if valor >= 2:
    n2 = valor//2
    valor = valor % 2
if valor >= 1:
    n1 = valor//1
    valor = valor % 1
print(valorO)
print("%d nota(s) de R$ 100,00" % (n100))
print("%d nota(s) de R$ 50,00" % (n50))
print("%d nota(s) de R$ 20,00" % (n20))
print("%d nota(s) de R$ 10,00" % (n10))
print("%d nota(s) de R$ 5,00" % (n5))
print("%d nota(s) de R$ 2,00" % (n2))
print("%d nota(s) de R$ 1,00\n" % (n1))
