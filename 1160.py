t = int(input())
for i in range(t):
    populacaoA, populacaoB, crescA, crescB = map(float,input().split())   
    anos = 0
    
    
    while populacaoA <= populacaoB:
        populacaoA *= 1+crescA/100
        populacaoA = int(populacaoA)
        populacaoB *= 1 + crescB/100
        populacaoB = int(populacaoB)
        anos+=1
        if anos > 100:
            break
    if anos > 100:
        print("Mais de 1 seculo.")
        
    else:
        print("%d anos." %(anos))
