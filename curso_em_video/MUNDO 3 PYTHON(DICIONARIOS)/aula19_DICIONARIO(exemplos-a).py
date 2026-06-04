# Criamos um dicionário usando chaves {} com 3 pares de Chave:Valor
pessoas = {'nome': 'Washington', 'sexo': 'M', 'idade': 42}

# Mostra o dicionário completo na tela: {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)

# Acessa e mostra um valor específico usando o nome da chave entre colchetes
print(pessoas['nome']) # Saída: Washington
print(pessoas['idade']) # Saída: 42

# Print formatado usando aspas duplas na chave para não quebrar a f-string de aspas simples
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

# .keys() captura apenas os títulos/índices do dicionário (nome, sexo, idade)
print(pessoas.keys())

# .values() captura apenas os dados armazenados (Washington, M, 42)
print(pessoas.values())

# .items() captura as chaves e os valores juntos estruturados em duplas
print(pessoas.items())

# O laço 'for' usa duas variáveis (k para Key/Chave e v para Value/Valor)
# O .items() é obrigatório para o 'for' conseguir ler as duas coisas juntas
for k, v in pessoas.items():
    print(f'{k} = {v}')

# O comando 'del' apaga a chave 'sexo' e seu valor permanentemente
del pessoas['sexo']

# Substitui o valor da chave 'nome' de 'Gustavo' para 'Leandro'
pessoas['nome'] = 'Leandro'

# Adiciona um elemento totalmente novo (peso) apenas inventando a nova chave. Não usa .append()!
pessoas['peso'] = 98.5
print(pessoas)