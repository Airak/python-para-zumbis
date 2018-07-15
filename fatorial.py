def fatorial():
	num = int(input('Entre com um numero: '))
	res = 1
	while num>0 :
		res *= num
		num -= 1
	print(res)
	
fatorial()
