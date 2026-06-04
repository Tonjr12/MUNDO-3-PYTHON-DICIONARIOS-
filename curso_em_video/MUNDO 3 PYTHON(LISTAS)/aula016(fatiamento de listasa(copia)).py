# ==============================================================================
# AS 3 REGRAS DE OURO DO FATIAMENTO (Para salvar o cérebro):
# 1. Indexação Direta (lista[x]) traz o ITEM REAL (puro).
# 2. Fatiamento (lista[x:y]) sempre traz uma FATIA (uma lista com colchetes [] em volta).
# 3. O Fim é EXCLUSIVO e o Python SÓ ANDA PRA FRENTE. No [início:fim], ele para ANTES do fim.
#    Se o início for maior ou igual ao fim (ex: [1:0] ou [2:2]), ele não anda e dá vazio [].
# ==============================================================================

brasil = list()

# Loop para alimentar a nossa lista de listas
for c in range(0, 3):
    uf = str(input('Unidade Federativa: '))
    sigla = str(input('Sigla do Estado: '))
    estado = [uf, sigla]
    brasil.append(estado[:]) # Tira uma "foto" (cópia) de estado e joga em brasil

print('\n' + '='*40)
print('LISTA COMPLETA:', brasil)
print('='*40 + '\n')

# ------------------------------------------------------------------------------
# BLOCO DO ÍNDICE 0 (Ex: ['Acre', 'AC'])
# ------------------------------------------------------------------------------
print(brasil[0])    # Pega o ITEM PURO do índice 0. (Sem colchetes extras da fatia)
print(brasil[0:0])  # [] -> Começa no 0 e para ANTES do 0. Não andou nada, deu vazio!
print(brasil[0:1])  # [ [item0] ] -> Pega o índice 0 e para antes do 1. (Vem encapsulado em lista)
print(brasil[0:2])  # [ [item0], [item1] ] -> Pega os índices 0 e 1 (para antes do 2)
print(brasil[0:3])  # [ [item0], [item1], [item2] ] -> Pega todo mundo do 0 ao 2

print('-'*40)

# ------------------------------------------------------------------------------
# BLOCO DO ÍNDICE 1 (Ex: ['Bahia', 'BA'])
# ------------------------------------------------------------------------------
print(brasil[1])    # Pega o ITEM PURO do índice 1.
print(brasil[1:0])  # [] -> O início(1) é maior que o fim(0). Python não anda para trás por padrão!
print(brasil[1:1])  # [] -> Começa no 1 e para ANTES do 1. Vazio!
print(brasil[1:2])  # [ [item1] ] -> Começa no 1 e para antes do 2. Pegou só o índice 1.

print('-'*40)

# ------------------------------------------------------------------------------
# BLOCO DO ÍNDICE 2 (Ex: ['Ceará', 'CE'])
# ------------------------------------------------------------------------------
print(brasil[2])    # Pega o ITEM PURO do índice 2.
print(brasil[2:0])  # [] -> Início(2) maior que o fim(0). Tentou andar para trás e falhou.
print(brasil[2:1])  # [] -> Início(2) maior que o fim(1). Falhou de novo.
print(brasil[2:2])  # [] -> Começa no 2 e para ANTES do 2. Vazio!
'''💡 Resumo "Gabarito" para fixar:
Por que aparecem tantos [] vazios no final? Porque você tentou fazer coisas como [2:0]. O Python olha para isso e pensa: "Ué, como vou do 2 até o 0 andando para a frente?". Como ele não consegue, ele te devolve uma lista vazia.

A diferença visual: brasil[0] te dá ['Acre', 'AC']. Já brasil[0:1] te dá [['Acre', 'AC']]. Viu o colchete duplo? Fatiamento sempre gera uma lista nova contendo os pedaços cortados!'''