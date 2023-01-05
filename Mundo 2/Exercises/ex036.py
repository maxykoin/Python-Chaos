print('=== Desafio 36 ===')
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o sálario do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

v = float(input('Qual é o valor da casa: R$'))
s = float(input('Qual é sua renda mensal: R$'))
a = int(input('Em quanto anos você espera pagar a casa: '))

print('Para pagar uma casa de R${:.2F} em {} anos, a prestação será de R${:.2F}'.format(v, a, v / (a * 12)))

if v / (a * 12) >= s * 30 /100:
    print('Seu empréstimo foi negado')
else:
    print('Seu empréstimo foi aceito')

# metemática /neg
# eu achei que ia ter nested if por isso fiquei confuso