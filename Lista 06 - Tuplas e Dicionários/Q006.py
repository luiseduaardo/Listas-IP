def fase_final(time_a, ranking_a, time_b, ranking_b, artilheiros, final = False):
    golsa_mata_mata = golsb_mata_mata = 0
    acabar_jogo = False
    
    while not acabar_jogo:
        entrada = input()
        if entrada == 'FIM':
            acabar_jogo = True
        
        else:
            jogador, time_do_gol = entrada.split(' - ')
            print(f"Gol do {time_do_gol}, {jogador} é o nome da emoção")

            if time_do_gol == time_a:
                golsa_mata_mata += 1
            elif time_do_gol == time_b:
                golsb_mata_mata += 1
            
            jogador_time = f'{jogador}|{time_do_gol}'

            if jogador_time not in artilheiros:
                artilheiros[jogador_time] = {'gols': 0, 'nome': jogador, 'time': time_do_gol}
            artilheiros[jogador_time]['gols'] += 1

    print("Fim de jogo.")
   
    if golsa_mata_mata > golsb_mata_mata:
        vencedor_mata_mata = time_a
        perdedor_mata_mata = time_b
        placar_vencedor = golsa_mata_mata
        placar_perdedor = golsb_mata_mata
        normal = True
    elif golsb_mata_mata > golsa_mata_mata:
        vencedor_mata_mata = time_b
        perdedor_mata_mata = time_a
        placar_vencedor = golsb_mata_mata
        placar_perdedor = golsa_mata_mata
        normal = True
    else:
        if ranking_a < ranking_b:
            vencedor_mata_mata = time_a
            perdedor_mata_mata = time_b
            placar_vencedor = golsa_mata_mata
            placar_perdedor = golsb_mata_mata
        else:
            vencedor_mata_mata = time_b
            perdedor_mata_mata = time_a
            placar_vencedor = golsb_mata_mata
            placar_perdedor = golsa_mata_mata
        
        normal = False

    print(f"Placar: {vencedor_mata_mata} {placar_vencedor} X {placar_perdedor} {perdedor_mata_mata}")

    if final:
        return artilheiros, vencedor_mata_mata, perdedor_mata_mata, normal
    
    return artilheiros, vencedor_mata_mata, normal

entradas = 0
fim_entradas = False

NORDESTE = ('PE', 'CE', 'BA', 'SE', 'AL', 'PB', 'RN', 'MA', 'PI')
SUL = ('PR', 'RS', 'SC')
SUDESTE = ('SP', 'RJ', 'ES', 'MG')

times = {}
cotas_região = {'NORDESTE': 0, 'SUL': 0, 'SUDESTE': 0}

while entradas < 6 and not fim_entradas:
    time = input()

    if time == 'FIM':
        fim_entradas = True

    else:
        estado = input()
        if estado in NORDESTE:
            if cotas_região['NORDESTE'] == 2:
                print(f"Cota para a região Nordeste atingida. Por favor, insira um clube de outro estado, de outra região.")
            else:
                cotas_região['NORDESTE'] += 1
                times.update({time: {'pontos': 0, 'saldo': 0}})
                entradas += 1

        elif estado in SUDESTE:
            if cotas_região['SUDESTE'] == 2:
                print(f"Cota para a região Sudeste atingida. Por favor, insira um clube de outro estado, de outra região.")
            else:
                cotas_região['SUDESTE'] += 1
                times.update({time: {'pontos': 0, 'saldo': 0}})
                entradas += 1

        elif estado in SUL:
            if cotas_região['SUL'] == 2:
                print(f"Cota para a região Sul atingida. Por favor, insira um clube de outro estado, de outra região.")
            else:
                cotas_região['SUL'] += 1
                times.update({time: {'pontos': 0, 'saldo': 0}})
                entradas += 1

total_times = len(times)

if total_times < 6:
    print(f"Ai não dá, com {total_times} somente não dá para fazer um campeonato, essa ideia de Copa União foi um fiasco mesmo, #VOLTACBF")

