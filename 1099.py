t = int(input())

for i in range(t):
    soma = 0
    x,y = map(int,input().split())
    if x> y:
        for j in range(x-1,y,-1):
            if j%2!=0:
                soma+=j
    if x<y:
        for j in range(x+1, y):
            if j%2!=0:
                soma+=j
    print(soma)