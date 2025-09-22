cont = 0
p = input('Digite uma palavra: ')
for c in p:
    if c == 'a':
        cont += 1
if cont > 1:
    print(f'A palavra {p} possui {cont} letras a')
else:
    print(f'A palavra {p} possui {cont} letra a')