x = float(input())
n = []
for i in range(0,100):
    if i ==0:
        n.append(x)
    else:
        n.append((n[i-1]/2))
    print("N[%d] = %.4f" %(i, n[i]))