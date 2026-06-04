lanche = ['hamburguer','suco','pizza','pudim']
print(f'Lista original {[lanche]}')
lanche.append('picole') # (.append(picole))  adiciona no final da lista um picolé
print(f'Lista com o picolé adicionado {[lanche]}')
lanche.insert(0,'cachorro') # (.insert(cachorro)) adiciona o objeto em qualquer posição
print(f'Lista com o cachorro adicionado na posição 0 {[lanche]}')
print(f'lista com o item {lanche.pop(0)} removido da posição 0')
print(f'Lista original {[lanche]}')
lanche.remove('picole')
print(f'lista com {[lanche]} com picolé removido')
del lanche[3]
print(f'Lista com {[lanche]} com pudim removido')
lanche.sort()
print(lanche)
lanche.sort(reverse=True)
print(lanche)
print(f'essa lista tem {len(lanche)} lanches')


