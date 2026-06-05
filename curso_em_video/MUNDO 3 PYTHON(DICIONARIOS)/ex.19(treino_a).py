print('-=' * 20)
print('         TREINANDO DICIONÁRIOS         ')
print('-=' * 20)

# =====================================================================
# 🚗 TREINO 1: O Dicionário do Carro (Criação e Acesso)
# Objetivo: Criar um dicionário chamado 'carro' com as chaves: 'marca', 'modelo' e 'ano'.
# Depois, mostre uma f-string na tela usando esses dados.
# =====================================================================
print('\n--- Treino 1 ---')

# 1. Crie o dicionário aqui com os dados do carro que você quiser:
carro = {'marca':'chevrolet','modelo':'onix','ano':2026}
print(carro['marca'])
print(carro['modelo'])
print(carro['ano'])
print(f'Eu tenho um {carro["modelo"]} da {carro["marca"]} ano {carro["ano"]}.')
# =====================================================================
# 🎨 TREINO 2: Customizando o Carro (Adicionar, Alterar e Rodar o For)
# Objetivo: Mudar o ano do carro, adicionar uma chave nova chamada 'cor'
# SEM usar .append(), e mostrar tudo usando o laço 'for k, v'.
# =====================================================================
print('\n--- Treino 2 ---')

# 1. Altere o ano do seu carro para um ano mais novo (ex: 2027):

carro['ano']=2027

# 2. Adicione uma chave totalmente nova chamada 'cor' e dê um valor a ela (ex: 'Preto'):
carro['cor']='Preto'

# 3. Use o laço 'for k, v' com o método correto para listar as chaves e valores:
for k, v in carro.items():
    print(f'{k}: {v}')# =====================================================================
# 🔧 TREINO 3: Desfazendo Peças (Deletar chaves)
# Objetivo: Apagar permanentemente a chave 'marca' de dentro do dicionário
# e exibir como o dicionário ficou no final.
# =====================================================================
print('\n--- Treino 3 ---')

# 1. Use o comando correto para apagar a chave 'marca' do dicionário 'carro':
del carro['marca']

# 2. Dê um print comum no dicionário inteiro para confirmar que a marca sumiu:
print(carro)  # 🎯 Só está linha simples!

print('\n' + '-=' * 20)


