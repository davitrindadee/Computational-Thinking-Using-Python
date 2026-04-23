#VARIÁVEIS INDEXADAS

lista = (1,2,3,4,5,6,7,8,9)
for 1 in lista:
    print(1)

listaString = ["A", "B", "C"]
len(listaString)

V = [10, 20, 30]


#MATRIZ

matriz = [[1, 2, 3, 4 ], [5, 6, 7 ,8]]
for i in range(0, len(matriz)):
    print(matriz[i])


'''
TENSORES É UM RECIPIENTE QUE ARMAZENA DADOS EM N DIMENSSÕES.
É A GENERALIZAÇÃO DE CONCEITOS QUE JÁ COHECEMOS:
ESCALAR (RANK 0): UM ÚNICO NÚMERO (EX: 25).
VETOR (RANK 1): UMA LISTA DE NUMEROS [X, Y].
MATRIZ (RANK 2): UMA TABELA DE NÚMEROS (LINHAS E COLUNAS).
TENSOR (RANK 3 OU SUPERIOR):UM "CUBO" OU ESTRUTURAAS DE DIMENSÕES AINDA MAIORES. 
'''

import numpy as np 
array = np.array([1, 2, 3])
print(array 1)

'''
type(lista1) = list
type(array1) = numpy.array
'''

#Vetor que armazena IDs de usuários créditos na casa, e bloquear por idade
vetorDados = [["10" , 20 True ],["20", 20 , False]]

#VETOR NOTAS
vetorNotas = [7, 5, 8, 6, 9]
for index in range(0, len(vetorNotas)): #len(vetorNotas) = "n"
#Não muda o tamanho da busca quando mudamos o tamanho da lista
    print(vetorNotas(index))

# O lista().sort() organiza os dados em ordem CRESCENTE :
vetorNotas.sort()
print(vetorNotas)

 #Métodos das listas
vetorNotas[0] = 10
nota1 = 9 
nota1 = 10 
print(nota1)
#Sempre irá pegar o último valor.

vetorGenerico = [1, 2, 3, 4] #Adicionar um valor dentro da lista 
vetorGenerico.append(5)
print(vetorGenerico)

listaVazia = []
print(f'A lista vazia começou desse jeito: {listaVazia}')
listaVazia.append(1)
listaVazia.append(2)
listaVazia.append(3)
listaVazia.append(4)
listaVazia.append(5)
print(f'A lista vazia terminou desse jeito: {listaVazia}')

#COUNT
vetorGenerico.count(1) #1 = True
#list() = contrutor do objeto tipo lista 
list((1, 2, 3, 4)).count("Elemento a ser contado")

#REMOVE 
vetorGenerico.remove(1)

#POP 
vetorGenerico.pop()
elementoRemovido = vetorGenerico.pop
print(f"O elemento removido foi: {elementoRemovido}")
