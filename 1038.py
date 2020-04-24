item,qtd = map(int,input().split())
resposta = "Total: R$ %.2f"
total = 0
if item == 1:
    total = 4*qtd
if item ==2:
    total = 4.5*qtd
if item ==3:
    total = 5*qtd
if item ==4:
    total = 2*qtd
if item == 5:
    total = 1.5*qtd
print(resposta %(total))