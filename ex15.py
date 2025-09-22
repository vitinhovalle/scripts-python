x = 1
s = input('Digite uma string: ')
if s.isalpha():
    for c in range(0,len(s) - 1):
        d = ord(s[c + 1]) - ord(s[c])
        if d < 3 and d > -3:
            print('Condição não satisfeita')
            x = 0
            break
else:
    print('ERRO')
if x == 1:
    print('Condição satisfeita')
