acabou = False
lista_infos = []

while not acabou:
    informacoes = dict()
    nome_jogador = input()
    if nome_jogador == 'FIM':
        acabou = True

    if not acabou:
        disposicao_percentual = int(input())
        posicao_jogador = input()

        informacoes.update({'nome': nome_jogador, 'disposicao': disposicao_percentual, 'posição': posicao_jogador})

        if disposicao_percentual >= 85:
            chutes_passes = int(input())
            informacoes.update({'chutes/passes': chutes_passes})

        elif 50 <= disposicao_percentual < 85:
            desempenho_ultimo_jogo = int(input())
            informacoes.update({'desempenho último jogo': desempenho_ultimo_jogo})

        else:
            desempenho_ultimo_treino = int(input())
            informacoes.update({'desempenho último treino': desempenho_ultimo_treino})
    
        lista_infos.append(informacoes)

jogadores = atacantes_prontos = outros_prontos = 0

for dicionario in lista_infos:
    nome = dicionario['nome']
    posicao = dicionario['posição']

    if 'chutes/passes' in dicionario:
        valencia = dicionario['chutes/passes']
        if posicao == 'atacante':
            if valencia > 10:
                print(f"{nome} está com um bom desempenho ofensivo.")
                atacantes_prontos += 1
            else:
                print(f"{nome} pode melhorar, Ancelotti pode usá-lo no segundo tempo.")
        else:
            if valencia >= 20:
                print(f"{nome} está com um bom desempenho de passes.")
                outros_prontos += 1
            else:
                print(f"{nome} pode melhorar, Ancelotti pode não colocá-lo no primeiro tempo.")
    
    elif 'desempenho último jogo' in dicionario:
        valencia = dicionario['desempenho último jogo']
        if valencia > 80:
            print(f"O jogador {nome} pode ser escalado para a próxima partida.")
            if posicao == 'atacante':
                atacantes_prontos += 1
            else:
                outros_prontos += 1
        else:
            print(f"Ancelotti precisa analisar o desempenho do {nome} na partida.")

    elif 'desempenho último treino' in dicionario:
        valencia = dicionario['desempenho último treino']
        if valencia > 70:
            print(f"Ancelotti deve colocar {nome} para treinar mais.")
        else:
            print(f"{nome} não deveria estar na próxima convocação.")
    
    jogadores += 1

print()

print(f"Relatório dos jogadores:\nTotal de jogadores analisados: {jogadores}\nAtacantes prontos para começar: {atacantes_prontos}\nMeio-campistas e Defensores prontos para começar: {outros_prontos}")
