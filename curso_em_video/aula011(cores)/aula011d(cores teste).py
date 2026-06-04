cores = {
    'limpa': '\033[m',
    'erro': '\033[1;31m',
    'sucesso': '\033[32m',
    'alerta': '\033[33m'
}
usuario = input('Usuário: ')
senha = input('Senha: ')

if usuario == 'admin' and senha == '123':
    print(cores['sucesso'] + 'Login realizado com sucesso!' + cores['limpa'])
else:
    print(cores['erro'] + 'Usuário ou senha inválidos!' + cores['limpa'])