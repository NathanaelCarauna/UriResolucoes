def novoCalc(): 
    print("novo calculo (1-sim 2-nao)")
    novoCalculo = int(input())
    if novoCalculo ==1:
        calcularMedia() 
    elif novoCalculo ==2:
        return
    else:
        novoCalc()

def calcularMedia():
    nota1 = float(input())
    while nota1<0 or nota1>10:
        print("nota invalida")
        nota1 = float(input())
    
    nota2 = float(input())
    while nota2<0 or nota2>10:
        print("nota invalida")
        nota2 = float(input())
    print("media = %.2f" %((nota1+nota2)/2))
    novoCalc()
    
calcularMedia()

