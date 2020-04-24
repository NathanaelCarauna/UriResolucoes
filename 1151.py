x = int(input())
a = 0
b = 1
c = a+b
sequencia = "%d"%(a)

if x == 1:
    print(sequencia)
if x == 2:
    print(sequencia + " %d"%(b))
if x ==3:
    print(sequencia + " %d"%(b) +" %d"%(c))
if x>3:
    sequencia = "{} {} {}".format(a,b,c)
    for i in range(1,x-2):
        a = b
        b = c
        c = a+b
        sequencia += " %d"%(c)
    print(sequencia)
    
