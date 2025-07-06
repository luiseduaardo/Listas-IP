def aumentar_pontuacao_atributo(frase): # define o atributo
    poder = ''
    for letra in frase:
        if letra.isdigit():
            poder += letra

    if poder != '':
        return int(poder)
    else:
        return 0

def analisar_atributos(atributo): # analisa cada atributo e retorna o idx de cada atributo
    atributo = atributo.lower()
    pontuacao = aumentar_pontuacao_atributo(atributo)
    if 'força' in atributo:
        return 0, pontuacao
    elif 'agilidade' in atributo:
        return 1, pontuacao
    elif 'ki' in atributo:
        return 2, pontuacao
    elif 'super saiyajin' in atributo:
        return 3, pontuacao
    
def print_matriz(matrix): # printa a matriz
    ordem = len(matrix)

    print()
    for i in range(ordem):
        print(' '.join(matrix[i]))
    print()

def calcular_distancia(pos1, pos2):
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))

def realizar_movimentacao(matriz, pos_atual, direcao, quantidade, velocidade, inicial_personagem):
    ordem = len(matriz)
    linha, coluna = pos_atual[0], pos_atual[1]
    movimento_real = min(quantidade, velocidade)

    # Apaga a posição antiga
    matriz[linha][coluna] = '0'

    # Calcula a nova posição
    if direcao == 'cima':
        linha -= movimento_real
    elif direcao == 'baixo':
        linha += movimento_real
    elif direcao == 'esquerda':
        coluna -= movimento_real
    elif direcao == 'direita':
        coluna += movimento_real

    if linha < 0: linha = 0
    if linha >= ordem: linha = ordem - 1
    if coluna < 0: coluna = 0
    if coluna >= ordem: coluna = ordem - 1
    
    # Atualiza para a nova posição
    matriz[linha][coluna] = inicial_personagem
    return [linha, coluna]

# leitura inicial dos nomes e print inicial
personagem_caesar = input()
personagem_artur = input()

print(f"Você sabe que {personagem_artur} é mais forte, nem tente dizer o contrário Caesar!\nNem venha Artur, {personagem_caesar} ganharia fácil numa luta.\n")

# padrão de stats: força, agilidade, ki e super saiyajin
lista_atributos_geral = ['força', 'agilidade', 'Ki', 'Transformação Super Saiyajin']
stats_ceasar = [0, 0, 0, 0]
stats_artur = [0, 0, 0, 0]

# computar atributos
for i in range(8):
    frase = input()
    idx_atributo, pontos = analisar_atributos(frase)

    if i % 2 == 0:
        personagem = personagem_caesar
        stats_ceasar[idx_atributo] = pontos

    else:
        personagem = personagem_artur
        stats_artur[idx_atributo] = pontos

    if (idx_atributo != 3) or (idx_atributo == 3 and pontos != 0):
        print(f"Computando {lista_atributos_geral[idx_atributo]} de {personagem}: {pontos}")

# print dos atributos
print(f"\n{personagem_caesar}: Força física: {stats_ceasar[0]}\nAgilidade: {stats_ceasar[1]}\nKi: {stats_ceasar[2]}")
if stats_ceasar[3] != 0:
    print(f"Transformação em Super Saiyajin: {stats_ceasar[3]}")

print()

print(f"{personagem_artur}: Força física: {stats_artur[0]}\nAgilidade: {stats_artur[1]}\nKi: {stats_artur[2]}")
if stats_artur[3] != 0:
    print(f"Transformação em Super Saiyajin: {stats_artur[3]}")

print()

# ----------------------------------------------------- #
# início da batalha

# status de combate de cada um dos lutadores
forca_c = stats_ceasar[0]
agilidade_c = stats_ceasar[1]
ki_c = stats_ceasar[2]
ssj_c = stats_ceasar[3]

vida_c = (ki_c + forca_c) * (1 + ssj_c)
ataque_c = forca_c * (1 + ssj_c) * 5
energia_c = ki_c * (1 + ssj_c)
velocidade_c = 1 + agilidade_c // 100

forca_a = stats_artur[0]
agilidade_a = stats_artur[1]
ki_a = stats_artur[2]
ssj_a = stats_artur[3]

vida_a = (ki_a + forca_a) * (1 + ssj_a)
ataque_a = forca_a * (1 + ssj_a) * 5
energia_a = ki_a * (1 + ssj_a)
velocidade_a = 1 + agilidade_a // 100

# inicialização e print da matriz
ordem_matriz = int(input())

matriz = []

for i in range(ordem_matriz):
    matriz.append([])
    for j in range(ordem_matriz):
        if i == 0 and j == 0: # personagem de caesar
            matriz[i].append(personagem_caesar[0])
        elif i == ordem_matriz - 1 and j == ordem_matriz - 1: # personagem de artur
            matriz[i].append(personagem_artur[0])
        else:
            matriz[i].append('0')

pos_c = [0, 0]
pos_a = [ordem_matriz - 1, ordem_matriz - 1]

# início da simulação da batalha
print(f"Iniciando simulação de batalha: {personagem_caesar} VS {personagem_artur}!")
print_matriz(matriz)

turno_atual = 'caesar'
if agilidade_a > agilidade_c:
    turno_atual = 'artur'

vencedor = ''
perdedor = ''
motivo_vitoria = ''

