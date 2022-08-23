print('=== Desafio 3 ===')
# um script python que leia dois números e devolva a soma
num1 = input('Primeiro número: ')
num2 = input('Segundo número: ')
sum = int(num1) + int(num2)
print('A soma entre {} e {} é {}'.format(num1, num2, sum))
# todo input é transformado em uma string, então você tem que expecificar pra fazer a soma correta
# usar format fica mais fácil na hora de escrever o código