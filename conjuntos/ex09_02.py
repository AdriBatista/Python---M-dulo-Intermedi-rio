texto = 'qualquer texto'
print(type(texto))

print('++++++++++++++++++++++++++++++++++++++++++++++======+++++++++++++')


#usando o metod0 construtor set() para criar conjunto
c1 = set(texto)
print(c1)  #vai mostrar os caracteres deste obleto sem repetir enão na mesma ordem

print('++++++++++++++++++++++++++++++++++++++++++++++======+++++++++++++')

tupla = (32,73,41)
c2 = set(tupla)
print(c2)  # vai criar uma tupla()

print('++++++++++++++++++++++++++++++++++++++++++++++======+++++++++++++')

lista = [10,25,48]
c3 = set(lista)
print(c3) #criando uma lista[]

print('++++++++++++++++++++++++++++++++++++++++++++++======+++++++++++++')

c4 = set(c1)
print(c4) #vai ser os mesmos valores iguai , tanto c4 e c1

print('++++++++++++++++++++++++++++++++++++++++++++++======+++++++++++++')

#vamos ver se eles estão na mesma memoria, usaremos os Id
A = print(id(c1))

print('++++++++++++++++++++++++++++++++++++++++++++++======+++++++++++++')

B = print(id(c4))   #logo eles são conjuntos onde aponta em diferente parte na memória

#OBS: c4 = c1 , ai sim aponta para o mesmo ligar da memória
