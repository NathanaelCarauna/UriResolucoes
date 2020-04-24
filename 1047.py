horaInicial, minInicial, horaFinal, minFinal = map(int,input().split())
resposta = "O JOGO DUROU {} HORA(S) E {} MINUTO(S)"

tempoFinal = (horaFinal*60+minFinal)
tempoInicial = ( horaInicial*60 + minInicial)


if tempoFinal < tempoInicial:
    tempoFinal += (24*60)
    horas = (tempoFinal - tempoInicial)//60
    minutos = (tempoFinal - tempoInicial)%60
elif tempoFinal > tempoInicial:
    
    if tempoFinal- tempoInicial < 60:
        horas = 0
        minutos = tempoFinal - tempoInicial
    else:
        horas = (tempoFinal - tempoInicial)//60
        minutos = (tempoFinal - tempoInicial)%60
elif tempoFinal == tempoInicial:
    horas = 24
    minutos = 0

print(resposta.format(horas,minutos))