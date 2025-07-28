def calcular_pontos_jogador(lista_infos):
    posicao = lista_infos[1]
    gols_feitos = int(lista_infos[2])
    assistencias = int(lista_infos[3])
    amarelos = int(lista_infos[4])
    vermelhos = int(lista_infos[5])
    gols_sofridos = int(lista_infos[6])

    pontuacao = (8 * gols_feitos) + (5 * assistencias) + ((-1) * amarelos) + ((-3) * vermelhos)

    if (posicao == 'goleiro' or posicao == 'zagueiro' or posicao == 'lateral') and gols_sofridos == 0:
        pontuacao += 5

    jogador_dict = {f'{lista_infos[0]}': {'posicao': f'{lista_infos[1]}',
                                        'pontuacao': pontuacao}}
    
    return jogador_dict

# bloco principal de código

qtd_tecnicos = int(input())
todos_os_tecnicos = {}

for i in range(qtd_tecnicos):
    nome_tecnico = input()
    titulares = {}
    reservas = {}

    for l in range(2):
        comando = input()
        if comando == 'titulares':
            for j in range(11):
                jogador = input().split(',')

                dicionario_jogador = calcular_pontos_jogador(jogador)

                titulares.update(dicionario_jogador)

        elif comando == 'reservas':
            for k in range(5):
                jogador = input().split(',')

                dicionario_jogador = calcular_pontos_jogador(jogador)

                reservas.update(dicionario_jogador)
    
    todos_os_tecnicos[nome_tecnico] = {'titulares': titulares, 'reservas': reservas}

lista_tecnicos = list(todos_os_tecnicos.keys())
print(f"Os técnicos que participarão da avaliação da rodada serão {', '.join(lista_tecnicos)}.")

prioridades = {'goleiro': 5,
                'lateral': 4,
                'zagueiro': 3,
                'meia': 2,
                'atacante': 1}

pontuacoes_finais = {}
tecnicos_que_trocaram = {}

for nome_tecnico, equipe in todos_os_tecnicos.items():
    pontuacao = 0
    for dados_titular in equipe['titulares'].values():
        pontuacao += dados_titular['pontuacao']

    melhor_troca = {'ganho': 0,
                    'titular_sai': '',
                    'reserva_entra': '',
                    'prioridade_posicao': -1,
                    'nome_titular_desempate': ''}
    for nome_reserva, dados_reserva in equipe['reservas'].items():
        for nome_titulares, dados_titulares in equipe['titulares'].items():
            if dados_reserva['posicao'] == dados_titulares['posicao']:
                ganho_atual = dados_reserva['pontuacao'] - dados_titulares['pontuacao']

                if ganho_atual > 0:                    
                    if ganho_atual > melhor_troca['ganho']:
                        melhor_troca['ganho'] = ganho_atual
                        melhor_troca['titular_sai'] = nome_titulares
                        melhor_troca['reserva_entra'] = nome_reserva
                        melhor_troca['prioridade_posicao'] = prioridades[dados_reserva['posicao']]
                        melhor_troca['nome_titular_desempate'] = nome_titulares

                    elif ganho_atual == melhor_troca['ganho']:
                        prioridade_atual = prioridades[dados_reserva['posicao']]
                        if prioridade_atual > melhor_troca['prioridade_posicao']:
                            melhor_troca['ganho'] = ganho_atual
                            melhor_troca['titular_sai'] = nome_titulares
                            melhor_troca['reserva_entra'] = nome_reserva
                            melhor_troca['prioridade_posicao'] = prioridade_atual
                            melhor_troca['nome_titular_desempate'] = nome_titulares
                        
                        elif prioridade_atual == melhor_troca['prioridade_posicao']:
                            if nome_titulares > melhor_troca['nome_titular_desempate']:
                                melhor_troca['ganho'] = ganho_atual
                                melhor_troca['titular_sai'] = nome_titulares
                                melhor_troca['reserva_entra'] = nome_reserva
                                melhor_troca['prioridade_posicao'] = prioridade_atual
                                melhor_troca['nome_titular_desempate'] = nome_titulares

    if melhor_troca['ganho'] > 0:
        print(f"{nome_tecnico} é um gênio da bola mesmo, a substituição de {melhor_troca['titular_sai']} por {melhor_troca['reserva_entra']} fez ele ganhar pontos!")
        
        pontuacao_final = pontuacao + melhor_troca['ganho']
        tecnicos_que_trocaram[nome_tecnico] = True
    
    else:
        print(f"Pode cortar {nome_tecnico} dos candidatos a técnico da amarelinha, nem fazer uma substituição ele consegue...")

        pontuacao_final = pontuacao
        tecnicos_que_trocaram[nome_tecnico] = False

    pontuacoes_finais[nome_tecnico] = pontuacao_final

vencedor_nome = ""
vencedor_pontos = -1

for tecnico, pontuacao in pontuacoes_finais.items():
    if pontuacao > vencedor_pontos:
        vencedor_pontos = pontuacao
        vencedor_nome = tecnico

print(f"{vencedor_nome} é incrível ganhou essa rodada com {vencedor_pontos} pontos!")

if not tecnicos_que_trocaram[vencedor_nome]:
    print(f"Temos que pedir desculpas a {vencedor_nome}, mesmo sem fazer uma substituição ele foi o melhor da rodada, talvez ele deva assumir a amarelinha depois do Ancelotti!")
