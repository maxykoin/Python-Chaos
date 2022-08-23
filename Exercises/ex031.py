print('=== Desafio 31 ===')
n = float(input('Qual é a distância da sua viagem? '))

if n <= 200:
    print('O valor da viagem foi de R${:.2F}'.format(n * 0.50))
else:
    print('O valor da viagem foi de R${:.2F}'.format(n * 0.45))

# também foi de primeira amém as vezes minha lógica funciona