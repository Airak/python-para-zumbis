import random

qtde = int(input("Qual a quantidade de numeros a ser sorteado: "))

i = 0
pares = []
impares = []
numeros = []

for i in range (qtde):
	numeros.append(random.randint(1,100))
	if numeros[i]%2 == 0:
		pares.append(numeros[i])
	else:
		impares.append(numeros[i])
		
numeros.sort()
pares.sort()
impares.sort()

print  "\nNumeros: ", numeros
print "Pares: ", pares
print "Impares: ", impares 
