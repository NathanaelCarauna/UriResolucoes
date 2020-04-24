continuar = 1
grenais = 0
interVitorias = 0
gremioVitorias = 0
empates =0

while continuar ==1:
    grenais +=1
    golsInter, golsGremio = map(int,input().split())

    if golsInter>golsGremio:
        interVitorias+=1
    elif(golsInter==golsGremio):
        empates+=1
    else:
        gremioVitorias+=1
    
    new = -1

    while new!= 1 and new!=2:
        new = int(input("Novo grenal (1-sim 2-nao)\n"))
        if new == 1:
            pass
        elif new == 2:
            continuar = 2

print("%d grenais" %(grenais))
print("Inter:%d" %(interVitorias))
print("Gremio:%d" %(gremioVitorias))
print("Empates:%d" %(empates))
if interVitorias>gremioVitorias:
    print("Inter venceu mais")
elif interVitorias == gremioVitorias:
    print("Nao houve vencedor")
else:
    print("Gremio venceu mais")