print('=== Desafio 57 ===')

s = input('Qual é seu sexo? (M/F): ').upper()

while s != 'M' or s != 'F':
    s = input('Digite novamente (M/F) Qual é seu sexo? (M/F): ').upper()

    if s == 'M' or s == 'F':
        print('Sexo {} registrado com sucesso'.format(s))
        break

# loops <3 so easy bc of arduino 