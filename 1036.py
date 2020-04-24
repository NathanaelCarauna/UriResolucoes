a,b,c = map(float,input().split())

try:
    r1 = (-b+((b*b)-4*a*c)**(1/2))/(2*a)
    print("R1 = %.5f" %(r1))
    r2 = (-b-((b*b)-4*a*c)**(1/2))/(2*a)
    print("R2 = %.5f" %(r2))
except:
    print("Impossivel calcular")