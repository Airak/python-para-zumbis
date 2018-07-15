peso=float(input("Peso: "))

if peso>50:
	excesso = peso - 50
	multa = float(excesso*4)
else:
	excesso, multa = 0, 0
	
print("Foi encontrado um excesso de %5.2f e por isso a multa sera de %5.2f" %(excesso, multa))
