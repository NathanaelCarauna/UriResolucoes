nCasos = int(input())

for i in range(nCasos):
    nDivisores = 0
    x = int(input())
    for j in range(1,x+1):
        if x%j == 0:
            nDivisores +=1
    if nDivisores >2:
        print("%d nao eh primo" %(x))
    else:
        print("%d eh primo" %(x))
        