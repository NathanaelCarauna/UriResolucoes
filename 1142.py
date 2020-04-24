n = int(input())
x=1
linhas = 1
while True:
    if linhas > n:
        break
    if x%4==0:
        print("PUM")
        x+=1
        linhas +=1
        continue
    print(x, end=" ")
    x+=1
