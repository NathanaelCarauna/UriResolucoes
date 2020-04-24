dias = minutos = segundos = 0
diaInicio = input()
diaInicio = diaInicio.split(" ")
diaInicio = int(diaInicio[1])

horaI, minutoI, segundoI = map(int, input().split(":"))

diaFinal = input()
diaFinal = diaFinal.split(" ")
diaFinal = int(diaFinal[1])

horaF, minutoF, segundoF = map(int, input().split(":"))

horaI *= 3600
minutoI *= 60
horaF *= 3600
minutoF *= 60
segundoI += horaI+minutoI
segundoF += horaF+minutoF

if segundoI > segundoF:
    dias += diaFinal-diaInicio-1
    segundos = segundoF - segundoI + (24*60*60)

else:
    dias += diaFinal-diaInicio
    segundos = segundoF - segundoI

horas = segundos/3600.0
segundos %= 3600
minutos = segundos/60.0
segundos %= 60

print("%d dia(s)" % (dias))
print("%d hora(s)" % (horas))
print("%d minuto(s)" % (minutos))
print("%d segundo(s)" % (segundos))
