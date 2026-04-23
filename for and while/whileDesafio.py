#Programa para verificar o While
 
# Rotina incrementa x
 
x = 8
 
#inicio
#Cardinalidade desta extrutura é: (0,N) --> (0,10)
 
while(x < 10):
    print(f'X é igual a {x} 1')
    #x = x + 1
    x +=1
 
print(f'X é igual a {x} 2')

# Simulação de estrutura Pós-Condicional (Do-While)
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
 
    match (opcao):
      case "1":
        print(">> Abrindo tela de cadastro...")
      case "2":
        print(">> Abrindo tela de exclusão...")
      case "3":
        print(">> Gerando relatório em PDF...")
      case "0":
        print("Saindo do sistema... Até logo!")
        break
      case _:
        print("Opção inválida! Tente novamente.")

  # Simulação de estrutura Pós-Condicional (Do-While/If and Elif)
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
 
    if opcao == "1":
        print(">> Abrindo tela de cadastro...")
    elif opcao == "2":
        print(">> Abrindo tela de exclusão...")
    elif opcao == "3":
        print(">> Gerando relatório em PDF...")
    elif opcao == "0":
        print("Saindo do sistema")
        break
    else:
        print("Opção inválida! Tente novamente.")

# Programa para verificar o (For)

# Rotina incrementa x

#inicio
# Cardinalidade desta estrutura é: (0,N) --> (0,10)

for x in range(8, 10):
    print(f'X é igual a {x} 1')

print(f'X é igual a {x} 2')

#Definindo uma Função (For)
def exibir_menu():
    print("\n--- SISTEMA DE GESTÃO ---")
    print("1. Adicionar Item")
    print("2. Remover Item")
    print("3. Visualizar Relatório")
    print("0. Sair")
    print("-------------------------")
