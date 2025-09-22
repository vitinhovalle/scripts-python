s = 0
a = int(input('Insira um número: '))
b = int(input('Insira outro número: '))
if a >= b:
    print('Cálculo não será realizado')
else:
    for c in range(a + 1, b):
        if c > 0:
            s += c**3
    print(f'A soma dos cubos dos números inteiros positivos entre {a} e {b} é {s}')
