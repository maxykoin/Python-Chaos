print('=== Desafio 40 ===')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

if (n1 + n2) / 2 < 5:
    print('Com a nota {} e {}, o aluno fica com a média {} e está reprovado'.format(n1, n2, (n1 + n2) / 2))
elif 7 > (n1 + n2) / 2 >= 5:
    print('Com a nota {} e {}, o aluno fica com a média {} e está de recuperação'.format(n1, n2, (n1 + n2) / 2))
elif (n1 + n2) / 2 >= 7:
    print('Com a nota {} e {}, o aluno fica com a média {} e está aprovado'.format(n1, n2, (n1 + n2) / 2))

# did this w my grades before
# had a bit of trouble on the syntax of the second ilif (put it as (n1 + n2) / 2 >= 5 < 7 at first) 