print('=== Desafio 41 ===')
n = int(input('Ano de nascimento: '))

if 2022 - n <= 9:
    print('Você é um atleta mirim')
elif 2022 - n <= 14:
    print('Você é um atleta infantil')
elif 2022 - n <= 19:
    print('Você é um atleta junior')
elif 2022 - n <= 25:
    print('Você é um atleta sênior')
elif 2022 - n > 25:
    print('Você é um atleta master')