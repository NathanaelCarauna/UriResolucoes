while True:
    x,y = map(int, input().split())
    if x == y:
        break
    elif x>y:
        resposta = "Decrescente"
    else:
        resposta = "Crescente"
    print(resposta)