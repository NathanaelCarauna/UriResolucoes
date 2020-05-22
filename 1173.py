n = []
x = int(input())
for i in range(10):
    n.append(x)
    x*=2
    print("N[{}] = {}".format(i,n[i]))