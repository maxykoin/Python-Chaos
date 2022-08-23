print('=== Desafio 35 ===')
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# how do I even I don't even know what this means
 
n1 = float(input('Primeiro Seguimento: '))
n2 = float(input('Segundo Seguimento: '))
n3 = float(input('Terceiro Seguimento: '))

# cada um dos seguimentos tem que ser menor do que a soma dos outros dois para formar um triângulo

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os seguimentos acima podem formar um triângulo')
else:
    print('Os seguimentos acima não podem formar um triângulo')

# first try babyyy