# implementação do algoritmo muito parecida com a da questão anterior
def busca_recursiva(mapa, custos, dist_passos, custos_res, predecessores, fila):
    # fila de prioridades vazia
    if len(fila) == 0:
        return
    
    infinito_arbitrario = 999999999

    # busca o item com menor custo nessa fila
    menor_custo = infinito_arbitrario
    melhor_idx = -1 # index fora do range (também defini arbitrariamente)
    for i in range(len(fila)):
        if fila[i][0] < menor_custo:
            menor_custo = fila[i][0]
            melhor_idx = i
    
    # remove o item de menor custo da fila
    res_gasta, passos, linha, col = fila.pop(melhor_idx)

    # caminho mais curto já encontrado
    if res_gasta > custos_res[linha][col]:
        busca_recursiva(mapa, custos, dist_passos, custos_res, predecessores, fila)
        return
        
    linhas_mapa = len(mapa)
    colunas_mapa = len(mapa[0])

    movimentos = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for movimento_linha, movimento_coluna in movimentos:
        nova_linha = linha + movimento_linha
        nova_coluna = col + movimento_coluna

        # verifica validade do movimento (dentro da matriz) e se não existe uma # na nova posição
        if 0 <= nova_linha < linhas_mapa and 0 <= nova_coluna < colunas_mapa and mapa[nova_linha][nova_coluna] != '#':
            caracter_destino = mapa[nova_linha][nova_coluna]
            custo_passo = custos[0]
            if caracter_destino == 'T':
                custo_passo = custos[1]
            elif caracter_destino == 'E':
                custo_passo = custos[2]

            novos_passos = passos + 1
            nova_res_gasta = res_gasta + custo_passo

            if nova_res_gasta < custos_res[nova_linha][nova_coluna]:
                dist_passos[nova_linha][nova_coluna] = novos_passos
                custos_res[nova_linha][nova_coluna] = nova_res_gasta
                predecessores[nova_linha][nova_coluna] = [linha, col]
                fila.append([nova_res_gasta, novos_passos, nova_linha, nova_coluna])

    busca_recursiva(mapa, custos, dist_passos, custos_res, predecessores, fila)

def encontrar_caminho(mapa, custos, inicio, fim, linhas, colunas):
    infinito_arbitrario = 999999999
    movimento_invalido = [-1, -1]
    
    dist_passos = []
    for a in range(linhas):
        dist_passos.append([infinito_arbitrario] * colunas)

    custos_res = []
    for b in range(linhas):
        custos_res.append([infinito_arbitrario] * colunas)

    caminho_anterior = []
    for c in range(linhas):
        caminho_anterior.append([movimento_invalido] * colunas)

    inicio_l, inicio_c = inicio
    dist_passos[inicio_l][inicio_c] = 0
    custos_res[inicio_l][inicio_c] = 0
    
    fila = [[0, 0, inicio_l, inicio_c]] # [custo_rest, passos, linha, coluna]
    busca_recursiva(mapa, custos, dist_passos, custos_res, caminho_anterior, fila)

    fim_l, fim_c = fim
    custo_final = custos_res[fim_l][fim_c]

    if custo_final == infinito_arbitrario:
        return infinito_arbitrario, []
    
    caminho = []
    atual = fim
    while atual != movimento_invalido:
        caminho.append(atual)
        atual = caminho_anterior[atual[0]][atual[1]]
    caminho.reverse()

    if caminho and caminho[0] == inicio:
        return custo_final, caminho
    return infinito_arbitrario, []

def formatar_caminho(caminho):
    partes_do_caminho = []
    for linha, coluna in caminho:
        texto_da_coordenada = f"({coluna},{linha})"
        partes_do_caminho.append(texto_da_coordenada)
    return " -> ".join(partes_do_caminho)

# bloco principal do código
entrada_dimensoes = input().split(' ')
linhas = int(entrada_dimensoes[0])
colunas = int(entrada_dimensoes[1])

mapa = []
for i in range(linhas):
    linha_mapa = input()
    mapa.append(linha_mapa)

res_maxima = int(input())

entrada_custos_str = input().split(' ')
custos = []
for custo_str in entrada_custos_str:
    custos.append(int(custo_str))

pacto_reviver = int(input())
if pacto_reviver == 1:
    reviver = True
else:
    reviver = False

infinito_arbitrario = 999999999
movimento_invalido = [-1, -1]

# posições S, K, e G no mapa
pos_s, pos_k, pos_g = movimento_invalido, movimento_invalido, movimento_invalido
for r in range(linhas):
    for c in range(colunas):
        if mapa[r][c] == 'S':
            pos_s = [r, c]
        elif mapa[r][c] == 'K':
            pos_k = [r, c]
        elif mapa[r][c] == 'G':
            pos_g = [r, c]

# caminho de S até K
caminhos_combinados = []
custo_S_K, caminho_S_K = encontrar_caminho(mapa, custos, pos_s, pos_k, linhas, colunas)

if not caminho_S_K:
    print("A escuridão sussurra derrota... Não há caminho.")
elif custo_S_K > res_maxima:
    print("A alma definha... Resistencia esgotada.")
else:
    # caminho de K até G
    res_restante = res_maxima - custo_S_K
    custo_K_G, caminho_K_G = encontrar_caminho(mapa, custos, pos_k, pos_g, linhas, colunas)

    if not caminho_K_G:
        print("A escuridão sussurra derrota... Não há caminho.")
    elif custo_K_G <= res_restante:
        print("Lamina Profanada recuperada! Altar alcançado!")
        print(f"Custo total de Resistencia: {custo_S_K + custo_K_G}")
        print("Caminho:")
        caminho_s_k_str = formatar_caminho(caminho_S_K)
        caminho_k_g_str = formatar_caminho(caminho_K_G[1:])
        print(f"{caminho_s_k_str} -> {caminho_k_g_str}")
        
        caminhos_combinados = [caminho_S_K, caminho_K_G]
    else:
        if reviver:
            custo_revivido, caminho_revivido = encontrar_caminho(mapa, custos, pos_s, pos_g, linhas, colunas)
            if not caminho_revivido or custo_revivido > res_maxima: # se o reviver deu errado
                print("Mesmo renascido das cinzas, o destino era a derrota.")
                caminhos_combinados = []
            else:
                # reviver deu certo
                print("Com a ajuda dos deuses antigos, o altar foi alcançado!")
                print(f"Custo total de Resistencia: {custo_revivido}")
                print("Caminho:")
                print(formatar_caminho(caminho_S_K))
                print("...revivido das cinzas em S...")
                print(formatar_caminho(caminho_revivido))
                
                caminhos_combinados = [caminho_S_K, caminho_revivido]
        else:
            print("A alma definha... Resistencia esgotada.")
            caminhos_combinados = []

if caminhos_combinados:
    mapa_vis = []
    for i in range(linhas):
        nova_linha = ['#'] * colunas
        mapa_vis.append(nova_linha)

    pontos_trajeto = []
    for caminho in caminhos_combinados:
        for ponto in caminho:
            if ponto not in pontos_trajeto:
                pontos_trajeto.append(ponto)

    for r, c in pontos_trajeto:
        mapa_vis[r][c] = '*'
    
    mapa_vis[pos_s[0]][pos_s[1]] = 'S'
    mapa_vis[pos_k[0]][pos_k[1]] = 'K'
    mapa_vis[pos_g[0]][pos_g[1]] = 'G'
    
    print("Visualização do Caminho:")
    for linha in mapa_vis:
        print("".join(linha))
