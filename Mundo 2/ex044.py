print('=== Desafio 44 ===')
# 10% de desconto a vista no dinheiro
# 5% de desconto a vista no cartão
# até 2x no cartão preço normal
# 3x ou mais 20% de juros

p = float(input('Preço das compras: R$'))
print('''Formas de Pagamento:
    [ 1 ] a vista no dinheiro
    [ 2 ] a vista no cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão
''')
o = int(input('Qual é a opção? '))

if o == 1:
    print ('Sua compra de R${:.2F} vai custar R${:.2F} no final'.format(p, p - 10 / 100))
elif o == 2:
    print ('Sua compra de R${:.2F} vai custar R${:.2F} no final'.format(p, p - 5 / 100))
elif o == 3:
    print ('Sua compra de R${:.2F} vai custar R${:.2F} no final'.format(p, p))
elif o == 4:
    pt = int(input('Quantas parcelas? '))
    print ('Sua compra de R${:.2F} será parcelada em R${:.2F} de {}x'.format(p, (p + (p * 20 / 100)) / pt, pt))
    print ('O valor subirá para R${}'.format(p + (p * 20 / 100)))
else:
    print('Inválido')
    
# problema com porcentagem de novo thumbs up ainda nao aprendi