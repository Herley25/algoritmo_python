#lista1 + lista2 - serve para concatenar listas. 
# lista * 5 - imprime a lista cinco vezes.
# <valor> in lista - verifica se o elemento existe dentro da lista. 
# lista.append(x) - acrescentar itens na lista. 
# lista.insert(posição, x) - acrescentar itens na posição tal.
# lista.index(x) - Busca de posição por valor.
# lista.count(x) - Contagem de ocorrências de x.


lista = ['janderson', 'Hellem', 'Lays']
lista.insert(1, 'Herley')
for x in lista:
    print(x)


# MÉTODOS SUPORTADOS POR LISTAS 

# lista.sort() - Ordenar lista.
# lista.reverse() - reverter a lista.
# lista.remove(x) - remove a primeira ocorrência do item.
# lista.pop(POSIÇÃO) - Remove item na posição de índice especificada.
# del lista[POSIÇÃO] - Remove item na posição de índice especificada.
# del lista[i:j] - Remove os itens da posição i até j.

lista.sort()
print(lista)

lista.reverse()
print(lista)


#lista.remove('janderson')
#print(lista)

lista.pop(2)
print(lista)


# OPERAÇÕES COM LISTAS 

# lista[i] = valor - atribuição de valor à posição i.
# lista[i:j] = [x1,x2,x3] - atribuição de valores ao intervalo.
# lista2 = [x+1 for x in lista] - Criar a lista2 com os elementos de lista incrementados.
# len(lista) - Retorna o tamanho da lista.
# list(lista) - Retorna os elementos da lista.
# map(f, lista) - Aplica a função f a cada um dos elementos da lista; para ver o resultado, combine com list().

len(lista) 
if 'Lays' not in lista:
    print("nome não pertence a lista.")
else:
    print("nome encontrado!")


# - ORDENAÇÃO DE DICIONÁRIO
# - Dicionários não são sequências, logo não mantém nenhuma ordem específica de seus objetos.
# - Portanto, se você imprimir os itens de um dicionário, eles podem aparecer em qualquer ordem, sem ordenação.
# - Mas é possível exibir os itens de um dicionário em ordem, usando alguns métodos interessantes.

dic = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
ordenada =  list(dic.keys()) # criando uma lista, obtendo as chaves("keys") do dicionário.  
for key in sorted(dic): # verifica item por item dentro do dicionário e ordena-os.
    print(key, "=", dic[key])

    
