s = 0
f = input('Digite uma frase: ')
v = 'aeiou'
for c in range (0,5):
    s += f.count(v[c])
print(f'A frase possui {s} vogais')
