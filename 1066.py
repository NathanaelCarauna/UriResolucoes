par = impar = positivo = negativo = 0

for i in range(5):
    entrada = float(input())
    if entrada>0:
        positivo+=1
    if entrada<0:
        negativo+=1
    if entrada%2 ==0:
        par +=1
    if entrada%2!=0:
        impar +=1
print("%d valor(es) par(es)" %(par))
print("%d valor(es) impar(es)" %(impar))
print("%d valor(es) positivo(s)"%(positivo))
print("%d valor(es) negativo(s)"%(negativo))