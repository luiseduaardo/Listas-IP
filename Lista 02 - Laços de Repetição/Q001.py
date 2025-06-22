# Variáveis globais
ataque = defesa = 0
errou = False

# Input das bolas rebatidas
rebatidas = int(input())

print("------- Início do Treino -------")

# Laço de repetição para a quantidade de bolas
for i in range(rebatidas):
    # Input do tipo de bola e golpe executado
    bola_lancada = input()
    golpe_executado = input()

    # Condicionais para cada tipo de bola e golpe
    if golpe_executado == 'Errou':
        errou = True
        print("Você errou! Levanta a cabeça que ainda tem mais.")
        if bola_lancada == 'Defesa':
            defesa -= 10
        elif bola_lancada == 'Ataque':
            ataque -= 10

    else:
        print(f"Você conseguiu rebater uma bola de {bola_lancada}! Golpe executado: {golpe_executado}.")
        if bola_lancada == 'Defesa':
            if golpe_executado == 'Chop':
                defesa += 10
            elif golpe_executado == 'Push':
                defesa += 5

        elif bola_lancada == 'Ataque':
            if golpe_executado == 'Topspin':
                ataque += 5
            elif golpe_executado == 'Smash':
                ataque += 10

# Evita que um dos valores seja 0
if ataque < 0:
    ataque = 0

if defesa < 0:
    defesa = 0

# Condicional inicial
if ataque > defesa:
    print("Ter um bom jogo ofensivo será fundamental para ganhar o InterCin!")
elif defesa > ataque:
    print("Defesa ganha campeonatos! Agora sim estou preparado.")
else:
    print("Foi um treino equilibrado.")

if errou:
    print("Infelizmente não foi um treino perfeito, mas pude melhorar muito.")

# Atributos finais
print("------- Atributos -------")
print(f"Ataque: {ataque}\nDefesa: {defesa}")
