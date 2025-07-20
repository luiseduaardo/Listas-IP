# função para verificar se o número é fatorial
def eh_fatorial_checker(n, k=1, fat=1):
    if fat == n: # caso base 1: retorna verdade se o número for igual ao fatorial
        return True
    
    elif fat > n: # caso base 2: retorna falso se o fatorial ultrapassar o valor que quero comparar
        return False
    
    else: # recursivo: calcula próximo fatorial
        return eh_fatorial_checker(n, k + 1, fat * (k + 1))

# função para verificar se o número faz parte da seq de tribonacci
def eh_tribonacci_checker(n, a=0, b=1, c=1):
    if c == n or n == 0 or n == 1: # caso base 1: retorna verdade se o número for igual ao número de tribonacci
        return True
    
    elif c > n: # caso base 2: retorna falso se o número de tribonacci ultrapassou o número que eu quero comparar
        return False
    
    else: # recursivo: calcula próximo tribonacci e atribui valores novos às antigas variáveis de tribonacci
        return eh_tribonacci_checker(n, b, c, a + b + c)

# função fatorial para ajudar na sequência de catalan (poderia ter usado antes também, mas achei melhor assim)
def fatorial(num):
    if num <= 1: # caso base: 0 ou 1 - retorna 1
        return 1
    
    else: # recursivo: calcula fatorial
        return num * fatorial(num - 1)

# função para calcular a sequência de catalan
def calcula_catalan(n):
    if n == 0: # caso base 1: elemento 0 = 1
        return 1
    
    else: # recursivo: calcula com base na fórmula (2n)! / ((n+1)! . n!)
        return fatorial(2 * n) // (fatorial(n + 1) * fatorial(n))

# função para definir se o numero alvo faz parte da sequência de catalan
def eh_catalan_checker(alvo, n=0):
    c_atual = calcula_catalan(n)

    if c_atual == alvo: # caso base 1: retorna o índice da seq de catalan o numero pertence
        return n
    
    elif c_atual > alvo: # caso base 2: retorna -1 se o numero da sequência ultrapassou o número que defini como alvo, ou seja, esse número não faz parte da sequência
        return -1
    
    else: # recursivo: prossegue pro próximo número da seq de catalan
        return eh_catalan_checker(alvo, n + 1)

# verifica se três números seguidos fazem parte da seq de catalan
def verifica_sequencia_catalan(numeros_runa, i=0):
    if i > len(numeros_runa) - 3: # caso base: sequência não tem mais trios possíveis para escolher
        return [False, []]

    n1, n2, n3 = numeros_runa[i], numeros_runa[i+1], numeros_runa[i+2]
    
    # faz na prática a verificação e retorna verdadeiro se a sequência de três faz parte da sequência de catalan
    idx1 = eh_catalan_checker(n1)
    if idx1 != -1:
        c_next = calcula_catalan(idx1 + 1)
        c_next_next = calcula_catalan(idx1 + 2)
        if n2 == c_next and n3 == c_next_next:
            return [True, [n1, n2, n3]]
        
        if n1 == 1: # caso em que 1 é o primeiro e segundo número da sequência (1, 1, 2, 5) - testcase oculto que tava dando errado
            c2_alt = calcula_catalan(1 + 1)
            c3_alt = calcula_catalan(1 + 2)
            if n2 == c2_alt and n3 == c3_alt:
                return [True, [n1, n2, n3]]
    
    # recursivamente volta para o início da função caso ainda existam trios possíveis de escolher e o que foi verificado agora não fazia parte da sequência de catalan
    return verifica_sequencia_catalan(numeros_runa, i + 1)

def batalha(turno, vida_maculado, vida_maxima, vida_inimigo, armas, nome_inimigo, dano_inimigo, nome_runa_ativa):
    if vida_maculado <= 0:
        print("You Died")
        print(f"Droga acabei morrendo para a/o {nome_inimigo} e ele ainda tem {vida_inimigo} pontos de vida, vou ter que trazer armas mais fortes da próxima vez.")
        return

    if vida_inimigo <= 0:
        print("Great Enemy Felled")
        if len(armas) == 0:
            print(f"Acabei usando tudo que eu trouxe, mas finalmente consegui derrotar a/o {nome_inimigo}.")
        else:
            print(f"Finalmente depois de tanto me preparar consegui derrotar a/o {nome_inimigo}.")
            nomes_armas_restantes = []
            for arma in armas:
                nomes_armas_restantes.append(arma[0])
            armas_str = ", ".join(nomes_armas_restantes)
            print(f"Acho que me preparei bem eu ainda tenho {len(armas)} arma/as sobrando são ela/as: {armas_str}.")
        return

    if len(armas) == 0:
        print(f"Parece que eu não me preparei o suficiente, acabei usando tudo que tinha e a/o {nome_inimigo} ainda tem {vida_inimigo} pontos de vida, vou ter que me preparar mais da próxima vez.")
        return
        
    print(f"{turno}° TURNO")
    print(f"Melhor conferir meus status antes de lutar -> vida: ({vida_maculado}/{vida_maxima})")
    print(f"E o {nome_inimigo} ainda está com {vida_inimigo} pontos de vida")
    
    arma_atual = armas[0]
    armas_restantes = armas[1:]
    nome_arma_usada = arma_atual[0]
    dano_causado = arma_atual[1]
    
    print(f"Atacando com {nome_arma_usada}.")
    vida_inimigo -= dano_causado
    print(f"Consegui causar {dano_causado} de dano no/a {nome_inimigo}!!!")
    print(f"Acabei consumindo a/o {nome_arma_usada}, hora de pegar outra arma do arsenal.")

    if nome_runa_ativa == "Grande Runa de Malenia" and vida_inimigo > 0 and vida_maculado < vida_maxima:
        cura_potencial = int(0.05 * vida_maxima)
        espaco_para_curar = vida_maxima - vida_maculado
        valor_de_cura = min(cura_potencial, espaco_para_curar)
        vida_maculado += valor_de_cura
        print(f"Ainda bem que eu ativei a Grande Runa da Malenia, consegui recuperar {valor_de_cura}")
    
    if vida_inimigo > 0:
        vida_maculado -= dano_inimigo
        print(f"Droga {nome_inimigo} ainda não morreu, acabei recebendo {dano_inimigo} de dano.")

    print()
    batalha(turno + 1, vida_maculado, vida_maxima, vida_inimigo, armas_restantes, nome_inimigo, dano_inimigo, nome_runa_ativa)

