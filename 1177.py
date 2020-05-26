t = int(input())
n = []
for i in range(1000):
    for j in range(t):
        n.append(j)
    print("N[%d] = %d" %(i,n[i]))
