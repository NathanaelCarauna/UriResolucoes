n1,n2,n3 = map(int, input().split())
maior = (n1+n2+abs(n1-n2))/2
maior2 = (maior+ n3+ abs(maior - n3))/2
print(str(int(maior2)) + " eh o maior")