t = int(input())
dentro = 0
fora = 0
for i in range(t):
    n = int(input())
    if 10<=n<=20:
        dentro +=1
    else:
        fora +=1
print("%d in" %(dentro))
print("%d out" %(fora))