# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

#Com lista
notas = [7.9, 9.7, 8.2]

#Criando listas
lista = []
lista = list()
lista = [26, 'Vanessa', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e slice ( fatiamneto)

lista = [26, 'Vanessa', 3.14159, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3]) 

# Slices
lista = [10, 50, 30, 40, 25, 60, 5 ]
print (lista[0:3])
print (lista[3:6])
print (lista[3:])
print (lista[2:6:2])

# Iteração com FOR

#1. Utilizando os próprios elementos da lista
for elemento in lista:
    print(elemento)  # percorre os elementos da lista 

# 2. Índices 

print('Comprimento da lista:', len(lista))  # len informa a quantidade de elemnetos que existe na lista 

for i in range(len(lista)):
    print(lista[i]) # imprime os elementos  da lista ou  (print([i]))


# Métodos de lista 

lista = [1, 3, 12, 8, 2]

# append
print('Antes do append:',lista)

lista.append(3)

print('Depois do append:',lista)

# insert
lista.insert(2,10)
print('Depois do insert:',lista)

# extend
lista2 = [1,2,3]

lista.extend(lista2)
print('Depois do extend:',lista)

#pop - remove o ultimo elementi ou um elemento especificado
lista.remove(3)
print('lista apos o pop:',lista)

#remove- retira elemento especificado , o primeiro que encontar 
lista.remove(3)
print('Depois do remove:',lista)

#count -  informa quantoas vezes o elemento aparece na lista.
print('Quantidade de 2 na lista:',lista.count(2))

#index - índice de um determinado elemento
print('índice do elemento 12:',lista.index(12))

# SORT - ordena de forma crescente
lista.sort()
print(lista)

#decrescente
lista.sort(reverse = True)
print(lista)


print(len(lista)) #quantidade de elementos

print(sum(lista)) # soma elemntos

print('Maior elemento da lista:',max(lista))

print('Menor elemento da lista:',min(lista))




