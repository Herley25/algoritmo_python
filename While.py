# LOOP WHILE

# Estrutura de repetição que permite executar um bloco de códico, enquanto a condição for verdadeira
# Sintaxe;

#  while (condição):
#   bloco de códico.
# 
# ex: 

#controle = ""
#while (controle != "s"):
#    print("a.Pagar") 
#    print("b.Receber") 
#    print("c.Transferir") 
#    print("s.Sair")
#    controle = input('Digite a opção desejada: ')
#print('Atividade Encerrada') 

#WHILE COM BREAK

# A declaração break termina o loop atual e consegue a execução na próxima declaração após o loop.
# O usos mais comum é quando alguma condição externa é disparada e requer saída imediata do loop.
# O comando brack pode ser usado tanto em loops while quanto em lopps for.

cont = 20
while (cont > 0):
    print(f"o valor da variável é igual a {cont}")
    cont -= 1
    if (cont == 11):
        break
print('Loop interrompido no valor 11')    