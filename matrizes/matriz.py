def soma_diagonal_secundaria(m):
    s = 0
    linhas = int(input('Número de linhas e colunas: '))
    for i in range(linhas):
        m.append([])
        for j in range(linhas):
            m[i] = (int(input(f'Elemento[{i}][{j}]: ')))
            if i == linhas - j - 1:
                s += m[i]
    return s
m1 = []
print(soma_diagonal_secundaria(m1))

def transposta_matriz(mt):
    t = []
    for j in range(len(mt[0])):
        t.append([])
        for i in range(len(mt)):
            t[j].append(mt[i][j])
    return t
m2 = [[1,4],[2,5],[3,6]]
print(transposta_matriz(m2))

def freq_nrs(mat):
    d = {}
    x = []
    for i in range(len(mat)):
        for j in (mat[i]):
            x.append(j)
    for c in x:
        cont = 0
        for k in x:
            if k == c:
                cont += 1
                d[c] = cont
    return d
m3 = [[1,2,3],[4,1,2],[1,5,3]]
print(freq_nrs(m3))

def maior_e_posicao(mtz):
    maior_valor = float('-inf')
    for i in range(len(mtz)):
        for j in range(len(mtz[i])):
            if mtz[i][j] > maior_valor:
                maior_valor = mtz[i][j]
                posicao = [i,j]
    return (maior_valor,posicao)
m4 = [[3,5,7],[1,6,9],[2,8,4]]
print(maior_e_posicao(m4))

def somar_bordas(mtr):
    soma = 0
    for i in range(len(mtr)):
        for j in range(len(mtr[i])):
            if i == 0 or i == len(mtr) - 1:
                soma += mtr[i][j]
            elif j == 0 or j == len(mtr) - 1:
                soma += mtr[i][j]
    return soma
m4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(somar_bordas(m4))
