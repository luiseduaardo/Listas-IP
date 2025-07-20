# ação de genichiro
def get_acao_genichiro():
    acao = input()
    acoes_validas = ["ataque", "defesa", "recuperação de postura", "ataque kanji"]
    if acao in acoes_validas: # caso base - ação escolhida foi válida
        return acao
    
    print("Genichiro não tem esse movimento em seu arsenal.")
    return get_acao_genichiro() # chama a própria função caso não seja escolhida uma ação válida

# ação do lobo - definida com base nas permissões da rodada
def get_acao_sekiro(acoes_validas):
    acao = input()
    if acao in acoes_validas: # caso base - ação escolhida foi válida
        return acao
    
    print("O lobo não adquiriu esse movimento ainda.")
    return get_acao_sekiro(acoes_validas) # chama a própria função caso não seja escolhida uma ação válida

def simulador_de_combate(sekiro_vit, sekiro_pos, sekiro_cab, genichiro_vit, genichiro_pos, turno, genichiro_vulneravel):
    if sekiro_vit <= 0:
        print("Sekiro cai de joelhos, derrotado...")
        print("====================================")
        print("Vitória de Genichiro: Morte.")
        return

    if sekiro_pos >= 100:
        print("A postura do lobo foi quebrada! Ele não consegue se defender e é derrotado!")
        print("====================================")
        print("Vitória de Genichiro: Morte.")
        return
    
    print(f"--- Turno {turno} ---")

    if genichiro_vulneravel:
        print("Genichiro está de joelhos e vulnerável! Acabe com isso, Lobo!")
        
        acao_final = get_acao_sekiro(["ataque", "hesitar"])

        if acao_final == "ataque":
            print("Sekiro executa um Golpe Mortal em Genichiro!")
            print("====================================")
            print("Vitória de Sekiro: Golpe Mortal!")
            return
        
        if acao_final == "hesitar":
            print("O lobo hesitou no seu golpe final, Genichiro recupera sua postura! Cuidado, Lobo!")
            
            if genichiro_vit <= 0:
                genichiro_vit = 50
                genichiro_pos = 50
            else:
                genichiro_pos = genichiro_pos - 50
                if genichiro_vit < 50:
                    genichiro_vit = 50
            
            simulador_de_combate(sekiro_vit, sekiro_pos, sekiro_cab, genichiro_vit, genichiro_pos, turno + 1, False)
            return
    
    acao_genichiro = get_acao_genichiro()
    acao_sekiro = get_acao_sekiro(["ataque", "defesa", "defesa perfeita", "usar cabaça", "desviar", "contra ataque mikiri"])
    
    if acao_genichiro == "ataque":
        if acao_sekiro == "ataque":
            sekiro_vit -= 25; genichiro_vit -= 10; genichiro_pos += 15
            print("Clima de tensão! Os dois atacam numa luta implacável!")
        elif acao_sekiro == "defesa":
            sekiro_vit -= 10; sekiro_pos += 20
            print("Sekiro firma sua espada e se defende, absorvendo o impacto em sua postura!")
        elif acao_sekiro == "defesa perfeita":
            genichiro_pos += 25
            print("Lâminas se encontram! Um desvio perfeito de Sekiro desequilibra Genichiro!")
        elif acao_sekiro == "usar cabaça":
            if sekiro_cab > 0:
                sekiro_cab -= 1; sekiro_vit -= 25
                print("Sekiro tenta curar, mas é punido pelo ataque impiedoso de Genichiro!")
            else:
                sekiro_vit -= 25
                print("Sekiro busca sua cabaça, mas ela está vazia!")
                print("Enquanto Sekiro se distrai, Genichiro avança com um ataque certeiro!")
        elif acao_sekiro == "desviar":
            print("O lobo desvia agilmente do ataque comum de Genichiro!")
        elif acao_sekiro == "contra ataque mikiri":
            genichiro_pos += 10
            print("O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro faz um movimento comum.")
    
    elif acao_genichiro == "defesa":
        if acao_sekiro == "ataque":
            genichiro_pos += 5
            print("Genichiro prevê o movimento e apara o golpe de Sekiro com sua lâmina!")
        elif acao_sekiro == "defesa":
            print("Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.")
        elif acao_sekiro == "defesa perfeita":
            print("Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.")
        elif acao_sekiro == "usar cabaça":
            if sekiro_cab > 0:
                sekiro_vit += 25; sekiro_cab -= 1
                print("Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.")
            else:
                print("Sekiro busca sua cabaça, mas ela está vazia!")
                print("Genichiro mantém a guarda, enquanto o lobo percebe seu erro.")
        elif acao_sekiro == "desviar":
            print("O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.")
        elif acao_sekiro == "contra ataque mikiri":
            print("O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.")

    elif acao_genichiro == "recuperação de postura":
        if acao_sekiro == "ataque":
            genichiro_vit -= 10; genichiro_pos += 15
            print("Genichiro ia recuperar sua postura mas o lobo foi mais rápido, um grande ataque por parte do lobo!")
        else:
            genichiro_pos = 0
            if acao_sekiro == "defesa":
                print("Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.")
                print("Genichiro consegue recuperar sua postura, cuidado lobo!")
            elif acao_sekiro == "defesa perfeita":
                print("Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.")
                print("Genichiro consegue recuperar sua postura, cuidado lobo!")
            elif acao_sekiro == "usar cabaça":
                if sekiro_cab > 0:
                    sekiro_vit += 25; sekiro_cab -= 1
                    print("Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.")
                else:
                    print("Sekiro busca sua cabaça, mas ela está vazia!")
                    print("Genichiro aproveita a hesitação do lobo para recuperar sua postura.")
                print("Genichiro consegue recuperar sua postura, cuidado lobo!")
            elif acao_sekiro == "desviar":
                print("O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.")
                print("Genichiro consegue recuperar sua postura, cuidado lobo!")
            elif acao_sekiro == "contra ataque mikiri":
                print("O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.")
                print("Genichiro consegue recuperar sua postura, cuidado lobo!")

    elif acao_genichiro == "ataque kanji":
        if acao_sekiro == "contra ataque mikiri":
            genichiro_pos += 25
            print("O lobo utiliza a técnica de contra ataque mikiri e pisa na arma de Genichiro!")
        elif acao_sekiro == "desviar":
            print("O lobo desvia do ataque especial de Genichiro com muita agilidade!")
        elif acao_sekiro == "usar cabaça":
            sekiro_vit -= 50; sekiro_pos += 20
            if sekiro_cab > 0:
                sekiro_cab -= 1
                print("O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!")
            else:
                print("O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!")
                print("Para piorar, Sekiro nem sequer tinha uma cabaça para usar!")
        else:
            sekiro_vit -= 50; sekiro_pos += 20
            print("O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!")
            
    if sekiro_vit > 100:
        sekiro_vit = 100
    if sekiro_pos < 0:
        sekiro_pos = 0
    if genichiro_pos < 0:
        genichiro_pos = 0

    proximo_turno_vulneravel = genichiro_vit <= 0 or genichiro_pos >= 100
    
    simulador_de_combate(sekiro_vit, sekiro_pos, sekiro_cab, genichiro_vit, genichiro_pos, turno + 1, proximo_turno_vulneravel)

print("O duelo começa! Suas decisões determinarão o vencedor.")

simulador_de_combate(
    sekiro_vit=100,
    sekiro_pos=0,
    sekiro_cab=2,
    genichiro_vit=100,
    genichiro_pos=0,
    turno=1,
    genichiro_vulneravel=False
)
