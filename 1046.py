hI, hF = map(int,input().split())
resposta = "O JOGO DUROU %d HORA(S)"

if hI > hF:
    hF +=24
    horas = hF - hI
elif hF >  hI:
    horas = hF - hI
else:
    horas = 24
print(resposta %(horas))