import random

palavra = list(raw_input("Entre com a palavra: "))
#print(palavra)
random.shuffle(palavra)
palavra = str("".join(palavra))
print(palavra)
