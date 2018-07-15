'''
	Sequencia de fibonacci usando lista:

num = int(input())
i = 3

fib = [1,1]

if num <= 2:
	print('Fib(1) = 1')
	print('Fib(2) = 1')
else:
	print('Fib(1) = 1')
	print('Fib(2) = 1')
	while i<=num:
		fib.append(fib[i-2]+fib[i-3])
		print('Fib(%d) = %d' %(i,fib[i-1]))
		i+=1		
'''
	
#Sequencia de fibonacci sem usar lista
	
num = int(input())
a = 1
b = 1
i = 1
while i<=num:
	print('Fib(%d) = %d' %(i,a))
	a, b = b, a+b
	i+=1
	
	

