def lista_comuns(a, b):
    l3 = []
    comuns = []
    l3 = a + b
    posicao = 1
    for i in l3:
        cont = 0
        if posicao == len(l3) - 1:
            break
        for j in range(posicao, len(l3)):
            if l3[j] == i:
                cont += 1
                comuns.append(i)
        posicao += 1
    return comuns

def numeros_pares(lista):
    d = {}
    for c in lista:
        if c % 2 == 0:
            d[c] = 3 * c
    return d

def reversa_lista(lista):
    reversa = []
    for c in range(len(lista) - 1, -1, -1):
        reversa.append(lista[c])
    return reversa

def somar_fora_diagonais(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range (len(matriz)):
            if i != j:
                soma += matriz[i][j]
    return soma
