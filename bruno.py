fixo = 1643
print(f'Valor fixo: {fixo}')
fator = (input('Digite um fator para ser calculado: '))
fator = float(fator.replace(',','.'))
if fator >= 0.0001 and fator <= 9.9999:
    r = (f'{round((fixo * fator),2)}')
    r = r.replace('.',',')
    fator = round((fator * 100),2)
    f = (f'{fator}')
    f = f.replace('.',',')
    print(f'Valor da franquia: R${r}')
    print(f'{f}% da obrigatória')
else:
    print('ERRO. Tente novamente')
