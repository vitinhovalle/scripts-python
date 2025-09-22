import random
def printArena(arena):
    for i in range(len(arena)):
        for j in range(len(arena[i])):
            print('{:^3}'.format(arena[i][j]), end='')
        print()
cont = acertos = 0
arena = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
while True:
    cord_i = random.randint(0, 4)
    cord_j = random.randint(0, 4)
    if arena[cord_i][cord_j] == 0:
        arena[cord_i][cord_j] = 1
        cont += 1
    if cont == 3:
        break
print()
printArena(arena)
while True:
    print()
    print('Escolha suas coordenadas')
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    linha -= 1
    coluna -= 1
    print()
    if arena[linha][coluna] == 0:
        print('Errou!!!')
        print()
        arena[linha][coluna] = 'x'
        printArena(arena)
    elif arena[linha][coluna] == 'x':
        print('Errar é humano, persistir no erro é burrice.')
        print()
        printArena(arena)
    elif arena[linha][coluna] == 1:
        acertos += 1
        arena[linha][coluna] = -1
        print('Na mosca!!')
        print()
        printArena(arena)
    elif arena[linha][coluna] == -1:
        print('Pare!! Ele já está morto!')
        print()
        printArena(arena)
    if acertos == 3:
        print('Parabéns! Todos os alvos foram destruidos')
        break
