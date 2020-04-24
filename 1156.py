sequencia = 0
divisor = 1
for i in range(1,40,2):
    sequencia+=i/divisor
    divisor*=2
print("%.2f" %sequencia)