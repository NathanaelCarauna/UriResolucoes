v1, v2 = map(int,input().split())

if v1<=v2:
    if v2%v1 ==0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    if v1%v2 == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")