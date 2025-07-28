qtd_grupos = int(input())

if qtd_grupos < 2 or qtd_grupos % 2 == 1:
    print(f"Mas como que vamos fazer um torneio com {qtd_grupos} grupos Samir!?")

else:
    print("Roda os dados Samir!")
    
    passaram_de_fase = []
    rebaixados = []

    for i in range(qtd_grupos):
        grupo = dict()
        primeiro_do_grupo = ''
        segundo_do_grupo = ''
        pontos_primeiro = pontos_segundo = 0
        ultimo_time = ''
        pontos_ultimo = 100 # definido arbitrariamente
        for j in range(4):
            time, pontuacao = input().split(' - ')
            pontuacao = int(pontuacao)
            if pontuacao > pontos_primeiro:
                pontos_segundo = pontos_primeiro
                segundo_do_grupo = primeiro_do_grupo

                pontos_primeiro = pontuacao
                primeiro_do_grupo = time
            
            elif pontuacao > pontos_segundo:
                pontos_segundo = pontuacao
                segundo_do_grupo = time

            if pontuacao < pontos_ultimo:
                pontos_ultimo = pontuacao
                ultimo_time = time

        grupo.update({'primeiro': primeiro_do_grupo, 'segundo': segundo_do_grupo})

        rebaixados.append(ultimo_time)
        passaram_de_fase.append(grupo)

    cruzamentos = []
    chaves_existentes = qtd_grupos // 2

    for k in range(chaves_existentes):
        grupo_a, grupo_b = input().split(' x ')
        cruzamentos.append((int(grupo_a) - 1, int(grupo_b) - 1))

    chave_atual = 1
    for times in cruzamentos:
        primeiro_a = passaram_de_fase[times[0]]['primeiro']
        primeiro_b = passaram_de_fase[times[1]]['primeiro']
        segundo_a = passaram_de_fase[times[0]]['segundo']
        segundo_b = passaram_de_fase[times[1]]['segundo']


        print(f"\nConfrontos chave {chave_atual}:")

        print(f"{primeiro_a} x {segundo_b}")
        print(f"{segundo_a} x {primeiro_b}")

        chave_atual += 1

    print()

    for time in rebaixados:
        print(f"O time {time} ficou em último lugar em seu grupo e foi rebaixado!")
