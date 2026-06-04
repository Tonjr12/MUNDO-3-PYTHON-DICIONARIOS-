# Criamos um dicionário vazio para servir de molde temporário
estado = dict()

# Criamos uma lista vazia para armazenar todos os estados digitados
brasil = list()

# Um laço para repetir a leitura dos dados 3 vezes do teclado
for c in range(0, 3):
    # Lê o texto e guarda diretamente na chave 'uf' do molde
    estado['uf'] = str(input('Unidade Federativa: '))
    # Lê o texto e guarda diretamente na chave 'sigla' do molde
    estado['sigla'] = str(input('Sigla do Estado: '))

    # 🚨 O GRANDE SEGREDO DA AULA: Adiciona uma CÓPIA do molde na lista.
    # Em dicionários, usar [:] dá erro. Precisamos usar o método .copy()!
    brasil.append(estado.copy())

# Primeiro laço 'for' para varrer a lista. 'e' representa cada dicionário de estado
for e in brasil:
    # Laço interno para varrer o dicionário atual usando as chaves (k) e valores (v)
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

print('-' * 40)

# Outra forma estilizada que ele mostra para exibir os resultados limpos
for e in brasil:
    # Este laço passa apenas pelos valores (ex: Rio de Janeiro, depois RJ)
    for v in e.values():
        print(v, end=' ')  # Mostra os valores lado a lado com espaço
    print()  # Quebra a linha quando termina o estado atual