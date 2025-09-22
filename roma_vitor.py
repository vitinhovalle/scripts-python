import random
cont = acertos = 0
# matriz base
arena = [[0,0,0,0,0],[0,0,0,0,0],
         [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# sorteio das coordenadas 
while True:
    i = random.randint(0,4)
    j = random.randint(0,4)
    if arena[i][j] == 0:
        arena[i][j] = 1
        cont += 1
    if cont == 3:
        break
# arena inicial
for i in range(5):
    for elemento in arena[i]:
        print(f'{elemento:^3}',end='')
    print()
while True:
    # tentativas
    print(f'Tentativa {cont - 2}')
    cont += 1
    print('Escolha suas coordenadas')
    i = int(input('Linha: '))
    j = int(input('Coluna: '))
    # checagem das coordenadas
    if arena[i][j] == 1:
        acertos += 1
        print()
        print('Acertou!!')
        arena[i][j] = -1
        for i in range(5):
            for elemento in arena[i]:
                print(f'{elemento:^3}',end='')
            print()
    elif arena[i][j] == 0:
        print()
        print('Parabéns, você matou inocentes!')
        arena[i][j] = 'X'
        for i in range(5):
            for elemento in arena[i]:
                print(f'{elemento:^3}',end='')
            print()
    elif arena[i][j] == 'X':
        print()
        print('Eu tô com medo de você. Sério.')
        for i in range(5):
            for elemento in arena[i]:
                print(f'{elemento:^3}',end='')
            print()
    elif arena[i][j] == -1:
        print()
        print('Só pra garantir, né?')
        for i in range(5):
            for elemento in arena[i]:
                print(f'{elemento:^3}',end='')
            print()
    if acertos == 3:
        print('Parabéns, você venceu!')
        break
