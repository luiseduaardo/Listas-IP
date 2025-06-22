print("Bem amigos da Rede Globo, emoção no ar! Prepare o coração porque hoje é dia de decisão! É final de Copa do Mundo, mas não é futebol… é ping pong, meu amigo! A raquete vai cantar, a bolinha vai voar, e só um será campeão! Segura essa emoção porque vai começar!")

# Input do primeiro sacador
sacador_1 = input()
sacador = sacador_1

# Define sacador do primeiro set
if sacador == 'hugo':
    hugo_saca = True
    lin_saca = False
elif sacador == 'lin':
    lin_saca = True
    hugo_saca = False

# Variáveis globais
set_atual = 0
MAX_SETS = 5
sets_hugo = sets_lin = 0

acabar_partida = False
tie_break_set = False
hugo_vez = False
lin_vez = False

# Define contagem de sets
while not acabar_partida:
    set_atual += 1
    print(f"Set {set_atual}:")

    # Print inicial em caso de tie break
    if set_atual == MAX_SETS:
        print(f"Agora é hora da decisão! Vamos para o tie-break, quem errar, perde tudo! É emoção até o fim!")
        tie_break_set = True
    
    # Reseta variáveis de pontos a cada fim de set
    acabar_set = False
    pontos_hugo = pontos_lin = 0

    # Máximo de pontos por set
    if set_atual == MAX_SETS:
        MAX_PONTOS = 7 # máximo de pontos por set em caso de tie break
    else:
        MAX_PONTOS = 5

    # Definição de variáveis para alternar as jogadas na sequência
    if hugo_saca:
        hugo_vez = True
        lin_vez = False
    elif lin_saca:
        hugo_vez = False
        lin_vez = True

    # Define ação dos pontos
    while not acabar_set:
        sequencia = input()
        ponto_encerrado = False
        acao = ''
        acao_anterior = ''
        jogador_pontua = ''
        jogador_erro = ''
        contagem_acoes = 0
        
        # Define quem pontuou a depender de cada tipo de ataque ou defesa
        for letra in sequencia:
            if letra != '-': 
                acao += letra
            else:   # Casos em que deve apenas prosseguir a rodada / ações permitidas
                contagem_acoes += 1

                acao_anterior = acao
                acao = ''

        contagem_acoes += 1 # Valida última ação já que ela não vem seguida de '-'

        # Vê quem é o jogador da vez apenas no final
        if hugo_saca:
            if contagem_acoes % 2 == 0: # hugo saca e qtd de ações é par
                lin_vez = True
                hugo_vez = False
            else: # hugo saca e qtd de ações é ímpar
                lin_vez = False
                hugo_vez = True
        elif lin_saca: 
            if contagem_acoes % 2 == 0: # lin saca e qtd de ações é par
                lin_vez = False
                hugo_vez = True
            else: # lin saca e qtd de ações é ímpar
                lin_vez = True
                hugo_vez = False
                    
        if acao != '': # condicional sempre será atendida
            # condicionais de erro que valida pontuação para o jogador que não cometeu o erro
            if acao_anterior == 'saque' and (acao == 'ataque' or acao == 'erro'):
                if hugo_vez:
                    pontos_lin += 1
                    jogador_pontua = 'Lin'
                elif lin_vez:
                    pontos_hugo += 1
                    jogador_pontua = 'Hugo'
                print(f"Uau, um ace! {jogador_pontua} solta o braço e deixa o adversário parado!")
                ponto_encerrado = True

            elif acao == 'erro':
                if hugo_vez:
                    pontos_lin += 1
                    jogador_pontua = 'Lin'
                    jogador_erro = 'Hugo'
                elif lin_vez:
                    pontos_hugo += 1
                    jogador_pontua = 'Hugo'
                    jogador_erro = 'Lin'
                print(f"{jogador_erro} se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                ponto_encerrado = True
            
            elif acao_anterior == 'ataque' and acao != 'defesa':
                if lin_vez:
                    pontos_hugo += 1
                    jogador_pontua = 'Hugo'
                elif hugo_vez:
                    pontos_lin += 1
                    jogador_pontua = 'Lin'
                print(f"{jogador_pontua} acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!")
                ponto_encerrado = True
                
            elif acao_anterior == 'defesa' and acao == 'defesa':
                if hugo_vez:
                    pontos_lin += 1
                    jogador_pontua = 'Lin'
                    jogador_erro = 'Hugo'
                elif lin_vez:
                    pontos_hugo += 1
                    jogador_pontua = 'Hugo'
                    jogador_erro = 'Lin'
                print(f"{jogador_erro} tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.")
                ponto_encerrado = True
        
        # print de placar
        if ponto_encerrado:
            print(f"Ponto para {jogador_pontua}!\nPlacar do {set_atual} set : {pontos_hugo} x {pontos_lin}")

        # Caracteriza fim de set
        if (pontos_hugo >= MAX_PONTOS or pontos_lin >= MAX_PONTOS) and abs(pontos_lin - pontos_hugo) >= 2:
            acabar_set = True

            # Define vencedor do set
            if pontos_lin > pontos_hugo:
                jogador = 'Lin'
                sets_lin += 1
            elif pontos_hugo > pontos_lin:
                jogador = 'Hugo'
                sets_hugo += 1

            # Prints de vitória de set
            if (pontos_lin == 0 or pontos_hugo == 0): # pneu
                if MAX_PONTOS == 5: # pneu em set convencional
                    print(f"Fim de set! Domínio total: 5 a 0, sem chance para o adversário — {jogador} passeia na mesa")
                elif MAX_PONTOS == 7: # pneu no tie break
                    print(f"Fim de tie-break! {jogador} arrasa com um 7 a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!")
            else: # Caso um set não tenha sido pneu
                print(f"E o set vai para {jogador}!")

        # Apenas em caso de tie-break
        if tie_break_set:
            if (pontos_hugo + pontos_lin) % 2 == 1: # alterna jogada a cada 2 saques de cada jogador
                if hugo_saca:
                    lin_saca = True
                    hugo_saca = False
                else:
                    hugo_saca = True
                    lin_saca = False

        # print de vai a dois em set convencional
        elif (pontos_hugo == 4 and pontos_lin == 4) and not tie_break_set:
            print(f"O set está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva — é decisão na mesa!")

        # print de vai a 2 em tie break
        if (pontos_hugo == 6 and pontos_lin == 6) and tie_break_set:
            print(f"O tie-break está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva, é a reta final da disputa! Quem será o grande campeão?")

    # Printa placar do jogo em sets
    print(f"Placar do jogo: {sets_hugo} x {sets_lin}")

    # Alterna sacadores para início de novo set
    if hugo_saca:
        lin_saca = True
        hugo_saca = False
    elif lin_saca:
        hugo_saca = True
        lin_saca = False

    # Verifica se a partida acabou
    if sets_hugo == MAX_SETS // 2 + 1 or sets_lin == MAX_SETS // 2 + 1:
        acabar_partida = True

# Prints finais
if (sets_hugo > sets_lin) and not tie_break_set:
    print(f"Hugo garantiu a vitória sem precisar de tie-break! Uma performance sólida e sem erros, ele dominou o jogo do início ao fim e se sagrou campeão do mundo!")

elif (sets_hugo > sets_lin) and tie_break_set:
    print(f"Hugo é o grande vencedor! Ele conquista o tie-break com uma performance impecável e leva a vitória!")

elif (sets_hugo < sets_lin) and tie_break_set:
    print(f"Hugo lutou até o fim, mas no tie-break, o adversário levou a melhor. Uma derrota apertada, mas ainda assim, uma grande batalha!")

elif (sets_hugo < sets_lin) and not tie_break_set:
    print(f"Hugo não conseguiu segurar a pressão e acabou perdendo sem precisar do tie-break. Foi uma grande final, mas hoje não foi o seu dia. Vitória do chinês!")
