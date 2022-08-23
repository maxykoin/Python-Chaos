print('=== Desafio 43 ===')
p = float(input('Qual é o seu peso (KG): '))
a = float(input('Qual é sua altura (m): '))

imc = p / (a * a)

if imc < 40 :
    print('Você está com obesidade grau III')
elif imc < 30:
    print('Você está com obesidade grau II')
elif imc < 25:
    print('Você está com sobrepeso')
elif imc < 19:
    print('Você está no peso ideal')
elif imc > 19:
    print('Você está abaixo do peso')

# eu errei boquinha de jacaré mlk