# Variáveis globais
incremento = F_acumulada = tempo = contador_rebatidas = 0
acabar = False

# Input de atributos de cada jogador
F_max = int(input())
forca_inicial = int(input())
nivel = str(input())
forca_media_jogador = int(input())

print("Robô Hugo 4.0 foi inicializado…")

# Output e incremento com base no nível
if nivel == 'facil':
    incremento = 1
    print("Iniciando no modo iniciante... Ótimo para aquecer os motores!")
elif nivel == 'medio':
    incremento = 3
    print("Você escolheu o modo intermediário. Hora de mostrar técnica e estratégia!")
elif nivel == 'dificil':
    incremento = 5
    print("Modo lendário ativado! Hugo 4.0 está a todo vapor — prepare-se para o combate definitivo!")

# Laço de repetição (a partir da rebatida 2)
while not acabar:
    tempo += 1
    contador_rebatidas = tempo
    F_rebatida = forca_inicial + (tempo * incremento)

    if F_rebatida > 150:
        acabar = True
        print("Bola fora! A força da rebatida excedeu os limites da mesa.")
    
    else:
        F_acumulada += F_rebatida
        print(f"Rebatida {contador_rebatidas}: força = {F_rebatida}, força acumulada = {F_acumulada}")
        if F_acumulada > F_max:
            acabar = True
            print("Energia do robô esgotada! Encerrando o confronto…")

# Fim da partida
print("Partida finalizada! Estas são as estatísticas do embate:")
if tempo > 0:
    forca_media_robo = F_acumulada // tempo
else:
    forca_media_robo = 0
print(f"O robô realizou {contador_rebatidas} rebatidas em {tempo} segundos, com força total de {F_acumulada}.")
print(f"Força média do robô: {forca_media_robo}")
print(f"Força média do jogador: {forca_media_jogador}")

# Declarar vencedor
if forca_media_jogador > forca_media_robo:
    print("Vitória do jogador! O talento humano ainda é imbatível!")
elif forca_media_robo > forca_media_jogador:
    print("Vitória do Hugo 4.0! O robô mostrou quem manda na quadra!")
else:
    print("Empate técnico! Um duelo digno de mestres do tênis de mesa.")
