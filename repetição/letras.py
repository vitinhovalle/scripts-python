s = input('Digite uma string: ')
n = 0
for c in range(0, len(s) - 1):
    if s.count(s[c]) > 1:
        if s[c].isalpha() == True:
            print(f'{s} possui letras repetidas')
            n = 0
            break
        else:
            n = 1
    else:
        n = 1
if n == 1:
    print(f'{s} não possui letras repetidas')