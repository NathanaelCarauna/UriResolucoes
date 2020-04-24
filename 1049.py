entrada1 = input()
entrada2 = input()
entrada3 = input()
resposta = ""

if entrada1 == "vertebrado":
	if entrada2 == "ave":
		if entrada3 == "carnivoro":
			resposta = "aguia"
		elif entrada3 == "onivoro":
			resposta = "pomba"
	elif entrada2 == "mamifero":
		if entrada3 == "onivoro":
			resposta = "homem"
		elif entrada3 =="herbivoro":
			resposta = "vaca"
			
			
elif entrada1 =="invertebrado":
	if entrada2 =="inseto":
		if entrada3 == "hematofago":
			resposta = "pulga"
		elif entrada3 == "herbivoro":
			resposta = "lagarta"
		

	elif entrada2 == "anelideo":
		if entrada3 == "hematofago":
			resposta = "sanguessuga"
		elif entrada3 == "onivoro":
			resposta = "minhoca"

print(resposta)
