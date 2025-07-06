def calcula_dano(golpe, motivacao):
    if golpe == 'Normal':
        return 20 * motivacao
    elif golpe == 'Potente':
        return 40 * motivacao

def combate_simulado(oponente, vida_inicial_oponente, motivacao_oponente, motivacao_vegeta):
    print(f"--- Iniciando o combate contra {oponente} ---\n")

    vida_vegeta = 100
    golpe_anterior_vegeta = ''
    vida_oponente = vida_inicial_oponente

    numero_do_turno = 1

    while vida_vegeta > 0 and vida_oponente > 0:
        print(f"--- Turno {numero_do_turno} ---")
        acabar_turno = False

        contador_de_vez = 0
        while not acabar_turno:
            acao = input()

            if contador_de_vez % 2 == 0:
                lutador = 'Vegeta'
                if acao == 'Potente' and golpe_anterior_vegeta == 'Potente':
                    print("Vegeta usou dois Golpes Potentes seguidos e desmaiou com o esforço!")
                    vida_vegeta = 0

                    print(f"|Vegeta: {vida_vegeta} HP vs {oponente}: {vida_oponente} HP|\n")
                    print(f"Vegeta foi derrotado! A Terra está a salvo graças a {oponente}!")

                    acabar_turno = True

                    return motivacao_vegeta, True
            
                else:
                    dano_vegeta = int(calcula_dano(acao, motivacao_vegeta))
                    vida_oponente -= dano_vegeta

                    if vida_oponente < 0:
                        vida_oponente = 0

                    print(f"{lutador} usou Golpe {acao} e causou {dano_vegeta} de dano!")

                    golpe_anterior_vegeta = acao

                    if vida_oponente == 0:
                        print(f"|Vegeta: {vida_vegeta} HP vs {oponente}: {vida_oponente} HP|\n")
                        print(f"Vitória de Vegeta!\nVegeta venceu a batalha contra {oponente} com {vida_vegeta} HP restantes!\n")

                        motivacao_vegeta *= (1 + (vida_vegeta / vida_inicial_oponente))

                        acabar_turno = True

                        return motivacao_vegeta, False
            
            else:
                lutador = oponente

                dano_oponente = int(calcula_dano(acao, motivacao_oponente))
                vida_vegeta -= dano_oponente

                if vida_vegeta < 0:
                    vida_vegeta = 0
                
                print(f"{lutador} usou Golpe {acao} e causou {dano_oponente} de dano!")

                if vida_vegeta == 0:
                    print(f"|Vegeta: {vida_vegeta} HP vs {oponente}: {vida_oponente} HP|\n")
                    print(f"Vegeta foi derrotado! A Terra está a salvo graças a {lutador}!")

                    acabar_turno = True

                    return motivacao_vegeta, True

            if contador_de_vez == 1:
                acabar_turno = True

            contador_de_vez += 1
        
        print(f"|Vegeta: {vida_vegeta} HP vs {oponente}: {vida_oponente} HP|\n")
        
        numero_do_turno += 1


nomes_oponentes = ['Piccolo', 'Gohan', 'Goku']
lista_vida_inicial_oponentes = [100, 100, 200]

vegeta_perdeu = False
contador_oponentes = 0

print("A saga de Vegeta começa!\n")

motivacao_inicial_vegeta = float(input())

while not vegeta_perdeu and contador_oponentes < len(nomes_oponentes):
    oponente_da_vez = nomes_oponentes[contador_oponentes]
    vida_inicial_da_vez = lista_vida_inicial_oponentes[contador_oponentes]
    motivacao_guerreiroZ = float(input())

    motivacao_vegeta, vegeta_perdeu = combate_simulado(oponente_da_vez, vida_inicial_da_vez, motivacao_guerreiroZ, motivacao_inicial_vegeta)

    motivacao_inicial_vegeta = motivacao_vegeta

    contador_oponentes += 1

if not vegeta_perdeu:
    print(f"Vegeta derrotou todos os Guerreiros Z! A Terra foi conquistada!")
