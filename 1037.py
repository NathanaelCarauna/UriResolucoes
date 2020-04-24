entrada = float(input())
resposta = "Intervalo "
if 0 <= entrada <= 100:
    if 0 <= entrada <= 25:
        resposta += "[0,25]"
    elif 25 < entrada <= 50:
        resposta += "(25,50]"
    elif 50 < entrada <= 75:
        resposta += "(50,75]"
    elif 75 < entrada <= 100:
        resposta += "(75,100]"
    print(resposta)
else:
    print("Fora de intervalo")
