p = 0
x = int(input('Insira um número: '))
y = int(input('Insira outro número: '))
if x < y:
    for c in range (x,y + 1):
        if c % 2 == 0:
            p += 1
else:
    for c in range (y,x + 1):
        if c % 2 == 0:
            p += 1
if p > 1:
    print(f'No intervalo entre {x} e {y} existem {p} números pares')
else:
    print(f'No intervalo entre {x} e {y} existe {p} número par')
