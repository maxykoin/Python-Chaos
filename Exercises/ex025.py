print('=== Desafio 25 ===')
n = input('Qual é seu nome completo: ').strip().lower()
# i keep thinking like are there any means to count the whitespaces
# in a string to say anything after this white space is a surname
print('Seu nome tem Silva? ', 'silva' in n)
# caralho então tem como usar o in assim
# queria ter usado no último mas ele só aparecia em if