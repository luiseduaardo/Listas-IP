def print_escolha_chefao(chefao):
    if chefao == 'Sif, a Grande Loba Cinzenta':
        print("Venha até mim guardiã do túmulo de Artorias... Vamos acabar logo com isso!")
        return 3432, 35
    
    elif chefao == 'Gwyn, Lorde das Cinzas':
        print("Enfim estou de frente ao Senhor das Cinzas! Nossa batalha será lendária e ecoará em todos os cantos de Lordran!!!")
        return 4185, 55
    
def batalha(tentativa, vida_player, dps_player, vida_boss, dps_boss, xp, boss, inicial_chefao):
    player_venceu = luta_por_turno(vida_player, vida_boss, dps_player, dps_boss, boss, False, False, inicial_chefao)

    if player_venceu:
        return tentativa
    else:
        if xp == 'Iniciante':
            dps_player *= 1.05
            dps_boss *= 0.90

        elif xp == 'Veterano':
            dps_player *= 1.10
            dps_boss *= 0.80

        elif xp == 'Mestre do Souls':
            dps_player *= 1.20
            dps_boss *= 0.67

        return batalha(tentativa + 1, vida_player, dps_player, vida_boss, dps_boss, xp, boss, inicial_chefao)


def luta_por_turno(vida_p, vida_b, dps_p, dps_b, boss_name, sif_ferido, gwyn_chamas, v0_chefao):
    vida_b = vida_b - dps_p

    if vida_b <= 0:
        return True

    if boss_name == 'Sif, a Grande Loba Cinzenta' and vida_b < (v0_chefao * 0.1) and not sif_ferido:
        print("Sif, a Grande Loba Cinzenta está gravemente ferida! Essa é sua chance, acabe com o sofrimento dela!")
        dps_b -= 15
        sif_ferido = True
    
    elif boss_name == 'Gwyn, Lorde das Cinzas' and vida_b < (v0_chefao * 0.5):
        gwyn_chamas = True

    vida_p = vida_p - dps_b

    if gwyn_chamas:
        vida_p -= 10

    if vida_p <= 0:
        return False

    return luta_por_turno(vida_p, vida_b, dps_p, dps_b, boss_name, sif_ferido, gwyn_chamas, v0_chefao)

def prints_finais(n_tent, chefe, xp):
    print(f"Você precisou de {n_tent} tentativas para vencer o(a) {chefe}!")

    if xp == 'Iniciante':
        if n_tent <= 5:
            print("Esse iniciante teve muita sorte, no próximo boss ele vai conhecer a verdadeira DOR!!!")
        elif 5 < n_tent <= 10:
            print("Até que não foi tão ruim assim, continue assim novato!")
        else:
            print("Bem vindo a Dark Souls.")
    elif xp == 'Veterano':
        if n_tent <= 5:
            print("Você já andou por Lordran antes, não é? Impressionante.")
        elif 5 < n_tent <= 10:
            print("Nada mal, guerreiro. Mas os próximos desafios não terão piedade.")
        else:
            print("Mesmo os veteranos sangram em Dark Souls...")
    elif xp == 'Mestre do Souls':
        if n_tent == 1:
            print("Inacreditável. Um verdadeiro Mestre do Souls. Está destinado a se tornar o Dark Lord!")
        elif 1 < n_tent <= 10:
            print("Seu conhecimento sobre o ciclo é profundo. Quase como se já tivesse vivido isso mil vezes...")
        else:
            print("Nem mesmo os Mestres escapam ilesos da chama...")
    
    if chefe == 'Sif, a Grande Loba Cinzenta':
        print("A grande loba cai com honra. No fundo dos seus olhos, havia apenas lealdade.")
    
    elif chefe == 'Gwyn, Lorde das Cinzas':
        print("A chama se apaga, e o silêncio reina em Lordran. Você derrotou o Senhor das Cinzas...")

        if n_tent == 1:
            print("O ciclo foi quebrado... Você se tornou o verdadeiro Senhor das Cinzas. Um novo destino começa...")
        else:
            print(f"Mas o ciclo... o ciclo continua.")

experiencia = input()
stats = input().split(' ')
vitalidade, forca = int(stats[0]), int(stats[1])

vida_inicial = vitalidade * 20
dps_inicial = forca * 5

nome_chefao = input()

vida_inicial_chefao, dps_inicial_chefao = print_escolha_chefao(nome_chefao)
tent_total = batalha(1, vida_inicial, dps_inicial, vida_inicial_chefao, dps_inicial_chefao, experiencia, nome_chefao, vida_inicial_chefao)
prints_finais(tent_total, nome_chefao, experiencia)