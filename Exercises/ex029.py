print('=== Desafio 29 ===')
v = int(input('Qual é a velocidade do carro? '))

if v <= 80:
    print('Você na velocidade certa')
else:
    print('''Você está acima da velocidade! \n Deve pagar uma multa de R${:.2F}'''.format((v - 80) * 7)) 

# esse foi de primeira amém irmãos