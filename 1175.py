n = []
for i in range(20):
    n.append(int(input()))

n.reverse()
for i in range(len(n)):
    print("N[{}] = {}".format(i, n[i]))