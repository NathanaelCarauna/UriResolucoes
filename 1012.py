a,b,c = map(float, input().split())
triang = a*c/2
circ = 3.14159*c**2
trape = ((a+b)*c)/2
quad = b**2
ret = a*b
print("TRIANGULO: %.3F" %(triang))
print("CIRCULO: %.3f" %(circ))
print("TRAPEZIO: %.3F" %(trape))
print("QUADRADO: %.3F" %(quad))
print("RETANGULO: %.3F" %(ret))