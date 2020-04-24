t = int(input())

for i in range(t):
    x,y = map(int,input().split())
    if y !=0:
        print("%.1f" %(x/y))
    else:
        print("divisao impossivel")