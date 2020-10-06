# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO
# CATETO OPOSTO E DO CATETO ADJACENTE DE UM
# TRIÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.

# 1 maneira de fazer

#from math import hypot
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto Adjacente:'))
#hip = hypot(co, ca )
#print ('O valor da hipotenusa será {:.2f}'.format(hip))

# 2 maneira de fazer

#def hipotenusa(co, ca):
#    hip = (co**2 + ca**2)**(1/2)
#    return (hip)

#catoposto = float(input("valor do cateto oposto: "))
#catadjacente = float(input("valor do cateto adjacente: "))
#print (f"o valor da hipotenusa é {hipotenusa(catoposto,catadjacente):.2f}")

# 3 maneira de fazer

def hipotenusa(co,ca):
    return (co**2 + ca**2)**(1/2)

hip = hipotenusa(3,4)
print(f'O valor da hipotenusa é {hip :.2f}')