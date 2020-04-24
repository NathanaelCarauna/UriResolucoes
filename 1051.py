salario = float(input())
salario = round(salario,2)
resposta = "R$ %.2f"

if salario <=2000:
    print("Isento")
if 2000 <salario<=3000:
    imposto = (salario-2000)*0.08
    print(resposta %(imposto))
if 3000<salario<=4500:
    imposto = (salario-3000)*0.18 + 1000*0.08
    print(resposta %(imposto))
if salario>4500:
    imposto = (salario-4500)*0.28+1500*0.18+1000*0.08
    print(resposta %(imposto))
