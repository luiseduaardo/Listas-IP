# Variáveis globais
rodada_atual = 1
jogo_acabou = False
pontos_jaob = pontos_luvu = 0

# Input número de rodadas
numero_rodadas = int(input())

# Input vencedor da tomada
print("Vamos dar início à disputa!!! TOMADA!!!")
vencedor_tomada = str(input())

if vencedor_tomada == 'Jaob':
    print("Jaob veio de Catende e está pronto para vencer!!!")

elif vencedor_tomada == 'Luvusier':
    print("Nada se cria, tudo se transforma, então Luvusier irá se transformar em um vencedor!!!")

jogador_comeca = vencedor_tomada

# Laço de repetição
while rodada_atual <= numero_rodadas and not jogo_acabou:
    print(f"COMEÇA A {rodada_atual}ª RODADA!")

    acertou = False
    jogador_atual = jogador_comeca
    pontos_jogador = 0

    while not acertou:
        objeto = str(input())

        print(f"{jogador_atual} jogou a bolinha no(a) {objeto}!")

        if objeto == 'mesa':
            if jogador_atual == 'Jaob':
                jogador_atual = 'Luvusier'
            elif jogador_atual == 'Luvusier':
                jogador_atual = 'Jaob'
        
        else:
            acertou = True

            if objeto == 'Baralho de UNO':
                pontos = 2
                if jogador_atual == 'Luvusier':
                    pontos_luvu += pontos
                    pontos_jogador = pontos_luvu
                elif jogador_atual == 'Jaob':
                    pontos_jaob += pontos
                    pontos_jogador = pontos_jaob
                print(f"{jogador_atual} teve uma grande pontaria e acertou {objeto}! Agora está com {pontos_jogador} pontos.")
                
            elif objeto == 'Armário de Homero e Elena' or objeto == 'Peça de Dominó':
                pontos = 3
                if jogador_atual == 'Luvusier':
                    pontos_luvu += pontos
                    pontos_jogador = pontos_luvu
                elif jogador_atual == 'Jaob':
                    pontos_jaob += pontos
                    pontos_jogador = pontos_jaob
                print(f"{jogador_atual} teve uma grande pontaria e acertou {objeto}! Agora está com {pontos_jogador} pontos.")

            elif objeto == 'Baralho de Coup Desaparecido':
                pontos = 100
                jogo_acabou = True
                if jogador_atual == 'Luvusier':
                    pontos_luvu += pontos
                    pontos_jogador = pontos_luvu
                elif jogador_atual == 'Jaob':
                    pontos_jaob += pontos
                    pontos_jogador = pontos_jaob
                print(f"{jogador_atual} teve uma grande pontaria e acertou {objeto}! Agora está com {pontos_jogador} pontos.")
                print(f"{jogador_atual} achou o Coup!!! Ele merece a vitória sem dúvidas!")
            
            
            elif objeto == 'Projetor':
                pontos = 2
                if jogador_atual == 'Luvusier':
                    pontos_luvu = max(0, pontos_luvu - pontos)
                    pontos_jogador = pontos_luvu
                    print(f"{jogador_atual} teve mãos de alface e acertou o(a) {objeto}. Agora está com {pontos_jogador} pontos.")
                    jogador_atual = 'Jaob'
                elif jogador_atual == 'Jaob':
                    pontos_jaob = max(0, pontos_jaob - pontos)
                    pontos_jogador = pontos_jaob
                    print(f"{jogador_atual} teve mãos de alface e acertou o(a) {objeto}. Agora está com {pontos_jogador} pontos.")
                    jogador_atual = 'Luvusier'
            
            elif objeto == 'Computador':
                pontos = 3
                if jogador_atual == 'Luvusier':
                    pontos_luvu = max(0, pontos_luvu - pontos)
                    pontos_jogador = pontos_luvu
                    print(f"{jogador_atual} teve mãos de alface e acertou o(a) {objeto}. Agora está com {pontos_jogador} pontos.")
                    jogador_atual = 'Jaob'
                elif jogador_atual == 'Jaob':
                    pontos_jaob = max(0, pontos_jaob - pontos)
                    pontos_jogador = pontos_jaob
                    print(f"{jogador_atual} teve mãos de alface e acertou o(a) {objeto}. Agora está com {pontos_jogador} pontos.")
                    jogador_atual = 'Luvusier'
            
            elif objeto == 'Cabeça do Amiguinho':
                pontos = 5
                if jogador_atual == 'Luvusier':
                    pontos_luvu = max(0, pontos_luvu - pontos)
                    pontos_jogador = pontos_luvu
                    print(f"{jogador_atual} teve mãos de alface e acertou o(a) {objeto}. Agora está com {pontos_jogador} pontos.")
                    jogador_atual = 'Jaob'
                elif jogador_atual == 'Jaob':
                    pontos_jaob = max(0, pontos_jaob - pontos)
                    pontos_jogador = pontos_jaob
                    print(f"{jogador_atual} teve mãos de alface e acertou o(a) {objeto}. Agora está com {pontos_jogador} pontos.")
                    jogador_atual = 'Luvusier'
            
            elif objeto == 'Nada':
                pontos = 1
                if jogador_atual == 'Luvusier':
                    pontos_luvu = max(0, pontos_luvu - pontos)
                    pontos_jogador = pontos_luvu
                    print(f"{jogador_atual} teve mãos de alface e acertou o(a) {objeto}. Agora está com {pontos_jogador} pontos.")
                    jogador_atual = 'Jaob'
                elif jogador_atual == 'Jaob':
                    pontos_jaob = max(0, pontos_jaob - pontos)
                    pontos_jogador = pontos_jaob
                    print(f"{jogador_atual} teve mãos de alface e acertou o(a) {objeto}. Agora está com {pontos_jogador} pontos.")
                    jogador_atual = 'Luvusier'

        jogador_comeca = jogador_atual
    
    rodada_atual += 1

# Resultado
print("\nTEMOS O RESULTADO DA PARTIDA!")
if pontos_jaob > pontos_luvu:
    print(f"Jaob deu orgulho à Catende e ganhou a disputa com {pontos_jaob} pontos!")

elif pontos_luvu > pontos_jaob:
    print(f"A química está em festa, Luvusier ganha a disputa com {pontos_luvu} pontos!")

else:
    print("Jaob usou a sua autoridade como monitor-chefe e ganhou a disputa mesmo com o empate!")
