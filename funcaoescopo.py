# ESCOPO DAS VARIÁVEIS 

# O escopo da variável indica sua visibilidade- onde, no código, a variável é acessível.
# Temos dois escopos para variáveis em Python.

# ESCOPO GLOBAL; uma variável global é declarada fora das funções e pode ser acessada por todas as funções presentes 
# no módulo onde é definida.
 
# ESCOPO LOCAL; uma variável local (criada dentro de uma função) existe apenas dentro da função onde foi declarada.



# DESEMPACOTAMENTO
#def listar_itens(w, x, y, z):
#    print(w, x, y, z)

#lista = [21, 25, 65, 69]

#listar_itens(*lista)

# EMPACOTAMENTO
def somar(*argumentos):
    soma = 0
    for i in range(0, len(argumentos)):
        soma += argumentos[i]
    return soma

print('A soma dos argumentos é ' + str(somar(45, 50)))
print('A soma dos argumentos é ' + str(somar(20, 30)))
 

