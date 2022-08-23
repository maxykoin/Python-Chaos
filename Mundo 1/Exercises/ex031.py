print('=== Desafio 31 ===')
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule e peça o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R#0,45 para viagens mais longas.

n = float(input('Qual é a distância da sua viagem? '))

if n <= 200:
    print('O valor da viagem foi de R${:.2F}'.format(n * 0.50))
else:
    print('O valor da viagem foi de R${:.2F}'.format(n * 0.45))

# também foi de primeira amém as vezes minha lógica funciona