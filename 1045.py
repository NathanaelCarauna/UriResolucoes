entrada = list(map(float, input().split()))
entrada.sort()
entrada.reverse()

a = entrada[0]
b = entrada[1]
c = entrada[2]

if a >= b+c:
    print("Nao forma triangulo".upper())
else:

    if a**2 == (b**2)+(c**2):
        print("triangulo retangulo".upper())

    if a*a > b*b + c*c:
        print("TRIANGULO OBTUSANGULO")

    if a*a < b*b + c*c:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")

    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")
