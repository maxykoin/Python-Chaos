nome = input('Qual é seu nome?')
idade = input('Qual é sua idade?')
peso = input('Qual é seu peso?')
print(nome, idade, peso)

print('=== Desafio 1 === ')
# um script python que leia o nome de uma pessoa e mostre uma mensagem de boas vindas com o nome dela
nome = input('Qual é seu nome?')
print('Bem vindo(a),', nome)
# vírgula espaço variável já deixa espaçado na promt quando + espaço não

print('=== Desafio 2 === ')
# um script python que leia o dia, mês e o ano do bnascimento de uma pessoa e devolva uma mensagem com a data formatada
dia = input('Qual é o dia do seu nascimento?')
mês = input('Qual é o mês do seu nascimento?')
ano = input('Qual é o ano que você nasceu?')
print('Você nasceu no dia', dia, 'do mês', mês, 'do ano de', ano + '. Correto?')
# pode misturar os dois

print('=== Desafio 3 === ')
# um script python que leia dois números e devolva a soma
num1 = input('Primeiro número')
num2 = input('Segundo número')
sum = int(num1) + int(num2)
print('A soma é', sum)
# em minha defesa eu nem sabia que tinha int em python