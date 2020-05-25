for i in range(int(input())):
    a = 0
    b = 1
    c = 0

    resposta = "Fib({}) = {}"
    fibX = int(input())
    
    if fibX ==0:
        resposta = resposta.format(fibX,a)
    elif fibX ==1:
        resposta = resposta.format(fibX,b)
    else:
        for i in range(1,fibX+1):
            a = b
            b = c
            c = a+b
        resposta = resposta.format(fibX,c)
    print(resposta)