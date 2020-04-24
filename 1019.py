segundos = int(input())
minutos = horas = 0

if segundos>horas:
    horas = segundos//3600
    segundos %= 3600
if segundos>minutos:
    minutos = segundos//60
    segundos %= 60

print("{}:{}:{}".format(horas,minutos,segundos))