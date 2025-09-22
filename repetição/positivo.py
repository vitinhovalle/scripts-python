p = 0
n = 0
x = 1
while x != 0:
    x = int(input('Digite um número: '))
    if x > 0:
        p += 1
    elif x < 0:
        n += 1
print()
print(f'Números positivos: {p}')
print(f'Números negativos: {n}')
