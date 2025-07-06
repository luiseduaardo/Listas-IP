def verificar_terceiro(primeiro_lutador, segundo_lutador):
    if (lutador1 == 'Goku' and lutador2 == 'Jiren') or (lutador1 == 'Jiren' and lutador2 == 'Goku'):
        return 'Goku'
    elif (lutador1 == 'Frieza' and lutador2 == 'Jiren') or (lutador1 == 'Jiren' and lutador2 == 'Frieza'):
        return 'Frieza'
    elif (lutador1 == 'Gohan' and lutador2 == 'Namekuseijins') or (lutador1 == 'Namekuseijins' and lutador2 == 'Gohan'):
        return 'Gohan'
    elif (lutador1 == 'Androide 17' and lutador2 == 'Ribrianne') or (lutador1 == 'Ribrianne' and lutador2 == 'Androide 17'):
        return 'Androide 17'
    else:
        return ''

def calcular_forca(tecnica):
    tamanho_string = len(tecnica)
    pontuacao = tamanho_string % 8
    return pontuacao

def batalha(primeiro_lutador, pontuacao_primeiro, segundo_lutador, pontuacao_segundo, possivel_terceiro, terceiro_lutador, pontuacao_terceiro):
    equipe_1 = [primeiro_lutador]
    pontuacao_equipe1 = pontuacao_primeiro
    equipe_2 = [segundo_lutador]
    pontuacao_equipe2 = pontuacao_segundo

    if possivel_terceiro:
        if primeiro_lutador == 'Goku' or primeiro_lutador == 'Frieza' or primeiro_lutador == 'Gohan' or primeiro_lutador == 'Androide 17':
            equipe_1.append(terceiro_lutador)
            pontuacao_equipe1 += pontuacao_terceiro
        else:
            equipe_2.append(terceiro_lutador)
            pontuacao_equipe2 += pontuacao_terceiro

    if pontuacao_equipe1 > pontuacao_equipe2:
        return equipe_1
    else:
        return equipe_2

qtd_batalhas = int(input())

print(f"O torneio do poder irá começar com {qtd_batalhas} batalhas no dia de hoje! Vamos ver quais universos vão conseguir se manter vivos até o final do dia!")

for i in range(qtd_batalhas):
    entrada_1 = input().split(' - ')
    lutador1 = entrada_1[0]
    lutador1_tecnica = entrada_1[1]
    pontuacao1 = calcular_forca(lutador1_tecnica)

    entrada_2 = input().split(' - ')
    lutador2 = entrada_2[0]
    lutador2_tecnica = entrada_2[1]
    pontuacao2 = calcular_forca(lutador2_tecnica)

    aliado = verificar_terceiro(lutador1, lutador2)

    if aliado != '':
        entrada_3 = input().split(' - ')
        lutador3 = entrada_3[0]
        lutador3_tecnica = entrada_3[1]
        pontuacao3 = calcular_forca(lutador3_tecnica)
        terceiro_lutador = True

        print(f"A intensidade dos dois lutadores motivou {lutador3} a entrar na batalha também!")
    else:
        lutador3 = ''
        pontuacao3 = 0
        terceiro_lutador = False

    lista_vencedores = batalha(lutador1, pontuacao1, lutador2, pontuacao2, terceiro_lutador, lutador3, pontuacao3)

    if aliado == '':
        print(f"Incrível! {lista_vencedores[0]} mostrou sua força e defenderá seu universo até o final!")

    else:
        print(f"Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {lutador1_tecnica}, {lutador2_tecnica} e {lutador3_tecnica}! A batalha acaba com {' e '.join(lista_vencedores)} no topo!")
