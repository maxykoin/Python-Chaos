print('=== Desafio 33 ===')
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Primeiro Valor: '))
n2 = float(input('Segundo Valor: '))
n3 = float(input('Terceiro Valor: '))

m = n1
if n2 < n1 and n2 < n3:
    m = n2
if n3 < n2 and n3 < n1:
    m = n3

M = n1
if n2 > n1 and n2 > n3:
    M = n2
if n3 > n2 and n3 > n1:
    M = n3

print('O menor valor é {} \n E o maior valor é {}'.format(m, M))