else:
    for i in range(15):
        partida = input()

        lista_split1 = partida.split(' X ')

        primeiro_time = lista_split1[0]
        segundo_time = lista_split1[1]

        idx_ultimo_espaco_string = -1
        espaco_encontrado = False

        for i in range(len(primeiro_time) -1, -1, -1):
            if primeiro_time[i] == ' ' and not espaco_encontrado:
                idx_ultimo_espaco_string = i
                espaco_encontrado = True

        nome_primeiro_time = primeiro_time[:idx_ultimo_espaco_string]
        gols_primeiro_time = int(primeiro_time[idx_ultimo_espaco_string + 1:])

        lista_split3 = segundo_time.split(' ', 1)
        nome_segundo_time = lista_split3[1]
        gols_segundo_time = int(lista_split3[0])

        saldo_primeiro_time = gols_primeiro_time - gols_segundo_time
        saldo_segundo_time = gols_segundo_time - gols_primeiro_time

        pontos_primeiro_time = 0
        pontos_segundo_time = 0

        if gols_primeiro_time > gols_segundo_time:
            pontos_primeiro_time = 3
        
        elif gols_primeiro_time < gols_segundo_time:
            pontos_segundo_time = 3

        else:
            pontos_primeiro_time = pontos_segundo_time = 1
        
        times[nome_primeiro_time]['pontos'] += pontos_primeiro_time
        times[nome_primeiro_time]['saldo'] += saldo_primeiro_time

        times[nome_segundo_time]['pontos'] += pontos_segundo_time
        times[nome_segundo_time]['saldo'] += saldo_segundo_time

    seis_primeiros = {
        'nome': {'primeiro': '', 'segundo': '', 'terceiro': '', 'quarto': '', 'quinto': '', 'sexto': ''},
        'pontos': {'primeiro': -1, 'segundo': -1, 'terceiro': -1, 'quarto': -1, 'quinto': -1, 'sexto': -1},
        'saldo': {'primeiro': -100, 'segundo': -100, 'terceiro': -100, 'quarto': -100, 'quinto': -100, 'sexto': -100}
    }

    for equipe in times:
        pontos_candidato = times[equipe]['pontos']
        saldo_candidato = times[equipe]['saldo']

        pontos_primeiro_lugar = seis_primeiros['pontos']['primeiro']
        saldo_primeiro_lugar = seis_primeiros['saldo']['primeiro']
        
        pontos_segundo_lugar = seis_primeiros['pontos']['segundo']
        saldo_segundo_lugar = seis_primeiros['saldo']['segundo']

        pontos_terceiro_lugar = seis_primeiros['pontos']['terceiro']
        saldo_terceiro_lugar = seis_primeiros['saldo']['terceiro']

        pontos_quarto_lugar = seis_primeiros['pontos']['quarto']
        saldo_quarto_lugar = seis_primeiros['saldo']['quarto']

        pontos_quinto_lugar = seis_primeiros['pontos']['quinto']
        saldo_quinto_lugar = seis_primeiros['saldo']['quinto']

        pontos_sexto_lugar = seis_primeiros['pontos']['sexto']
        saldo_sexto_lugar = seis_primeiros['saldo']['sexto']


        if (pontos_candidato > pontos_primeiro_lugar) or (pontos_candidato == pontos_primeiro_lugar and saldo_candidato > saldo_primeiro_lugar):
            seis_primeiros['nome']['sexto'] = seis_primeiros['nome']['quinto']
            seis_primeiros['pontos']['sexto'] = seis_primeiros['pontos']['quinto']
            seis_primeiros['saldo']['sexto'] = seis_primeiros['saldo']['quinto']

            seis_primeiros['nome']['quinto'] = seis_primeiros['nome']['quarto']
            seis_primeiros['pontos']['quinto'] = seis_primeiros['pontos']['quarto']
            seis_primeiros['saldo']['quinto'] = seis_primeiros['saldo']['quarto']

            seis_primeiros['nome']['quarto'] = seis_primeiros['nome']['terceiro']
            seis_primeiros['pontos']['quarto'] = seis_primeiros['pontos']['terceiro']
            seis_primeiros['saldo']['quarto'] = seis_primeiros['saldo']['terceiro']

            seis_primeiros['nome']['terceiro'] = seis_primeiros['nome']['segundo']
            seis_primeiros['pontos']['terceiro'] = seis_primeiros['pontos']['segundo']
            seis_primeiros['saldo']['terceiro'] = seis_primeiros['saldo']['segundo']

            seis_primeiros['nome']['segundo'] = seis_primeiros['nome']['primeiro']
            seis_primeiros['pontos']['segundo'] = seis_primeiros['pontos']['primeiro']
            seis_primeiros['saldo']['segundo'] = seis_primeiros['saldo']['primeiro']

            seis_primeiros['nome']['primeiro'] = equipe
            seis_primeiros['pontos']['primeiro'] = pontos_candidato
            seis_primeiros['saldo']['primeiro'] = saldo_candidato
        
        elif (pontos_candidato > pontos_segundo_lugar) or (pontos_candidato == pontos_segundo_lugar and saldo_candidato > saldo_segundo_lugar):
            seis_primeiros['nome']['sexto'] = seis_primeiros['nome']['quinto']
            seis_primeiros['pontos']['sexto'] = seis_primeiros['pontos']['quinto']
            seis_primeiros['saldo']['sexto'] = seis_primeiros['saldo']['quinto']

            seis_primeiros['nome']['quinto'] = seis_primeiros['nome']['quarto']
            seis_primeiros['pontos']['quinto'] = seis_primeiros['pontos']['quarto']
            seis_primeiros['saldo']['quinto'] = seis_primeiros['saldo']['quarto']

            seis_primeiros['nome']['quarto'] = seis_primeiros['nome']['terceiro']
            seis_primeiros['pontos']['quarto'] = seis_primeiros['pontos']['terceiro']
            seis_primeiros['saldo']['quarto'] = seis_primeiros['saldo']['terceiro']

            seis_primeiros['nome']['terceiro'] = seis_primeiros['nome']['segundo']
            seis_primeiros['pontos']['terceiro'] = seis_primeiros['pontos']['segundo']
            seis_primeiros['saldo']['terceiro'] = seis_primeiros['saldo']['segundo']

            seis_primeiros['nome']['segundo'] = equipe
            seis_primeiros['pontos']['segundo'] = pontos_candidato
            seis_primeiros['saldo']['segundo'] = saldo_candidato

        elif (pontos_candidato > pontos_terceiro_lugar) or (pontos_candidato == pontos_terceiro_lugar and saldo_candidato > saldo_terceiro_lugar):
            seis_primeiros['nome']['sexto'] = seis_primeiros['nome']['quinto']
            seis_primeiros['pontos']['sexto'] = seis_primeiros['pontos']['quinto']
            seis_primeiros['saldo']['sexto'] = seis_primeiros['saldo']['quinto']

            seis_primeiros['nome']['quinto'] = seis_primeiros['nome']['quarto']
            seis_primeiros['pontos']['quinto'] = seis_primeiros['pontos']['quarto']
            seis_primeiros['saldo']['quinto'] = seis_primeiros['saldo']['quarto']

            seis_primeiros['nome']['quarto'] = seis_primeiros['nome']['terceiro']
            seis_primeiros['pontos']['quarto'] = seis_primeiros['pontos']['terceiro']
            seis_primeiros['saldo']['quarto'] = seis_primeiros['saldo']['terceiro']

            seis_primeiros['nome']['terceiro'] = equipe
            seis_primeiros['pontos']['terceiro'] = pontos_candidato
            seis_primeiros['saldo']['terceiro'] = saldo_candidato
        
        elif (pontos_candidato > pontos_quarto_lugar) or (pontos_candidato == pontos_quarto_lugar and saldo_candidato > saldo_quarto_lugar):
            seis_primeiros['nome']['sexto'] = seis_primeiros['nome']['quinto']
            seis_primeiros['pontos']['sexto'] = seis_primeiros['pontos']['quinto']
            seis_primeiros['saldo']['sexto'] = seis_primeiros['saldo']['quinto']

            seis_primeiros['nome']['quinto'] = seis_primeiros['nome']['quarto']
            seis_primeiros['pontos']['quinto'] = seis_primeiros['pontos']['quarto']
            seis_primeiros['saldo']['quinto'] = seis_primeiros['saldo']['quarto']

            seis_primeiros['nome']['quarto'] = equipe
            seis_primeiros['pontos']['quarto'] = pontos_candidato
            seis_primeiros['saldo']['quarto'] = saldo_candidato

        elif (pontos_candidato > pontos_quinto_lugar) or (pontos_candidato == pontos_quinto_lugar and saldo_candidato > saldo_quinto_lugar):
            seis_primeiros['nome']['sexto'] = seis_primeiros['nome']['quinto']
            seis_primeiros['pontos']['sexto'] = seis_primeiros['pontos']['quinto']
            seis_primeiros['saldo']['sexto'] = seis_primeiros['saldo']['quinto']

            seis_primeiros['nome']['quinto'] = equipe
            seis_primeiros['pontos']['quinto'] = pontos_candidato
            seis_primeiros['saldo']['quinto'] = saldo_candidato

        elif (pontos_candidato > pontos_sexto_lugar) or (pontos_candidato == pontos_sexto_lugar and saldo_candidato > saldo_sexto_lugar):
            seis_primeiros['nome']['sexto'] = equipe
            seis_primeiros['pontos']['sexto'] = pontos_candidato
            seis_primeiros['saldo']['sexto'] = saldo_candidato
        
    print(f"{seis_primeiros['nome']['primeiro']} - {seis_primeiros['pontos']['primeiro']} pontos")
    print(f"{seis_primeiros['nome']['segundo']} - {seis_primeiros['pontos']['segundo']} pontos")
    print(f"{seis_primeiros['nome']['terceiro']} - {seis_primeiros['pontos']['terceiro']} pontos")
    print(f"{seis_primeiros['nome']['quarto']} - {seis_primeiros['pontos']['quarto']} pontos")
    print(f"{seis_primeiros['nome']['quinto']} - {seis_primeiros['pontos']['quinto']} pontos")
    print(f"{seis_primeiros['nome']['sexto']} - {seis_primeiros['pontos']['sexto']} pontos")

    classificados = {1: seis_primeiros['nome']['primeiro'], 2: seis_primeiros['nome']['segundo'], 3: seis_primeiros['nome']['terceiro'], 4: seis_primeiros['nome']['quarto']}

        # Depois de imprimir a tabela e definir os classificados...
    rankings_originais = {
        classificados[1]: 1,
        classificados[2]: 2,
        classificados[3]: 3,
        classificados[4]: 4,
        seis_primeiros['nome']['quinto']: 5,
        seis_primeiros['nome']['sexto']: 6
    }

    print("Os confrontos foram definidos:")
    print(f"{classificados[1]} X {classificados[4]}")
    print(f"{classificados[2]} X {classificados[3]}")
    
    print("Vai começar o confronto, quem será que vence?")

    artilheiros = {}

    artilheiros, vencedor_semi1, vitoria_normal = fase_final(classificados[1], 1, classificados[4], 4, artilheiros)

    if vitoria_normal:
        print(f"O {vencedor_semi1} venceu e foi para a final, será que vai ser campeão?")
    else:
        print(f"O {vencedor_semi1} passa para a final após vencer nos pênaltis, será que vai ser campeão?")

    print("Vai começar o confronto, quem será que vence?")

    artilheiros, vencedor_semi2, vitoria_normal = fase_final(classificados[2], 2, classificados[3], 3, artilheiros)

    if vitoria_normal:
        print(f"O {vencedor_semi2} venceu e foi para a final, será que vai ser campeão?")
    else:
        print(f"O {vencedor_semi2} passa para a final após vencer nos pênaltis, será que vai ser campeão?")

    print("Vai começar a grande decisão, quem será o campeão brasileiro de 1987?")

    artilheiros, vencedor_final, perdedor_final, vitoria_normal = fase_final(vencedor_semi1, 
                                                                             rankings_originais[vencedor_semi1], vencedor_semi2, 
                                                                             rankings_originais[vencedor_semi2], artilheiros, 
                                                                             True)

    campeao_para_anunciar = vencedor_final

    if campeao_para_anunciar == 'Sport':
        print("Quem deixou o Sport participar, a Copa União só permite clubes grandes de participarem, tirem ele daqui que do jeito que eles são é capaz de irem no tribunal pedir o reconhecimento do 'Brasileiro de Questão de IP'")
        campeao_para_anunciar = perdedor_final

    elif campeao_para_anunciar == 'Santa Cruz':
        print("O terror do Nordeste agradece o reconhecimento, porém recusa o titulo, diferente do seu rival ele prefere ganhar o título em campo, e não em imaginação")
        campeao_para_anunciar = perdedor_final

    # caso que repete campeão
    if campeao_para_anunciar == 'Sport':
        print("Quem deixou o Sport participar, a Copa União só permite clubes grandes de participarem, tirem ele daqui que do jeito que eles são é capaz de irem no tribunal pedir o reconhecimento do 'Brasileiro de Questão de IP'")
        campeao_para_anunciar = perdedor_final

    elif campeao_para_anunciar == 'Santa Cruz':
        print("O terror do Nordeste agradece o reconhecimento, porém recusa o titulo, diferente do seu rival ele prefere ganhar o título em campo, e não em imaginação")
        campeao_para_anunciar = perdedor_final


    if campeao_para_anunciar == 'Sport' or campeao_para_anunciar == 'Santa Cruz':
        semi_perdedor1 = ''
        semi_perdedor2 = ''
        if classificados[1] != vencedor_final and classificados[1] != perdedor_final:
            semi_perdedor1 = classificados[1]
        if classificados[2] != vencedor_final and classificados[2] != perdedor_final:
            if semi_perdedor1 == '':
                semi_perdedor1 = classificados[2]
            else:
                semi_perdedor2 = classificados[2]
        if classificados[3] != vencedor_final and classificados[3] != perdedor_final:
            if semi_perdedor1 == '':
                semi_perdedor1 = classificados[3]
            else:
                semi_perdedor2 = classificados[3]
        if classificados[4] != vencedor_final and classificados[4] != perdedor_final:
            semi_perdedor2 = classificados[4]

        if times[semi_perdedor1]['pontos'] > times[semi_perdedor2]['pontos']:
            campeao_para_anunciar = semi_perdedor1
        elif times[semi_perdedor2]['pontos'] > times[semi_perdedor1]['pontos']:
            campeao_para_anunciar = semi_perdedor2
        else:
            if times[semi_perdedor1]['saldo'] > times[semi_perdedor2]['saldo']:
                campeao_para_anunciar = semi_perdedor1
            else:
                campeao_para_anunciar = semi_perdedor2

    if campeao_para_anunciar == 'Flamengo':
        print("Em 1987, o Flamengo é o campeão inquestionável! Conquistou na bola e com o reconhecimento merecido. Qualquer outra conversa é história para boi dormir.")
    else:
        print(f"E o campeão do real Campeonato Brasileiro de 1987 foi o {campeao_para_anunciar}, ouvi dizer que a CBF tava querendo fazer um outro campeonato chamado módulo amarelo, ainda bem que todo mundo entendeu que aquilo é somente uma serie B")
    
    if len(artilheiros) == 0:
        print("Esse ano o nivel foi fraco, não tivemos um artilheiro")
    else:
        artilheiro_nome = ''
        artilheiro_gols = -1
        artilheiro_time = ''

        for chave in artilheiros:
            gols_candidato = artilheiros[chave]['gols']
            nome_candidato = artilheiros[chave]['nome'] 
            
            if (gols_candidato > artilheiro_gols) or (gols_candidato == artilheiro_gols and chave < artilheiro_nome):
                artilheiro_gols = gols_candidato
                artilheiro_nome = nome_candidato
                artilheiro_time = artilheiros[chave]['time']

        if artilheiro_time == campeao_para_anunciar:
            print(f"{artilheiro_nome} garantiu o título do campeonato e a artilharia, que ano feliz para ele")
        else:
            print(f"Apesar de não ter sido campeão, pelo menos {artilheiro_nome} foi o artilheiro, a culpa não foi dele")
