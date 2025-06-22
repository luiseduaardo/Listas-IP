quantidade_atletas = int(input())

# Se tiver só 1 entrada
if quantidade_atletas == 1:
    nome_atleta = str(input())
    posicao = int(input())
    ranking = int(input())
    velocidade = float(input())

    print(f"Não há dúvidas... {nome_atleta} é o culpado!")

elif quantidade_atletas == 2:
    nome_atleta_1 = str(input())
    posicao_1 = int(input())
    ranking_1 = int(input())
    velocidade_1 = float(input())

    nome_atleta_2 = str(input())
    posicao_2 = int(input())
    ranking_2 = int(input())
    velocidade_2 = float(input())

    print(f"Caso encerrado: {nome_atleta_1} e {nome_atleta_2} roubaram o troféu!")

else:
    # Coloca como -1 porque se algum não pontuar não vai ser computado
    nome_1, pontos_1 = '', -1
    nome_2, pontos_2 = '', -1
    nome_3, pontos_3 = '', -1

    for i in range(quantidade_atletas):
        print(f"COMEÇANDO A {i+1}ª RODADA DE INVESTIGAÇÃO")

        # Inputs
        nome_atleta = str(input())
        posicao = int(input())
        ranking = int(input())
        velocidade = float(input())

        vogais = pontos_suspeita = 0
        suspeito = False

        # Outputs
        # Contabilizar e pontuar vogais
        for letra in nome_atleta.lower():
            if letra in 'aeiou':
                vogais += 1
        if vogais % 2 == 0:
            pontos_suspeita += 10
        else:
            pontos_suspeita += 5
        
        # Contabilizar com base na posição
        if 45 <= posicao <= 135:
            pontos_suspeita += 10
            print(f"{nome_atleta} estava em posição estratégica para pegar o troféu... muito suspeito!")
            suspeito = True
        elif 225 <= posicao <= 315:
            pontos_suspeita += 5
        else:
            pontos_suspeita += 2

        # Contabilizar com base no ranking
        if ranking <= 10:
            pontos_suspeita += 10
            print(f"{nome_atleta} é um dos melhores do mundo... e também um dos principais suspeitos!")
            suspeito = True
        elif 11 <= ranking <= 50:
            pontos_suspeita += 5
        else:
            pontos_suspeita += 2

        # Contabilizar com base na velocidade de ataque
        if velocidade > 140:
            pontos_suspeita += 10
            print(f"Alta velocidade detectada! {nome_atleta} pode ter fugido rapidamente com o troféu!")
            suspeito = True
        elif 100 <= velocidade <= 140:
            pontos_suspeita += 5
        elif velocidade < 100:
            pontos_suspeita += 2

        # Se não for suspeito
        if not suspeito:
            print(f"Hum, esse {nome_atleta} sei não viu... Deve tá escondendo alguma coisa.")
        
        # Compara com anterior
        if pontos_suspeita > pontos_1:
            nome_3, pontos_3 = nome_2, pontos_2
            nome_2, pontos_2 = nome_1, pontos_1
            nome_1, pontos_1 = nome_atleta, pontos_suspeita
        elif pontos_suspeita > pontos_2:
            nome_3, pontos_3 = nome_2, pontos_2
            nome_2, pontos_2 = nome_atleta, pontos_suspeita
        elif pontos_suspeita > pontos_3:
            nome_3, pontos_3 = nome_atleta, pontos_suspeita
        
    print("\nRESULTADOS DAS INVESTIGAÇÕES:\n")
    print("Os 3 principais suspeitos são:")
    print(f"1. {nome_1} - {pontos_1} pontos")
    print(f"2. {nome_2} - {pontos_2} pontos")
    print(f"3. {nome_3} - {pontos_3} pontos\n")

    if pontos_1 == pontos_2:
        print(f"Que absurdo... {nome_1} e {nome_2} roubaram o troféu juntos!")
    else:
        print(f"Mistério resolvido: O culpado é {nome_1}! Ele roubou o troféu de Calderano.")
