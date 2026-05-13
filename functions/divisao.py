
    # Função de divisão

def dividir(numerador, denominador):
    
 
    if (denominador == 0):
        return 0
    else:
        valorDivisao = numerador/denominador
        return valorDivisao
 
# Testes
print(dividir(10, 2))   # 5.0
print(dividir(0, 5))    # 0
print(dividir(20, 4))   # 5.0

numeradorVariavel = 10
denominadorVariavel =2

div1 = divisao1(numerador=numeradorVariavel, denomominador=denominadorVariavel)
div2 = divisao2(numerador-numeradorVariavel, denominador=denominadorVariavel)

print(f'A divisão de {numeradorVariavel} e {denominadorVariavel} é igual a {div1}')
print(type(div2))