continuar = 's'

while continuar == 's':
    repetir = 0
    nota1 = float(input())
    while nota1<0 or nota1>10:
        print("nota invalida")
        nota1 = float(input())
    
    nota2 = float(input())
    while nota2<0 or nota2>10:
        print("nota invalida")
        nota2 = float(input())
    print("media = %.2f" %((nota1+nota2)/2))
    while repetir != 1 and repetir != 2:
        repetir = int(input("novo calculo (1-sim 2-nao)\n"))
        if repetir == 1:
            continuar = 's'
        elif repetir ==2:
            continuar = 'n'