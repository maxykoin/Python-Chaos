print('=== Desafio 56 ===')

si = 0
mi = 0
Mi = 0
nv = 0
tm = 0

for p in range(1, 5):
    print('=== {}ª Pessoa ===',format(p))
    n = input('Nome: ').strip()
    i = int(input('Idade: '))
    s = input('Sexo (M/F): ').strip().upper()

    si += i 

    if p == 1 and s in 'M':
        Mi = i
        nv = n
    if s in 'M' and i > Mi:
        Mi = i
        nv = n
    if s in 'F' and i < 20:
        tm += 1

m = si / 4
print('A média de idade do grupo é de {:.2F}'.format(m))
print('O homem mais velho tem {} anos e se chama {}'.format(Mi, nv))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tm))

# understood it better now i think