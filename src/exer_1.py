# CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO
# E MOSTRE NA TELA A SUA PORÇÃO INTEIRA
from math import trunc
numero = float(input('Digite um valor: '))
print (' o valor foi {} e a sua porção inteira é {}'.format(numero,trunc(numero)))

