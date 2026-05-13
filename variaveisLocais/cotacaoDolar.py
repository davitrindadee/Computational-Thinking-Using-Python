# Variável global
cotacao_dolar = 5.03

'''
Criem um código com uma variável global chamada
cotacao_dolar (hoje 5,03 R$/US$),
com a cotação do dólar do dia, e depois criem duas funções:

- uma que utilize a cotação do dólar, chamada conversao_dolar_real,
que converta valores em R$ para US$;

- Outra que altere a cotação do dólar na variável global, chamada
correcao_cotacao.
'''

# Função para converter Real em Dólar
def conversao_dolar_real(valor_real):
    return valor_real / cotacao_dolar


# Função para alterar a cotação do dólar
def correcao_cotacao(nova_cotacao):
    global cotacao_dolar
    cotacao_dolar = nova_cotacao


# Testes
print("Cotação atual:", cotacao_dolar)

valor = 100
print("R$ 100 em dólar:", conversao_dolar_real(valor))

# Alterando a cotação
correcao_cotacao(5.20)

print("Nova cotação:", cotacao_dolar)

print("R$ 100 em dólar com nova cotação:", conversao_dolar_real(valor))