p = 0
n = int(input('Insira um número: '))
if n > 0:
    for c in range(1,n):
        if n % c == 0:
            p += c
    if p == n:
        print('Número perfeito!')
    else:
        print('Não é um número perfeito!')
