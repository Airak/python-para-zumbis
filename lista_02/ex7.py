# -*- coding: utf-8 -*-

tamanho = int(input())
cobertura = tamanho/3
latas = cobertura/18

if tamanho % 54 != 0: 
	latas= latas + 1

preco = latas*18


print('Deverao ser compradas %d lata(s) de tinta, o valor a ser pago eh %d' %(latas, preco) )
