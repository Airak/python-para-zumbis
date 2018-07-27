import random

inteiros = []

qtde = int(input("Quantidade de itens a serem sorteados: "))

i = 0
maior = 0
menor = 101

for i in range(qtde):
	inteiros.append(random.randint(1,100))
	if inteiros[i] > maior:
		maior = inteiros[i]
	if inteiros[i] < menor:
		menor = inteiros[i]
		
inteiros.sort()
print(inteiros)
print("O maior valor eh %d e o menor eh %d." %(maior, menor))
