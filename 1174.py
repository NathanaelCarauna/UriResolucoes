a = []
for i in range(100):
    a.append(float(input()))
    if a[i] <=10:
        print("A[{}] = {}".format(i,a[i]))
