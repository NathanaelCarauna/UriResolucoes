i = 1
j=7
while i<10:
    for j in range(7,16,2):
        for x in range(j,j-3,-1):
            print("I={} J={}".format(i,x))
        i+=2
