#import de bibliotecas

#Documentação 

#Variáveis Globais 

PI = 3.1415
GRAVIDADE = 9.81

variavel = imput("Mensagem para o usuário: ")
print(variavel)
print(type(variavel))

#Exercício 1

#Exemplo
nomeCompleto = input("Digite seu nome e sobrenome, separado por espaços!!! -->")
nomeCompleto = nomeCompleto.upper()
print(nomeCompleto)

# O input é a entrada de dados. No Python, existe a função input(), que serve para receber informações digitadas pelo usuário. Quando o programa encontra um input, ele pausa a execução e espera o usuário digitar algo. O input() sempre retorna um texto (string), mesmo que o usuário digite números. Se você quiser transformar esse valor em número, precisa converter com int() ou float(). Você também pode colocar uma mensagem dentro do input(), que será exibida antes de esperar a digitação — isso funciona como um “pedido de informação” para o usuário.
# O output e a saida. Na pratica nao existe no python uma funcao chamada output, o que existe e a funcao print, que e utilizada para imprimir algo na tela, ou seja, para gerar uma saida. O print pode receber varios argumentos, separados por virgula, e vai imprimir todos eles na tela, separados por um espaco. O print tambem pode receber um argumento chamado end, que define o que vai ser impresso no final da linha, por padrao o end e um espaco, mas pode ser alterado para qualquer coisa, como por exemplo uma quebra de linha (\n) ou uma tabulacao (\t).


print("Olá Mundo") #imprime Olá Mundo na tela
print("Olá", "Mundo") #imprime Olá Mundo na tela, separado por um espaco
print("Olá", "Mundo", end="\n") #imprime Olá Mundo na tela, separado por um espaco e
#depois quebra a linha
print("Olá", "Mundo", end="\t") #imprime Olá Mundo na tela, separado por um espaco e
#depois tabula a linha
print("Olá Mundo")


# Exercício: Múltiplos Argumentos (O Simples)

# Criando as variáveis
produto = "Pão"
quantidade = 15
preco = 0.50

# Exibindo tudo no terminal
print("Item:", produto, "Quantidade:", quantidade, "Preço:", preco)


#Exercício B

#Criando as variáveis
quilometragem = 123.5
volumeCombustivel = 10.5 
consumo = quilometragem/volumeCombustivel

#Exibindo tudo no terminal 
print("A taxa de consumo do veículo foi de {:.2f} km/1".fortmt(consumo))

# A letra f antes do dois simula o float!!! 
# Ex:
# print(f"A taxa de consumo do veículo foi de {round: 2f} km/1")
# print(f"A taxa de consumo do veículo foi de {consumo: 2f} km/1")
