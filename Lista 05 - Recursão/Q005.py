def caminho_recursivo(matriz, distancia, fila_prioridades):
    # fila de prioridades vazia
    if len(fila_prioridades) == 0:
        return

    infinito_arbitrario = 999999999

    # busca o item com menor custo nessa fila
    menor_custo = infinito_arbitrario
    index_melhor_item = -1 # index fora do range (também defini arbitrariamente)
    for i in range(len(fila_prioridades)):
        custo_atual = fila_prioridades[i][0]
        if custo_atual < menor_custo:
            menor_custo = custo_atual
            index_melhor_item = i
    
    if index_melhor_item != -1:
        # remove o item de menor custo da fila
        custo, linha, coluna = fila_prioridades.pop(index_melhor_item)

        # caminho mais curto já encontrado
        if custo > distancia[linha][coluna]:
            caminho_recursivo(matriz, distancia, fila_prioridades)
            return
        
        linhas_matriz = len(matriz)
        colunas_matriz = len(matriz[0])

        direcoes_possiveis = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for movimento_linha, movimento_coluna in direcoes_possiveis:
            nova_linha = movimento_linha + linha
            nova_coluna = movimento_coluna + coluna

            # verifica validade do movimento (dentro da matriz) e se o movimento não vai para uma barreira (célula de valor 0)
            if 0 <= nova_linha < linhas_matriz and 0 <= nova_coluna < colunas_matriz and matriz[nova_linha][nova_coluna] != 0:
                tipo_destino = matriz[nova_linha][nova_coluna]

                if tipo_destino == 3:
                    custo_movimento = 3
                else:
                    custo_movimento = 1

                novo_custo = custo + custo_movimento

                if novo_custo < distancia[nova_linha][nova_coluna]:
                    distancia[nova_linha][nova_coluna] = novo_custo
                    fila_prioridades.append((novo_custo, nova_linha, nova_coluna))
        
        if matriz[linha][coluna] == 2: # mesmo esquema do último loop
            for mov_linha, mov_coluna in direcoes_possiveis:
                # move duas casaas
                nova_linha, nova_coluna = linha + 2 * mov_linha, coluna + 2 * mov_coluna

                # verifica se o salto cai dentro da matriz e se o movimento não vai para uma barreira (célula de valor 0)
                if 0 <= nova_linha < linhas_matriz and 0 <= nova_coluna < colunas_matriz and matriz[nova_linha][nova_coluna] != 0:
                    custo_movimento = 1
                    novo_custo_total = custo + custo_movimento

                    if novo_custo_total < distancia[nova_linha][nova_coluna]:
                        distancia[nova_linha][nova_coluna] = novo_custo_total
                        fila_prioridades.append((novo_custo_total, nova_linha, nova_coluna))

    caminho_recursivo(matriz, distancia, fila_prioridades)

def dijkstra(matriz, linhas, colunas):
    infinito_arbitrario = 999999999
    
    distancias = []
    for i in range(linhas):
        linha_nova = []
        for j in range(colunas):
            linha_nova.append(infinito_arbitrario)
        distancias.append(linha_nova)

    distancias[0][0] = 0
    fila_prioridade = [[0, 0, 0]] # ponto de partida

    caminho_recursivo(matriz, distancias, fila_prioridade)

    destino_final = distancias[linhas - 1][colunas - 1]

    if destino_final == infinito_arbitrario:
        return 0, False
    else:
        return destino_final, True

linhas = int(input())
colunas = int(input())

matriz = []

# cria a matriz e já transforma os valores internos da matriz em tipo inteiro
for i in range(linhas):
    valores_linha = input().split(' ')
    matriz.append(valores_linha)

    for j in range(colunas):
        matriz[i][j] = int(matriz[i][j])

# outputs iniciais
print("=== SEKIRO: O RESGATE DE CESAR ===\nWolf deve resgatar CESAR!")

# realiza o algorimo de djikstra
movimentos, conseguiu = dijkstra(matriz, linhas, colunas)

# outputs finais
if not conseguiu:
    print("MORTE! Wolf não conseguiu resgatar Cesar... ele nunca saberá quem venceu Satoru Gojo ou Sukuna!")
else:
    print(f"SUCESSO! Wolf resgatou o Cesar em {movimentos} movimentos!")

    if movimentos <= 4:
        print("PERFEITO! Verdadeiro Shinobi! Cesar está ORGULHOSO!!")
    elif movimentos < 8:
        print("BOM! Caminho eficiente! Mas você quase decepcionou Cesar")
    else:
        print("Wolf chegou, mas pode melhorar... Cesar está decepcionado, quase morreu de tédio!")
