entrada = raw_input("Digita tres numeros separados por espaco: ")

num = []

for x in entrada.split(" "):
	num.append(int(x))
print("O maior desses numeros eh %d e o menor eh %d" %(max(num),min(num)))


