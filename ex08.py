f = input('Digite uma frase: ')
if f.count(' ') < 1:
    print(f'Esta frase tem {f.count(' ') + 1} palavra')
else:
    print(f'Esta frase tem {f.count(' ') + 1} palavras')
