# Algoritmo: calculo_media_TDS
# Rotina que calcula a média das CPS do semestre

# Entrada de dados
print("Para calcular a média de notas de Cps do semestre!")

cp1 = float(input("Digite a nota do CP1: "))
cp2 = float(input("Digite a nota do CP2: "))
cp3 = float(input("Digite a nota do CP3: "))

# Processamento
notas = [cp1, cp2, cp3]
notas.sort(reverse=True)  # Ordena do maior para o menor

n1 = notas[0]  # Maior nota
n2 = notas[1]  # Segunda maior nota

media = (n1 + n2) / 2

# Saída
print("A média é:")
print(media)



 
