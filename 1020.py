dias = int(input())
meses = anos = 0

anos = dias//365
dias%=365
meses = dias//30
dias%= 30

print("{} ano(s)".format(anos))
print("%d mes(es)" %(meses))
print("{} dia(s)".format(dias))