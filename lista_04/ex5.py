import string

def trata_texto (texto):
	
	#remove pontuacoes
	#Removendo pontuacoes do texto:
	for c in string.punctuation:
		texto = texto.replace(c, ' ')
	
	texto = texto.lower()
	texto = list(texto.split())
	
	return texto
	
def conta(texto):
	cont = 0
	for palavra in texto:
		if len(palavra)>4 and (palavra[0] in 'python' or palavra[-1:] in 'python'):
			cont+=1
		else:
			continue
	return cont
	
texto = raw_input("Entre com o texto: ")
texto = trata_texto(texto)
print "Foram encontradas ", conta(texto) , " palavras que tem mais de 4 caracteres e possuem alguma letra da palavra 'python'."


