estilos = [0, 1, 4, 7]

for estilo in estilos:
    print(f'\n==== ESTILO {estilo} ====\n')

    for texto in range(30, 38):
        for fundo in range(40, 48):
            codigo = f'{estilo};{texto};{fundo}'
            print(f'\033[{codigo}m{codigo} -> Olá Mundo!!!\033[m')