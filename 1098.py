i = 0
while i<2:
    for j in range(1,4):
        if i==0 or i == 1 or i >= 1.9:
            print("I=%.0f J=%.0f" %(i,j+i))
        else:    
            print("I={} J={}".format(round(i,1),round(j+i,1)))
    i+=0.2