print('=== Desafio 39 ===')
# 

n = int(input('Ano de nascimento: '))

if 2022 - n == 18:
    print('''
        Quem nasceu em {} tem {} anos em 2022
        Você deve se alistar esse ano
     '''.format(n, 2022-n))
elif 2022 - n > 18:
    print('''
        Quem nasceu em {} tem {} anos em 2022
        Você já deveria ter se alistado à {} anos
    '''.format(n, 2022 - n, abs(18 - (2022 - n))))
elif 2022 - n < 18:
    print('''
        Quem nasceu em {} tem {} anos em 2022
        Você vai se alistar em {} anos
    '''.format(n, 2022 - n, abs(18 - (2022 - n))))

# "how to make a number go from negative to positive in python" my exact google search
# easy just took some time to format the prints
# learn abs()