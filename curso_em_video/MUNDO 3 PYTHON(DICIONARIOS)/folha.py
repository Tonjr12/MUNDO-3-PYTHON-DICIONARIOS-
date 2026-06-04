# Criamos dois dicionários separados para representar estados diferentes
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

# Criamos uma lista comum vazia usando colchetes
brasil = list()

# Usamos o .append() tradicional da lista para colocar os dicionários lá dentro
brasil.append(estado1) # O dicionário do RJ vira o índice 0 da lista
brasil.append(estado2) # O dicionário de SP vira o índice 1 da lista

# Mostra a lista completa com os dicionários aninhados
print(brasil)
# Acessa o índice 0 da lista (mostra o dicionário inteiro do Rio de Janeiro)
print(brasil[0])

# Acessa o índice 1 da lista (mostra o dicionário inteiro de São Paulo)
print(brasil[1])