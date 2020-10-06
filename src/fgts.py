funcionario = str(input("Nome: "))
valor = float(input("Salário: "))
fgts = (valor * 0.08)
if (valor <= 1840):
    print (f"R${fgts :.2f} reais, este será o valor a ser recolhido.")

