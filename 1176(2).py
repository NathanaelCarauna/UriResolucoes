fib = [0,1]

for i in range(59):
    fib.append(fib[-1]+fib[-2])
for i in range(int(input())):
    x = int(input())
    print("Fib(%d) = %d" %(x, fib[x]))