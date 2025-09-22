l = input('Digite uma letra: ')
if len(l) == 1:
    if l in 'aeiou':
        print(f'{l} é uma vogal')
    elif l in 'bcdfghjklmnpqrstvwxyz':
        print(f'{l} é uma consoante')
    else:
        print('ERRO')
else:
    print('ERRO')
