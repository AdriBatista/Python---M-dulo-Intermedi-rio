
#vpara os conjuntos usa-se chaves {}
c1 = {16, 8, 21, 30, 41, 28}


# o tipo é uma classe 'set' que contem os metodos que permite trabalhas com CONJUNTOS
#notamos que conjunto é da classe set
#conunto não aceita valores repetidos, ao printar apenas um deles é mostrado na saida
a = type(c1)
print(a)

print('=============++++++++++++++++++')

#vamor ver o tamanho de elementos que contem essa chave
b = len(c1)
print(b)


print('\n\n++++++++++++============+++++++\n')

c2 = {10, 8, 5, 10, '5'}
print(c2)    # mais mostrar apenas um 10 e '5' é uma string, por isso repetwe

print('\n\n++++++++++++============+++++++\n')

#cuidado para não confundir com dicionário
c3 = {}
print(type(c3)) #é da classe do tipo dict, não é cojunto vazio

print('\n\n++++++++++++============+++++++\n')

#para  contruir um conjunto vazio, precisa usar o método contrutor da classe set()
c4 = set()
print(len(c4)) #vai mostra que o tamanho do conjunto é zero '0'

# c4 = set(4, 8 , 20) isso tá errado, pois o método set() só aceita um unico elemento
# para usar mais elemento no set(), precisa usar uma tupla ( ()), ou lista que é um array ( [])

print('\n\n++++++++++++============+++++++\n')

c5 = set((10,25, 'casa'))
print(c5)

print('\n\n++++++++++++============+++++++\n')

c6 = set([10, 8, 'vaca'])
print(c6)

print('\n\n++++++++++++============+++++++\n')

