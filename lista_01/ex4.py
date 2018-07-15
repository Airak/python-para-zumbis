salario=float(input("Digite o salario: "))
aumento=float(input("Digite o aumento: "))

aumento = salario*(aumento/100)
salario += aumento
print("O aumento sera de %5.2f e o salario atualizado eh %5.2f" %(aumento,salario))
