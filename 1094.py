t = int(input())
total = 0
totalCoelhos = 0
totalSapos = 0
totalRatos = 0

for i in range(t):
    qtd, cobaia = input().split()
    qtd = int(qtd)
    if cobaia == "C":
        totalCoelhos += qtd
    elif cobaia == "S":
        totalSapos += qtd
    elif cobaia == "R":
        totalRatos += qtd
    total += qtd

print("Total: %d cobaias" %(total))
print("Total de coelhos: %d" %(totalCoelhos))
print("Total de ratos: %d" %(totalRatos))
print("Total de sapos: %d"  %(totalSapos))
print("Percentual de coelhos: %.2f %%" %((totalCoelhos/total)*100))
print("Percentual de ratos: %.2f %%" %((totalRatos/total)*100))
print("Percentual de sapos: %.2f %%" %((totalSapos/total)*100))