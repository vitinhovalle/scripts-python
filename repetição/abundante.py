somadiv = 0
num = int(input('Digite um número: '))
if num < 0:
    print('Erro')
else:
    for c in range(1,num):
        if num % c == 0:
            somadiv += c
    if somadiv > num:
        print('Número abundante!')
    else:
        print('Não é um número abundante!')
