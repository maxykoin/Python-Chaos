print('=== Desafio 66 ===')
i = s = 0 
n = int(input('Digite um valor (999 para parar): '))

# while n != 999:
#    s += n
#    i += 1
#    n = int(input('Digite um valor (999 para parar): '))
# print('A soma dos {} valores foi {}!'.format(i, s))

# getting used to += and how to add on loops 

while True:
    if n == 999:
        break
    s += n
    i += 1
    n = int(input('Digite um valor (999 para parar): '))
print('A soma dos {} valores foi {}!'.format(i, s))