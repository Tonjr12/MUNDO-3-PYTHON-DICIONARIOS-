# 1. Criamos um dicionário chamado 'pessoas' usando chaves {}.
# 'nome', 'sexo' e 'idade' são as CHAVES (Keys). 'Ton', 'Masculino' e '42' são os VALORES (Values).
pessoas = {'nome':'Ton','sexo':'Masculino','idade':'42'}

# 2. Mostra o dicionário inteiro na consola com a estrutura completa.
print(pessoas)

# 3. Print estético: Cria uma linha divisória com 60 asteriscos na consola.
print('*'*60)

# 4. Acessa e mostra especificamente o VALOR que está guardado dentro da chave 'nome' (vai mostrar: Ton).
print(pessoas['nome'])

print('*'*60)

# 5. O comando .keys() pega e mostra apenas os nomes das chaves: ['nome', 'sexo', 'idade'].
print(pessoas.keys())

print('*'*60)

# 6. O comando .values() pega e mostra apenas os dados guardados dentro das chaves: ['Ton', 'Masculino', '42'].
print(pessoas.values())

print('*'*60)

# 7. O comando .items() pega e mostra o conjunto completo (Chave e Valor juntos), organizados em Tuplas.
print(pessoas.items())

print('*'*60)

# 8. Três prints seguidos mostrando os valores individuais de cada chave na consola, um por linha.
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])

print('*'*60)

# 9. Uma f-string formatando os dados numa frase.
# 🚨 ATENÇÃO: Como usamos aspas simples para abrir o print f'...', as chaves do dicionário precisam usar aspas DUPLAS ["nome"] para o Python não se confundir!
print(f'Nome:{pessoas["nome"]}/ Sexo:{pessoas["sexo"]}/ idade:{pessoas["idade"]},anos')

print('*'*60)

# 10. O comando 'del' apaga permanentemente a chave 'nome' e o valor 'Ton' de dentro do dicionário.
del pessoas['nome']

# 11. Para percorrer dicionários com o 'for', usamos duas variáveis: uma para a chave (k) e outra para o valor (v).
# É obrigatório usar o .items() no final para o Python conseguir ler ambos ao mesmo tempo!
for k, v in pessoas.items():
    print(f'{k} = {v}') # Vai printar na consola: sexo = Masculino / idade = 42 (repare que o nome sumiu!)

# 12. Adicionando ou modificando dados: Como a chave 'nome' não existia mais (foi deletada),
# esta linha cria novamente a chave 'nome' e joga o valor 'Isaac' lá dentro.
pessoas ['nome'] = 'Isaac'

# 13. Mostra o dicionário atualizado na consola com o novo nome inserido.
print(pessoas)

# 14. Outro laço 'for' para listar os itens atualizados após a inserção do 'Isaac'.
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('*'*60)

# 15. Uma das maiores vantagens do dicionário: Para adicionar um elemento totalmente NOVO,
# você NÃO usa .append()! Basta inventar uma chave nova entre colchetes (ex: 'peso') e atribuir um valor.
pessoas ['peso'] = 98.5

# 16. Mostra o dicionário completo na consola, agora contendo também o peso.
print(pessoas)

# 17. O último laço 'for' mostrando a estrutura final com todas as chaves e valores na consola.
for k, v in pessoas.items():
    print(f'{k} = {v}')