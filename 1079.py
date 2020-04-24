t = int(input())

for i in range(t):
    a,b,c = map(float,input().split())
    mediaP = (a*2 + b*3 +c*5)/10
    print(round(mediaP,1))