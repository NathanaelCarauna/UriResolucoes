cod1,qtd1,value1 = input().split()
cod2,qtd2,value2 = input().split()
total = int(qtd1)*float(value1)+int(qtd2)*float(value2)
print("VALOR A PAGAR: R$ %.2f" %(total))
