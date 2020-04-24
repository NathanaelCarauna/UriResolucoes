q = int(input())
for i in range(q):
    entrada = int(input())
    if entrada %2 ==0:
        if entrada>0:
            print("EVEN POSITIVE")
        elif entrada<0:
            print("EVEN NEGATIVE")
        else:
            print("NULL")
    else:
        if entrada>0:
            print("ODD POSITIVE")
        if entrada<0:
            print("ODD NEGATIVE")