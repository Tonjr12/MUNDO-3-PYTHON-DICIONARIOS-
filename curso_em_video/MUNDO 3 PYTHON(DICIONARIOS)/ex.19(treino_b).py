print('-=' * 20)
print('    TREINO B: LISTAS + DICIONÁRIOS & COPY    ')
print('-=' * 20)

# =====================================================================
# 🎬 PARTE 1 (Baseada no Exemplo 2): Dicionários dentro de Listas
# Objetivo: Criar uma lista chamada 'locadora'. Criar 2 dicionários de filmes
# e dar .append() deles na lista. Depois, acessar um dado específico.
# =====================================================================
print('\n--- Parte 1: Estrutura Estática ---')

# 1. Crie uma lista vazia chamada 'locadora':
locadora = list()

# 2. Crie o dicionário 'filme1' com as chaves: 'titulo' (Star Wars) e 'ano' (1977)
filme1 = {'titulo':'Star Wars', 'ano':'1977'}

# 3. Crie o dicionário 'filme2' com as chaves: 'titulo' (Matrix) e 'ano' (1999)
filme2 = {'titulo': 'Matrix','ano':'1999'}

# 4. Adicione (append) o filme1 e o filme2 dentro da lista locadora:
locadora.append(filme1)
locadora.append(filme2)

# 5. TESTE DE ACESSO: Mostre na tela o título do segundo filme (Matrix)
# Dica: Acesse primeiro o índice da lista e depois a chave do dicionário! ex: lista[índice]['chave']
print(locadora)
print(locadora[1]['titulo'])


# =====================================================================
# 🎮 PARTE 2 (Baseada no Exemplo 3): Inputs Dinâmicos e o Super .copy()
# Objetivo: Criar um loop 'for' para ler o nome de 3 JOGOS e suas PLATAFORMAS.
# Salvar tudo numa lista usando o método correto de cópia.
# =====================================================================
print('\n--- Parte 2: Inputs Dinâmicos com .copy() ---')

# Já deixei a lista e o dicionário molde criados para você:
jogos_salvos = list()
molde_jogo = dict()

# 1. Crie um laço 'for' que vai repetir 3 vezes (use o range):
for c in range(0, 3):
# Dentro do laço, peça o input do nome do jogo e guarde na chave 'nome' do molde_jogo:
    molde_jogo ['nome'] = str(input('Nome do jogo:'))
# Peça o input da plataforma (PC, PS5, etc) e guarde na chave 'plataforma' do molde_jogo:
    molde_jogo['plataforma'] = str(input('Qual a plataforma do  jogo?(PC,PS5,PS4:)'))
# 🚨 A HORA DA VERDADE: Dê um .append() na lista 'jogos_salvos'
# fazendo uma CÓPIA do 'molde_jogo' (Use o método .copy()!)
    jogos_salvos.append(molde_jogo.copy())


print('\n--- Listando os Jogos Cadastrados ---')
# 2. Agora, use um laço 'for' simples para exibir os jogos da lista bonitinho:
for jogo in jogos_salvos:
    print(f"Jogo: {jogo['nome']} | Plataforma: {jogo['plataforma']}")

print('\n' + '-=' * 20)