lanche = 'hamburguer', 'suco', 'pizza', 'pudim' #variavel composta
print(lanche[0])
print(lanche[-4])
print(lanche[-4:0])
print(lanche[-4:4])
print('*'*20)
for pos, comida in enumerate(lanche):
    print(comida)
print('#='*20)
  #Tuplas são imutaveis
'''lanche [1] = 'beige'
print(lanche[1]) # -> deu erro'''
for comida in lanche:
    print(comida)
print('#='*20)
for c in range(0, len(lanche)):
    print(lanche[c])
print('#='*20)
for pos, comida in enumerate(lanche):
    print(f' Eu vou comer {comida} na posição {pos}')
print('comi pra caramba')


