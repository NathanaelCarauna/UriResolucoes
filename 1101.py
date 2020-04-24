while(True):
    x,y = map(int,input().split())
    soma = 0
    if x <= 0 or y <= 0:
        break
    if x<=y:
        for i in range(x,y+1):
            soma+=i
            print(i,end=" ")
            
        print("Sum=%d" %(soma))
    elif x>y:
        for i in range(y,x+1):
            print(i,end=" ")
            soma+=i
        print("Sum=%d" %(soma))
        