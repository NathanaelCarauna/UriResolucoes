salario = float(input())
rNovoSalario = "Novo salario: %.2f"
rReajuste = "Reajuste ganho: %.2f"
rPercentual = "Em percentual: {} %"

if salario>2000:
    percentual = 4
    novoSalario = salario + salario*percentual/100
    reajuste = salario*percentual/100
elif salario>1200:
    percentual = 7
    novoSalario = salario + salario*percentual/100
    reajuste = salario*percentual/100
elif salario>800:
    percentual = 10
    novoSalario = salario + salario*percentual/100
    reajuste = salario*percentual/100
elif salario>400:
    percentual = 12
    novoSalario = salario + salario*percentual/100
    reajuste = salario*percentual/100
elif salario>=0:
    percentual = 15
    novoSalario = salario + salario*percentual/100
    reajuste = salario*percentual/100

print(rNovoSalario %(novoSalario))
print(rReajuste %(reajuste))
print(rPercentual.format(percentual))