# script principal

info_maculado = input().split(" - ")
nome_maculado = info_maculado[0]
vida_maculado = int(info_maculado[1])
vida_maxima = vida_maculado

qtd_total_acoes = int(input())

lista_de_armas = []
nome_runa_ativa = ""

for i in range(qtd_total_acoes):
    entrada_acao = input()

    if " - " in entrada_acao:
        info_arma = entrada_acao.split(" - ")
        nome_arma = info_arma[0]
        dano_arma = float(info_arma[1])
        tipo_arma = info_arma[2]
        
        print(f"Vou levar a/o {nome_arma} ela/e vai ser de grande ajuda.")
        print("Hora de Aprimorar!!!")
        
        nivel_arma = 0
        aprimorou = False
        fim_loop = False
        while not fim_loop:
            entrada_num = input()
            if entrada_num == "fim":
                fim_loop = True

            if not fim_loop:
                num_aprimoramento = int(entrada_num)
                sucesso = False
                
                if tipo_arma == "basica" and nivel_arma < 20:
                    if eh_tribonacci_checker(num_aprimoramento):
                        sucesso = True
                        dano_arma *= 1.10
                elif tipo_arma == "especial" and nivel_arma < 10:
                    if eh_fatorial_checker(num_aprimoramento):
                        sucesso = True
                        dano_arma *= 1.20
                
                if sucesso:
                    aprimorou = True
                    nivel_arma += 1
                    print(f"Pronto, consegui mais um nível agora a/o {nome_arma} está no nível {nivel_arma}!")
            
        if aprimorou:
            print(f"Agora sim! Acho que a/o {nome_arma} está forte o suficiente, consegui colocar ele/a para o nível {nivel_arma}")
        else:
            print(f"Droga não consegui aumentar o nível da/o {nome_arma}")
        
        lista_de_armas.append([nome_arma, int(dano_arma)])

    else:
        nome_runa = entrada_acao
        frases_efeito = [
            ["Grande Runa de Godrick", "acho que um pouco de tudo não é nada mal."],
            ["Grande Runa de Radahn", "mais vida vai ajudar muito."],
            ["Grande Runa de Morgott", "quanto mais vida melhor."],
            ["Grande Runa de Malenia", "ela foi tão difícil de conseguir, tenho que testar ela pelo menos uma vez."]
        ]
        frase_runa = ""
        for item in frases_efeito:
            if item[0] == nome_runa:
                frase_runa = item[1]

        print("A batalha vai ser difícil melhor tentar ativar uma runa!")
        print(f"Me decidi vou tentar ativar a {nome_runa}, {frase_runa}")
        
        numeros_runa = []
        for i in range(10):
            numeros_runa.append(int(input()))
            
        resultado_ativacao = verifica_sequencia_catalan(numeros_runa)
        ativou = resultado_ativacao[0]
        
        if ativou:
            nome_runa_ativa = nome_runa
            numeros_encontrados = resultado_ativacao[1]
            print("Isso consegui ativar a Grande Runa.")
            print(f"Acabei precisando apenas dos números: {numeros_encontrados[0]} - {numeros_encontrados[1]} - {numeros_encontrados[2]}.")
        else:
            print("Caramba não consegui ativar a Grande Runa, infelizmente vou ter que me contentar com as armas que vou levar.")

    print()

if nome_runa_ativa == "Grande Runa de Radahn":
    vida_maxima = round(vida_maxima * 1.15)
elif nome_runa_ativa == "Grande Runa de Morgott":
    vida_maxima = round(vida_maxima * 1.25)
elif nome_runa_ativa == "Grande Runa de Godrick":
    vida_maxima = round(vida_maxima * 1.10)
    for arma in lista_de_armas:
        arma[1] = int(arma[1] * 1.10)

vida_maculado = vida_maxima

info_inimigo = input().split(" - ")
nome_inimigo = info_inimigo[0]
vida_inimigo = int(info_inimigo[1])
dano_inimigo = int(info_inimigo[2])

batalha(1, vida_maculado, vida_maxima, vida_inimigo, lista_de_armas, nome_inimigo, dano_inimigo, nome_runa_ativa)
