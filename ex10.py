m = 0
h = 0
cont = 0
while True:
    n = input('Nome: ')
    a = float(input('Altura: '))
    if a < 0:
        break
    elif a > m:
        m = a
    i = int(input('Idade: '))
    print()
    if i > 30:
        h += a
        cont += 1
print(f'Maior altura: {m}')
if cont > 0:
    print(f'Média de altura 31+: {round((h/cont),2)}')
elif cont == 0:
    print(f'Média de altura 31+: 0')
