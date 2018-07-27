import string

texto = raw_input("Entre com o texto: ")

#Removendo pontuacoes do texto:
for c in string.punctuation:
	texto = texto.replace(c, ' ')

texto.lower()
texto = list(texto.split())

print texto

lista = []

for palavra in texto:
	print palavra
	if palavra[0] in 'python' or palavra[-1:] in 'python':
		lista.append(palavra)
	else: 
		continue
		
print "Palavra que comecam ou terminam com alguma das letras de python:\n", lista
