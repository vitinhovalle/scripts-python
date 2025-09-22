n = int(input('Digite um número: '))
s = 0
if n >= 1:
    for c in range(1,n + 1):
        s += c
    print(f'A soma de 1 até {n} é {s}')
else:
    for c in range(n,2):
        s += c
    print(f'A soma de 1 até {n} é {s}')
