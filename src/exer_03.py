# RANDOM FAZ COM QUE O COMPUTADOR PENSE EM ALGO ALEATÓRIO

from random import choice
nome = str(input('Digite seu nome: '))
nome_2 = str(input('Digite seu nome: '))
nome_3 = str(input('Digite seu nome: '))
nome_4 = str(input('Digite seu nome: '))
lista = [nome, nome_2, nome_3, nome_4]
escolhido = choice(lista)
print ('O aluno escolhido foi {}'.format(escolhido))


