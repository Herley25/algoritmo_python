funcionario = str(input("Nome do funcionário: "))
valor = float(input("Remuneração: "))
cal1 = (46.54/30) * 30
cal2 = (32.80/30) * 30
if (valor <= 907.77):
    print (f"O valor do beneficio será de R${cal1 :.2f} ")
elif (valor >= 907.78) and (valor <= 1364.43):
    print (f"O valor do beneficio será de R${cal2 :.2f} ")

else:
    print('Não Cadastrado !!!')







