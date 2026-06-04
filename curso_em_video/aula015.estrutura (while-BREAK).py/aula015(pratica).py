n = cont = soma =    0
while True:
    n = int(input('Digite um numero: '))
    if n == 0:
        break
    soma += n
    cont += 1
print(f'a soma {soma}')
