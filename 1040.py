n1,n2,n3,n4 = map(float,input().split())
aprovado, reprovado = "Aluno aprovado.","Aluno reprovado."
media = (n1*2+n2*3+n3*4+n4*1)/10

print("Media: %.1f" %(media))
if media >=7:
    print(aprovado)
elif media<5:
    print(reprovado)
elif(5<=media<7):
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame: %.1f" %(notaExame))
    media = (media+notaExame)/2
    if media<5:
        print(reprovado)
    else:
        print(aprovado)
    print("Media final: %.1f" %(media))
