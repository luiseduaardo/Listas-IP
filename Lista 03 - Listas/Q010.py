# leitura da matriz
tamanho = input()
tamanho_dividido = tamanho.split('x')

linhas = int(tamanho_dividido[0])
colunas = int(tamanho_dividido[1])

somador = 0
matriz = []

for i in range(linhas):
    valor = input()
    valores_separados = valor.split(' ')
    for j in range(colunas):
        if valores_separados[j].isdigit():
            valores_separados[j] = int(valores_separados[j])
            somador += valores_separados[j]
    matriz.append(valores_separados)

# transpõe caso a soma seja par
if somador % 2 == 0:
    matriz_transposta = []
    for i in range(colunas):
        linha_nova = []
        for j in range(linhas):
            linha_nova.append(matriz[j][i])
        matriz_transposta.append(linha_nova)
    matriz = matriz_transposta
    linhas, colunas = colunas, linhas

# leitura das energias das personagens
energia_florzinha = int(input())
energia_lindinha = int(input())
energia_docinho = int(input())

# identifica posição de cada personagem na matriz
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == 'F':
            lf = i
            cf = j
        elif matriz[i][j] == 'L':
            ll = i
            cl = j
        elif matriz[i][j] == 'D':
            ld = i
            cd = j
        elif matriz[i][j] == 'M':
            lm = i
            cm = j

# flags de controle dos loops
capturado = False
vencedora = ''
jogo_ativo = True

# Loop principal
while jogo_ativo:
    pode_andar_geral = False

    # direções de movimentação possíveis - cima, baixo, esquerda, direita
    direcoes = [[-1,0],[1,0],[0,-1],[0,1]]

    # turno florzinha
    opcoes = []
    for d in direcoes:
        nl = lf + d[0]
        nc = cf + d[1]
        if 0 <= nl < linhas and 0 <= nc < colunas:
            celula = matriz[nl][nc]
            if celula != 'L' and celula != 'D' and celula != 0:
                custo = celula if type(celula) == int else 0
                if energia_florzinha >= custo:
                    dist = abs(nl - lm) + abs(nc - cm)
                    opcoes.append([dist, custo, nl, nc])
    if len(opcoes) > 0:
        pode_andar_geral = True
        opcoes.sort()
        matriz[lf][cf] = 0
        lf = opcoes[0][2]
        cf = opcoes[0][3]
        energia_florzinha -= opcoes[0][1]
        if lf == lm and cf == cm:
            capturado = True
            vencedora = 'F'
            matriz[lf][cf] = 'F'
            jogo_ativo = False
        else:
            matriz[lf][cf] = 'F'

    # turno lindinha
    if jogo_ativo:
        opcoes = []
        for d in direcoes:
            nl = ll + d[0]
            nc = cl + d[1]
            if 0 <= nl < linhas and 0 <= nc < colunas:
                celula = matriz[nl][nc]
                if celula != 'F' and celula != 'D' and celula != 0:
                    custo = celula if type(celula) == int else 0
                    if energia_lindinha >= custo:
                        dist = abs(nl - lm) + abs(nc - cm)
                        opcoes.append([dist, custo, nl, nc])
        if len(opcoes) > 0:
            pode_andar_geral = True
            opcoes.sort()
            matriz[ll][cl] = 0
            ll = opcoes[0][2]
            cl = opcoes[0][3]
            energia_lindinha -= opcoes[0][1]
            if ll == lm and cl == cm:
                capturado = True
                vencedora = 'L'
                matriz[ll][cl] = 'L'
                jogo_ativo = False
            else:
                matriz[ll][cl] = 'L'

    # turno docinho
    if jogo_ativo:
        opcoes = []
        for d in direcoes:
            nl = ld + d[0]
            nc = cd + d[1]
            if 0 <= nl < linhas and 0 <= nc < colunas:
                celula = matriz[nl][nc]
                if celula != 'F' and celula != 'L' and celula != 0:
                    custo = celula if type(celula) == int else 0
                    if energia_docinho >= custo:
                        dist = abs(nl - lm) + abs(nc - cm)
                        opcoes.append([dist, custo, nl, nc])
        if len(opcoes) > 0:
            pode_andar_geral = True
            opcoes.sort()
            matriz[ld][cd] = 0
            ld = opcoes[0][2]
            cd = opcoes[0][3]
            energia_docinho -= opcoes[0][1]
            if ld == lm and cd == cm:
                capturado = True
                vencedora = 'D'
                matriz[ld][cd] = 'D'
                jogo_ativo = False
            else:
                matriz[ld][cd] = 'D'

    # verifica se ainda pode andar
    if not pode_andar_geral and jogo_ativo:
        jogo_ativo = False

# outputs
if capturado:
    if vencedora == 'F':
        print('Florzinha usou sua inteligência e capturou o Macaco Louco com um plano perfeito!')
    elif vencedora == 'L':
        print('Lindinha, com coragem e coração, chegou primeiro e prendeu o Macaco Louco!')
    elif vencedora == 'D':
        print('Docinho não deu chance: partiu pra cima e derrotou o Macaco Louco com atitude!')

    print('Situação final da cidade de Townsville após a batalha:')
    for i in range(linhas):
        print(' '.join(str(x) for x in matriz[i]))

    print('E assim, mais uma vez, AS MENINAS SUPERPODEROSAS salvaram o dia!')

else:
    print('O Macaco Louco escapou! As Meninas não conseguiram alcançá-lo a tempo…')
