'''
DICIONARIO:
Pode ser mensionado de duas formas:
dicionario = {}
dicionario = dict()

TUPLAS:
Pode ser mensionado de duas formas:
tuplas:()
tuple()

LISTAS:
Pode ser mensionado de duas formas:
LISTAS:[]
list ()
'''

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
