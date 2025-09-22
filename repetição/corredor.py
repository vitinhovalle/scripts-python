maiorv = 0
maiord = 0
for c in range(0,5):
    id = int(input('Número de identificação: '))
    vm = int(input('Velocidade média(km/h): '))
    dt = int(input('Distância total(km): '))
    if vm > maiorv:
        maiorv = vm
        idenvm = id
    if dt > maiord:
        maiord = dt
        vmaiord = vm
        idendt = id
print(f'Maior distância - id:{idendt}, vm:{vmaiord}km/h')
print(f'Mais rápido - id:{idenvm}, vm:{maiorv}km/h')
