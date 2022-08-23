print('=== Desafio 22 ===')
n = input('Qual é seu nome inteiro: ')
s = n.split()
print('O seu nome em maiúsculas é {}. \n O seu nome em minúsculas é {}. \n Seu nome ao todo tem {} letras. \n Seu primeiro nome é {} e tem {} letras.'.format(n.upper(), n.lower(), len(n), s[0], len(s[0])))
# um pouco de problema na hora de fazer o split e pegar o número de letras da lista/array 