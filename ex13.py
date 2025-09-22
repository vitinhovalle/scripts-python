n = int(input('Insira um número: '))
m = n
for c in range (0,3):
     n = int(input('Insira outro número: '))
     if n > m:
        m = n
print(f'{m} é o maior número')
