ordem_matriz = int(input())
matriz = []

# variáveis globais
contagem_dias = quarts_restaurados = quarts_destruidos = dias_sem_restaurar = 0
acabar = False
acabou_com_fim = False
mensagem = ''

# define cada linha da matriz com base na quantidade de elementos por linha
for i in range(ordem_matriz):
    linha = input()
    linha_matriz = linha.split(' ')
    matriz.append(linha_matriz)

linha_h = coluna_h = 0

# define inicialmente o ponto de partida do homem aranha ou se o quarteirão é destruído
for i in range(ordem_matriz):
    for j in range(ordem_matriz):
        if matriz[i][j] == 'H':
            linha_h = i
            coluna_h = j
        if matriz[i][j] == 'X':
            quarts_destruidos += 1

while not acabar:
    acao = input()
    mensagem = ''
    fora_do_range = False

    # condição de parada
    if acao == 'FIM':
        acabar = True
        acabou_com_fim = True

    else:
        contagem_dias += 1
        restaurou = False

        nova_linha = linha_h
        nova_coluna = coluna_h

        # o que fazer com cada ação
        if acao == 'Cima':
            nova_linha -= 1
        elif acao == 'Baixo':
            nova_linha += 1
        elif acao == 'Esquerda':
            nova_coluna -= 1
        elif acao == 'Direita':
            nova_coluna += 1
        
        # Verifica se o movimento é inválido
        if nova_linha < 0 or nova_linha >= ordem_matriz or nova_coluna < 0 or nova_coluna >= ordem_matriz or matriz[nova_linha][nova_coluna] == 'X':
            fora_do_range = True
            mensagem_range = "Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!"
            nova_linha = linha_h
            nova_coluna = coluna_h
        
        else: # verifica movimentos válidos
            matriz[linha_h][coluna_h] = '.'

            if matriz[nova_linha][nova_coluna] == 'E':
                matriz[nova_linha][nova_coluna] = 'H'
                restaurou = True
                quarts_restaurados += 1
                mensagem = 'O Miranha restaurou um quarteirão!'
                dias_sem_restaurar = 0
            
            else:
                matriz[nova_linha][nova_coluna] = 'H'
                dias_sem_restaurar += 1
            
        linha_h = nova_linha
        coluna_h = nova_coluna

        # Destruição após 3 dias sem restaurar
        if dias_sem_restaurar == 3:
            destruido = False
            for i in range(ordem_matriz):
                for j in range(ordem_matriz):
                    if not destruido and matriz[i][j] == 'E':
                        matriz[i][j] = 'X'
                        quarts_destruidos += 1
                        dias_sem_restaurar = 0
                        destruido = True
            # Se não encontrou nenhum E para destruir, apenas zera o contador
            if not destruido:
                dias_sem_restaurar = 0

        # Verificar se ainda há quarteirões corrompidos
        ainda_tem_E = False
        for i in range(ordem_matriz):
            for j in range(ordem_matriz):
                if matriz[i][j] == 'E':
                    ainda_tem_E = True

        # Imprimir estado do dia
        print(f'Dia {contagem_dias}')
        for i in range(ordem_matriz):
            print(' '.join(matriz[i]))
        print(f'Posição atual do Homem-Aranha: ({linha_h}, {coluna_h})')
        print(f'Quarteirões restaurados: {quarts_restaurados} | Quarteirões destruídos: {quarts_destruidos}')

        if mensagem != '':
            print(mensagem)
        else:
            if restaurou:
                print('O Miranha restaurou um quarteirão!')
            elif not restaurou and not fora_do_range:
                print('O Electro está ganhando espaço!')
            elif fora_do_range:
                print(mensagem_range)

        print()

    # Verificar vitória
    if not ainda_tem_E and quarts_restaurados > 0:
        print('Missão cumprida! Nova York está segura e o Miranha faz tudo novamente!')
        acabar = True

    # Verificar derrota por 7 dias
    if contagem_dias == 7 and ainda_tem_E:
        print('O Miranha não conseguiu restaurar a cidade a tempo, o Electro venceu!')
        acabar = True

    # Verificar derrota se FIM com E na cidade
    if acabou_com_fim and ainda_tem_E:
        print('Ainda existem quarteirões corrompidos! O Miranha não pode ir embora agora!')
        acabar = True