while (vida_c > 0 and energia_c > 0) and (vida_a > 0 and energia_a > 0):
    # define personagem ativo
    if turno_atual == 'caesar':
        personagem_ativo_nome = personagem_caesar  
    else:
        personagem_ativo_nome = personagem_artur

    acao = input().lower()

    if turno_atual == 'caesar': # turno de caesar
        if acao == 'ataque de ki':
            energia_gasta = int(input())
            print(f"{personagem_caesar} está concentrando seu ki em um devastador ataque de energia!")
            if calcular_distancia(pos_c, pos_a) <= 5:
                if energia_c >= energia_gasta:
                    energia_c -= energia_gasta
                    vida_a -= energia_gasta
                    if vida_a < 0:
                        vida_a = 0
                if vida_a > 0:
                    print(f"{personagem_artur} sofreu um ataque, e agora está com {vida_a} de vida")


        elif acao == 'mover':
            direcao = input()
            quantidade = int(input())
            pos_c = realizar_movimentacao(matriz, pos_c, direcao, quantidade, velocidade_c, personagem_caesar[0])
            if agilidade_c > agilidade_a:
                print(f"{personagem_caesar} se move com uma agilidade impressionante! Será que seu oponente poderá acompanhar sua velocidade?")
            print_matriz(matriz)
        
        elif acao == 'soco':
            if calcular_distancia(pos_c, pos_a) == 1:
                if ataque_c > ataque_a:
                    print(f"{personagem_caesar} acerta um poderoso golpe! O oponente pode sentir o peso de cada ataque")
                vida_a -= ataque_c
                if vida_a > 0:
                    print(f"{personagem_artur} sofreu um ataque, e agora está com {vida_a} de vida")
                if vida_a < 0:
                    vida_a = 0
        
        elif acao == 'power up':
            print("AAAAAAAAAAAAAAAAAAAAAAAAAHHHHH!!!")
            conseguiu = input()
            if conseguiu.lower() == 'sim':
                ataque_c *= 2
                energia_c *= 2

    else: # ação de artur
        if acao == 'ataque de ki':
            energia_gasta = int(input())
            print(f"{personagem_artur} está concentrando seu ki em um devastador ataque de energia!")
            if calcular_distancia(pos_a, pos_c) <= 5:
                if energia_a >= energia_gasta:
                    energia_a -= energia_gasta
                    vida_c -= energia_gasta
                    if vida_c < 0:
                        vida_c = 0
                if vida_c > 0:
                    print(f"{personagem_caesar} sofreu um ataque, e agora está com {vida_c} de vida")

                    
        elif acao == 'mover':
            direcao = input()
            quantidade = int(input())
            pos_a = realizar_movimentacao(matriz, pos_a, direcao, quantidade, velocidade_a, personagem_artur[0])
            if agilidade_a > agilidade_c:
                print(f"{personagem_artur} se move com uma agilidade impressionante! Será que seu oponente poderá acompanhar sua velocidade?")
            print_matriz(matriz)

        elif acao == 'soco':
            if calcular_distancia(pos_a, pos_c) == 1:
                if ataque_a > ataque_c:
                    print(f"{personagem_artur} acerta um poderoso golpe! O oponente pode sentir o peso de cada ataque")
                vida_c -= ataque_a
                if vida_c > 0:
                    print(f"{personagem_caesar} sofreu um ataque, e agora está com {vida_c} de vida")
                if vida_c < 0:
                    vida_c = 0

        elif acao == 'power up':
            print("AAAAAAAAAAAAAAAAAAAAAAAAAHHHHH!!!")
            conseguiu = input()
            if conseguiu.lower() == 'sim':
                ataque_a *= 2
                energia_a *= 2

    # alterna o turno
    if turno_atual == 'caesar':
        turno_atual = 'artur'  
    else:
        turno_atual = 'caesar'

# fim de batlaha
print("TEMOS UM VENCEDOR!")

# determina o vencedor e o motivo
if vida_a <= 0:
    vencedor = personagem_caesar
    perdedor = personagem_artur
    energia_vencedor = energia_c

    if energia_vencedor > 0:
        print(f"{vencedor} nem precisou se esforçar nessa luta, Artur! Da proxima vez vê se você escolhe um oponente realmente forte") #
    else: # caesar venceu mas zerou a energia
        print(f"Ok, pode ter sido uma luta acirrada, mas {vencedor} nunca desaponta!")

elif vida_c <= 0:
    vencedor = personagem_artur
    perdedor = personagem_caesar
    energia_vencedor = energia_a

    if energia_vencedor > 0:
        print(f"Essa luta nem deu pro gasto, já estava claro que {vencedor} ia ganhar!")
    else: # artur venceu mas zerou a energia
        print(f"Foi uma boa luta, mas {vencedor} mostrou que era o melhor afinal!")

else:
    if energia_a == 0:
        vencedor = personagem_caesar
        perdedor = personagem_artur
        print(f"{vencedor} faz qualquer luta parecer fácil, mas essa aqui fez o {perdedor} passar vergonha!")

    elif energia_c == 0:
        vencedor = personagem_artur
        perdedor = personagem_caesar
        print(f"A diferença de poder era tanta que {vencedor} mal precisou encostar no {perdedor} e já ganhou")