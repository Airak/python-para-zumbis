import random

qtde = int(input("Quantidade de numeros a serem sorteados: "))

i = 0
lis1 = []
lis2 = []
lis3 = []

for i in range(qtde*2):
	num = random.randint(1,100)
	if i%2 == 0:
		lis1.append(num)
	else:
		lis2.append(num)
	lis3.append(num)
		
print "Numeros gerados para a primeira lista: ", lis1
		
print "Numeros gerados para a segunda lista: ", lis2
		
print "Numeros intercalados: ", lis3
