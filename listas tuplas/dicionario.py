#VARIÁVEIS INDEXADAS = SÃO VARIÁVEIS QUE PODEM ARMAZENAR VÁRIOS VALORES, COMO LISTAS, MATRIZES E TENSORES.

lista = (1,2,3,4,5,6,7,8,9)
for i in lista:
    print(i)

listaString = ["A", "B", "C"]
len(listaString)

V = [10, 20, 30]


#MATRIZ = É UMA ESTRUTURA DE DADOS BIDIMENSIONAL, OU SEJA, UMA TABELA COM LINHAS E COLUNAS.

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
print (array[1])

'''
type(lista1) = list
type(array1) = numpy.array
'''

#Vetor que armazena IDs de usuários créditos na casa, e bloquear por idade
vetorDados = [["10" , 20 , True ],["20", 20 , False]]

#VETOR NOTAS = [7, 5, 8, 6, 9]
vetorNotas = [7, 5, 8, 6, 9]
for index in range(0, len(vetorNotas)): #len(vetorNotas) = "n"
#Não muda o tamanho da busca quando mudamos o tamanho da lista
    print(vetorNotas[index])

# O lista().sort() organiza os dados em ordem CRESCENTE :
vetorNotas.sort()
print(vetorNotas)

vetorNotas.sort(reverse=True) #reverse = True = ORDEM DECRESCENTE
print(vetorNotas)

notas = [7, 5, 8, 6, 9]
notas.sort()
notas.sort(reverse=True)

maioresNotas = notas[0:3] #FATIAMENTO DE LISTA = SELECIONAR APENAS UMA PARTE DA LISTA ORIGINAL
print(maioresNotas)

notasMaiores = notas[-2:-1] #FATIAMENTO DE LISTA COM ÍNDICES NEGATIVOS = SELECIONAR APENAS UMA PARTE DA LISTA ORIGINAL, COMEÇANDO DO FINAL
print(notasMaiores[len(notasMaiores)-1]) #len(notasMaiores) = 1, len(notasMaiores) - 1 = 0, notasMaiores[0] = 9

#REMOVE = REMOVER A PRIMEIRA OCORRÊNCIA DE UM ELEMENTO NA LISTA
min = [7, 5, 8, 6, 9]
min.remove(5) #5 = ELEMENTO A SER REMOVIDO

max = [7, 5, 8, 6, 9]
max.pop() #POP = REMOVER O ÚLTIMO ELEMENTO DE UMA LISTA E

#INDEX = RETORNAR O ÍNDICE DA PRIMEIRA OCORRÊNCIA DE UM ELEMENTO NA LISTA
notas.index(8) #8 = ELEMENTO A SER PROCURADO

#ENTEND ENDO O MÉTODO EXTEND() = ADICIONAR OS ELEMENTOS DE UMA LISTA AO FINAL DE OUTRA LISTA
notasSemestre1 = [7, 5, 8, 6, 9]
notasSemestre2 = [8, 6, 9, 7, 5]
notas = notasSemestre1
notas.extend(notasSemestre2) #EXTEND = ADICIONAR OS ELEMENTOS DE UMA LISTA AO FINAL DE OUTRA LISTA
print(notas)

#CLEAR = REMOVER TODOS OS ELEMENTOS DE UMA LISTA
notas.clear() #CLEAR = REMOVER TODOS OS ELEMENTOS DE UMA LISTA
print(notas)

len(notas) #len() = RETORNAR O NÚMERO DE ELEMENTOS EM UMA LISTA 
del notas #DEL = EXCLUIR UMA VARIÁVEL, INCLUINDO LISTAS

#MÉTODO SORT() = ORGANIZA OS ELEMENTOS DE UMA LISTA EM ORDEM CRESCENTE
vetorNotas[0] = 10
nota1 = 9 
nota1 = 10 
print(nota1)
#Sempre irá pegar o último valor.

#APPEND = ADICIONAR UM ELEMENTO NO FINAL DA LISTA
vetorGenerico = [1, 2, 3, 4] #Adicionar um valor dentro da lista 
vetorGenerico.append(5)
print(vetorGenerico)

V.append(True)
print(V)
#Um argumento pode ser um objeto de qualquer tipo, inclusive outra lista.   
V.append([1, 2, 3])
print(V)

listaVazia = []
print(f'A lista vazia começou desse jeito: {listaVazia}')
listaVazia.append(1)
listaVazia.append(2)
listaVazia.append(3)
listaVazia.append(4)
listaVazia.append(5)
print(f'A lista vazia terminou desse jeito: {listaVazia}')

#COUNT = CONTAR QUANTAS VEZES UM ELEMENTO APARECE NA LISTA ORIGINAL 
vetorGenerico.count(1) #1 = True
#list() = contrutor do objeto tipo lista 
list((1, 2, 3, 4)).count("Elemento a ser contado")

vetorTeste = [10, 20, 30, True, [1, 2, 3]]
print(vetorTeste.count(10))

vetorNovo = V.copy() #COPY = CRIAR UMA CÓPIA DE UMA LISTA EXISTENTE.



#REMOVE = REMOVER A PRIMEIRA OCORRÊNCIA DE UM ELEMENTO NA LISTA
vetorGenerico.remove(1)

#POP = REMOVER O ÚLTIMO ELEMENTO DE UMA LISTA E RETORNAR O VALOR REMOVIDO 
vetorGenerico.pop()
elementoRemovido = vetorGenerico.pop()
print(f"O elemento removido foi: {elementoRemovido}")

elementoExtraido = vetorGenerico.pop() 
print(f"Foi apagado do banco de dados o elemento: {elementoExtraido}")

variavelRessucitavel= vetor.pop(4) #POP(ÍNDICE) = REMOVER O ELEMENTO DE UM ÍNDICE ESPECÍFICO E RETORNAR O VALOR REMOVIDO
print(V) 
vetor.insert(4, variavelRessucitavel) #INSERT(ÍNDICE, VALOR) = INSERIR UM ELEMENTO EM UM ÍNDICE ESPECÍFICO, DESLOCANDO OS ELEMENTOS EXISTENTES PARA A DIREITA

#LISTAS DUPLAS = LISTAS DENTRO DE LISTAS, OU SEJA, UMA ESTRUTURA DE DADOS BIDIMENSIONAL.
tupla = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(tupla[0][1]) #TUPLA DUPLA = TUPLAS DENTRO DE TUPLAS, OU SEJA, UMA ESTRUTURA DE DADOS BIDIMENSIONAL.

listaDupla = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listaDupla[0][1]) #LISTA DUPLA = LISTAS DENT

tupla = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(0, len(tupla)):
    for j in range(0, len(tupla[i])):
        print(tupla[i][j])

tupla.acont(2)
tupla.index(0)
max(tupla) 
min(tupla) 
sum(tupla)



