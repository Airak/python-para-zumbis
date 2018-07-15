entrada=raw_input("Digite a string: ")

for x in entrada:
	if x in 'aeiou':
		entrada = entrada[:entrada.index(x)] + "*" + entrada[entrada.index(x)+1:]
print(entrada)
