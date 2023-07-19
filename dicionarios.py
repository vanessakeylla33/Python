# Dicionários 

# Criando dicionários
dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Vanessa','idade': 26, 'altura': 1.56 }

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionário

dicionario['programador'] = True # adciona ao dicionário 
print(dicionario)

dicionario['altura'] = 2 # sobrescreve  ou seja substitue 
print(dicionario)

# Iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario) # descobrir se a chave existe ou nao no dicionario
print('altura' in dicionario)
