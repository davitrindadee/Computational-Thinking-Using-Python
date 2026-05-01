#Se é ou não Adulto 

varIdade = input("Digite sua idade: ")
varIdade = int(varIdade)

if varIdade >= 18:
    print("é Adulto!")
else:
    print("Não é Adulto!")

#TERNÁRIO (Operadores ternários são uma forma curta de escrever uma condição (if/else) em uma única linha.)

print("Adulto!" if varIdade >= 18 else "Não é Adulto!")

media = input("Digite a média: ")
media = int(media)
print("Aprovado!" if media >= 7 else "Reprovado!")

#Operadores Ternários c/ Laços de Decisão 

ternarioRepeticao = []

for i in range(1, 10):
    ternarioRepeticao.append(i)
print(ternarioRepeticao)

ternarioRepeticao = [numero for numero in range(1, 10):]
print(ternarioRepeticao)

#Mapeando Iterações 

lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d"]
for index in range(0,len(lista1)) :
print(lista1[index])
print(lista2[index])

print(Iteracoes)

#Desafio - Operadores Ternários com Laços de Repetição

#Lista de Númros de 1 até 20 com passo 1 usando operadores ternários:

numeros = [numero for numero in range(1,20,1)]
print(numeros)


# Exemplo de Algoritmo que descreve os passos para troca de pneu (pseudo-código):
print("1. Estacione o carro em um local seguro e acione o freio de mão.")
print("2. Pegue o macaco, a chave de roda e o estepe do carro.")
print("3. Posicione o macaco sob o ponto de apoio do carro próximo à roda")
print("4. Levante o carro usando o macaco até que a roda esteja suspensa no ar.")
print("5. Use a chave de roda para afrouxar os parafusos da roda, girando-os no sentido anti-horário.")
print("6. Remova os parafusos completamente e retire a roda do carro.") 
print("7. Coloque o estepe no lugar da roda removida e alinhe os furos dos parafusos.")
print("8. Aperte os parafusos com a mão para fixar o estepe no lugar.")
print("9. Use a chave de roda para apertar os parafusos, girando-os no sentido horário, até que estejam firmes.")
print("10. Abaixe o carro usando o macaco e remova-o do ponto de apoio.")
print("11. Guarde o macaco, a chave de roda e a roda danificada no porta-malas do carro.")
print("12. Verifique a pressão do estepe e dirija com cuidado até um local onde possa consertar ou substituir a roda danificada.")      
print("Fim do processo de troca de pneu!")



#OUTRO EXEMPLO
#INÍCIO
enquanto not(LocalLivreSeguro): # type: ignore
escreva("Hello, World!")
leia(LocalLivreSeguro)
#LocalLivreSeguro = Falso
#FIM ENQUANTO (WHILE)
Escreva("Verifique a condição do pneu reserva, do kit macaco e do carrinho de rodas!")

temKitFerramentas = bool(input("Você tem o kit de ferramentas? (True/False): "))
temPneuReserva = bool(input("Você tem um pneu reserva? (True/False): "))
temMacaco = bool(input("Você tem um macaco? (True/False): "))

if temKitFerramentas and temPneuReserva and temMacaco:
    print("Você tem tudo o que precisa para trocar o pneu!")    
else:
    print("Você não tem todos os itens necessários para trocar o pneu. Verifique o que está faltando.")     
#FIM




