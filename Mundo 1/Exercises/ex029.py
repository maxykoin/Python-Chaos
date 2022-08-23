print('=== Desafio 29 ===')
# Escreva um programa que leia a velocidade de um carro. -Se ele ultrapassar 80Km/, mostre uma mensagem dizendo
# que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual é a velocidade do carro? '))

if v <= 80:
    print('Você na velocidade certa')
else:
    print('''Você está acima da velocidade! \n Deve pagar uma multa de R${:.2F}'''.format((v - 80) * 7)) 

# esse foi de primeira amém irmãos