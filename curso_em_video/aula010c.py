n1 = float(input('digite uma nota de 0 a 10: '))
n2 =float(input('digite uma nota de 0 a 10: '))
media = (n1+n2)/2
print('sua nota foi {:.1f}'.format(media))
if media >= 7:
    print('aprovado')
else:
    print('reprovado')
