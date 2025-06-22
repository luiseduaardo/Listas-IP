partidas_jogadas = 1
vitorias = derrotas = 0
encerrar_carreira = False
encerrar_carreira2 = False

lugar_1 = str(input())
adversario_1 = str(input())
resultado_1 = str(input())

print("Byte, o cachorro mais promissor do futebol nordestino, acaba de calçar suas quatro chuteiras e está pronto para entrar em campo!")

if lugar_1 == 'Catende' or lugar_1 == 'Tabira':
    print("É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.")

if 's' in adversario_1 and 'p' in adversario_1 and 'o' in adversario_1 and 'r' in adversario_1 and 't' in adversario_1:
    print("Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!")

if resultado_1 == 'VENCEU':
    print("TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!")
    vitorias += 1
elif resultado_1 == 'perdeu':
    print("Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...")
    derrotas += 1
elif resultado_1 == 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
    print('Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!')
    expressao = str(input())
    a, b, c = expressao
    print("A expressão resolvida é:", end = ' ')
    if b == '+':
        print(f"{int(a) + int(c):.2f}")
    elif b == '-':
        print(f"{int(a) - int(c):.2f}")
    elif b == '*':
        print(f"{int(a) * int (c):.2f}")
    elif b == '/':
        print(f"{int(a) / int(c):.2f}")
    
    vitorias += 1
    
    print("Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!")
    encerrar_carreira = True

if not encerrar_carreira:
    partidas_jogadas += 1
    lugar_2 = str(input())
    adversario_2 = str(input())
    resultado_2 = str(input())

    if lugar_2 == 'Catende' or lugar_2 == 'Tabira':
        print("É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.")

    if (lugar_1 == 'Catende' or lugar_1 == 'Tabira') and (lugar_2 == 'Catende' or lugar_2 == 'Tabira'):
        print("Não dá mais! Jogar nessas duas cidades é sinal de que o Santa Cruz precisa mais de magia do que de reforços...")
    
    if 's' in adversario_2 and 'p' in adversario_2 and 'o' in adversario_2 and 'r' in adversario_2 and 't' in adversario_2:
        print("Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!")
    
    if resultado_2 == 'VENCEU':
        print("TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!")
        vitorias += 1
    elif resultado_2 == 'perdeu':
        print("Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...")
        derrotas += 1
    elif resultado_2 == 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
        print('Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!')
        expressao = str(input())
        a, b, c = expressao
        print("A expressão resolvida é:", end = ' ')
        if b == '+':
            print(f"{int(a) + int(c):.2f}")
        elif b == '-':
            print(f"{int(a) - int(c):.2f}")
        elif b == '*':
            print(f"{int(a) * int (c):.2f}")
        elif b == '/':
            print(f"{int(a) / int(c):.2f}")

        vitorias += 1
        
        encerrar_carreira2 = True
        print("Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!")

print("\nRELATÓRIO DA PRÉ-TEMPORADA DO BYTE:")
print(f"- Partidas jogadas: {partidas_jogadas}")
print(f"- Vitórias: {vitorias}")
print(f"- Derrotas: {derrotas}")
print(f"- Tentaram roubar o bixinho:", end = ' ')
if encerrar_carreira or encerrar_carreira2:
    print("sim :(")
else:
    print("Não!!!! :D")
print(f"- Cidades visitadas:", end = ' ')
if not encerrar_carreira and lugar_1 != lugar_2:
    print(f"{lugar_1} e {lugar_2}")
else:
    print(f"{lugar_1}")
    
print(f"- Adversários enfrentados:", end = ' ')
if not encerrar_carreira and adversario_1 != adversario_2:
    print(f"{adversario_1} e {adversario_2}\n")
else:
    print(f"{adversario_1}\n")
    

print("E assim termina a pré-temporada do Byte pelos gramados. Anotar tudo isso na mão dá uma trabalheira! Nas próximas férias o Byte deve esperar saber laços, listas, funções e muito mais pra registrar tudo com mais facilidade :)")
