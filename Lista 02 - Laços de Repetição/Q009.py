# Input de nome dos jogadores
jogador_1 = input()
jogador_2 = input()

# Condicional para poder usar o print da partida épica
if (jogador_1 == 'Luis' or jogador_1 == 'Lavoisier' or jogador_1 == 'Joab' or jogador_1 == 'Renan') or (jogador_2 == 'Luis' or jogador_2 == 'Lavoisier' or jogador_2 == 'Joab' or jogador_2 == 'Renan'):
    print("Essa partida vai ser épica! O jogo vai ser emocionante!")

# Input número de sets
sets = 0
while sets % 2 == 0 or sets <= 0:
    sets = int(input())

# Input nível de disputa
nivel_disputa = input()
if nivel_disputa == 'aprendizes':
    rebatida_maxima = 1
elif nivel_disputa == 'básicos':
    rebatida_maxima = 2
elif nivel_disputa == 'amostradinhos':
    rebatida_maxima = 3

# Variáveis globais
jogador_1_sets = 0
jogador_2_sets = 0
num_set_atual = 0
jogador_inicia = jogador_1
acabar_sets = False

while not acabar_sets:
    num_set_atual += 1
    print(f"Iniciando o {num_set_atual}º set")
    pontos_1 = 0
    pontos_2 = 0
    sacador = jogador_inicia
    acabar_set = False

    while not acabar_set:
        acao = ''
        while acao != 'saque':
            acao = input()

        # Ação inicial do set
        if acao == 'saque':
            print(f"O saque é de {sacador}")
            entrada1 = input()
            entrada2 = input()

            saque_valido = False
            erro_saque = False

            if entrada1 == 'REDE' or entrada2 == 'REDE':
                print("Vish, ainda bateu na rede")
                saque_valido = False
            elif entrada1 == 'SA' and entrada2 == 'AO':
                print("Um saque PERFEITO!!")
                saque_valido = True
            elif entrada1 == 'SA' and entrada2 == 'SA':
                print(f"{sacador}, a bola quicou duas vezes na sua própria área! Que saque feio foi esse??")
                saque_valido = False
            elif entrada1 == 'AO' and entrada2 == 'AO':
                print(f"Boa, {sacador}! Deu ponto de graça pro oponente!! Agora quem saca é ", end='')
                saque_valido = False

            # Verifica se houve erro no saque e printa o nome de quem vai sacar na próxima rodada
            if not saque_valido:
                if sacador == jogador_1:
                    pontos_2 += 1
                    sacador = jogador_2
                    if entrada1 == 'AO' and entrada2 == 'AO':
                        print(jogador_2)
                elif sacador == jogador_2:
                    pontos_1 += 1
                    sacador = jogador_1
                    if entrada1 == 'AO' and entrada2 == 'AO':
                        print(jogador_1)
            
            elif saque_valido:
                rebatidas = 0
                acabou_rebatida = False

                while not acabou_rebatida:
                    acao_rebatida = input()  # deve ser 'rebatida'

                    if acao_rebatida == f"{jogador_1} deixou a bola cair":
                        pontos_2 += 1
                        sacador = jogador_2
                        acabou_rebatida = True
                    elif acao_rebatida == f"{jogador_2} deixou a bola cair":
                        pontos_1 += 1
                        sacador = jogador_1
                        acabou_rebatida = True
                    elif acao_rebatida == "oponente rebateu":
                        rebatidas += 1
                        if rebatidas == rebatida_maxima:
                            velocidade_1 = int(input())
                            velocidade_2 = int(input())
                            if velocidade_1 < velocidade_2:
                                pontos_1 += 1
                                sacador = jogador_1
                            else:
                                pontos_2 += 1
                                sacador = jogador_2
                            acabou_rebatida = True

        # Verifica se o set acabou 
        if (pontos_1 >= 3 or pontos_2 >= 3) and abs(pontos_1 - pontos_2) >= 2:  # abs serve para garantir que a diferença é de pelo menos 2 pontos positivos
            if pontos_1 > pontos_2:
                jogador_1_sets += 1
                jogador_inicia = jogador_1
            else:
                jogador_2_sets += 1
                jogador_inicia = jogador_2
            acabar_set = True

    # Verifica se a partida acabou
    if jogador_1_sets == sets // 2 + 1 or jogador_2_sets == sets // 2 + 1:
        acabar_sets = True

# Fim do jogo
if jogador_1_sets > jogador_2_sets:
    vencedor = jogador_1
else:
    vencedor = jogador_2

print(f"Depois de {num_set_atual} set(s) vibrante(s), o grande vencedor é {vencedor}!!")
print("Fim do jogo!")
