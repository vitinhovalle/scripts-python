for c in range(0,5):
    if c == 0:
        num = int(input('Insira um número: '))
        menor = num
    elif c == 1:
        num = int(input('Insira outro número: '))
        if num < menor:
            segmenor = menor
            menor = num
        else:
            segmenor = num
    else:
        num = int(input('Insira outro número: '))
        if num < menor:
            segmenor = menor
            menor = num
        elif num >= menor and num < segmenor:
            segmenor = num
print(f'Menor número: {menor}')
print(f'Segundo menor número: {segmenor}')
