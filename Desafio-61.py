print('Gerador de PA')
print('='* 10)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = n1
cont = 1
while cont <= 10:
    print('{} ⇾ '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')