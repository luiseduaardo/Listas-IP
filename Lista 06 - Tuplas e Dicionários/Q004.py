qtd_tecnicos = int(input())
tecnicos = dict()
primeiro_lugar = {'pontos': -1}
segundo_lugar = {'pontos': -1}
terceiro_lugar = {'pontos': -1}

for i in range(qtd_tecnicos):
    nome = input()
    nacionalidade = input()

    if nacionalidade == 'argentino':
        print("Um hermano comandando a seleção? Sai fora!")

    else:
        titulos_continentais = int(input())
        titulos_nacionais = int(input())
        aproveitamento = float(input())

        interesse = input()

        pontuação_total = ((titulos_continentais * 100) + (titulos_nacionais * 50)) * aproveitamento

        if nacionalidade == 'brasileiro':
            pontuação_total *= 1.10
        elif nacionalidade == 'alemão':
            pontuação_total *= 0.90

        if titulos_continentais == 0:
            pontuação_total *= 0.50
        
        tecnicos.update({f'{nome}': {'nacionalidade': nacionalidade, 'pontos': pontuação_total, 'interesse': interesse}})
        
        if nome == 'Ancelotti':
            print("Será que Carleto irá continuar no cargo?")

        elif nome == 'Jorge Jesus':
            print("O mister finalmente retornará ao Brasil?")

        elif nacionalidade == 'alemão':
            print("Iremos mesmo perdoar o 7x1?")

        # lógica do ranking

        if pontuação_total > primeiro_lugar['pontos']:
            terceiro_lugar = segundo_lugar.copy()
            segundo_lugar = primeiro_lugar.copy()
            primeiro_lugar.update({'nome': nome, 'nacionalidade': nacionalidade, 'pontos': pontuação_total, 'interesse': interesse})
        
        elif pontuação_total > segundo_lugar['pontos']:
            terceiro_lugar = segundo_lugar.copy()
            segundo_lugar.update({'nome': nome, 'nacionalidade': nacionalidade, 'pontos': pontuação_total, 'interesse': interesse})
        
        elif pontuação_total > terceiro_lugar['pontos']:
            terceiro_lugar.update({'nome': nome, 'nacionalidade': nacionalidade, 'pontos': pontuação_total, 'interesse': interesse})

print(f"Lista de treinadores - CBF")
print(f"1º {primeiro_lugar['nome']} - {primeiro_lugar['nacionalidade']} - {primeiro_lugar['pontos']:.2f} pontos")
print(f"2º {segundo_lugar['nome']} - {segundo_lugar['nacionalidade']} - {segundo_lugar['pontos']:.2f} pontos")
print(f"3º {terceiro_lugar['nome']} - {terceiro_lugar['nacionalidade']} - {terceiro_lugar['pontos']:.2f} pontos")

escolhido = True

if (primeiro_lugar['nome'] == 'Ancelotti' and primeiro_lugar['interesse'] == 'sim'):
    tecnico = primeiro_lugar['nome']
    nacionalidade = primeiro_lugar['nacionalidade']

elif (segundo_lugar['nome'] == 'Ancelotti' and segundo_lugar['interesse'] == 'sim'):
    tecnico = segundo_lugar['nome']
    nacionalidade = segundo_lugar['nacionalidade']

elif (terceiro_lugar['nome'] == 'Ancelotti' and terceiro_lugar['interesse'] == 'sim'):
    tecnico = terceiro_lugar['nome']
    nacionalidade = terceiro_lugar['nacionalidade']

else:
    if (primeiro_lugar['interesse']) == 'sim':
        tecnico = primeiro_lugar['nome']
        nacionalidade = primeiro_lugar['nacionalidade']
    
    else:
        print(f"O {primeiro_lugar['nome']} não aceitou a proposta da CBF e outros nomes serão analisados. Cuida, CBF!")

        if (segundo_lugar['interesse']) == 'sim':
            tecnico = segundo_lugar['nome']
            nacionalidade = segundo_lugar['nacionalidade']
        
        else:
            print(f"O {segundo_lugar['nome']} não aceitou a proposta da CBF e outros nomes serão analisados. Cuida, CBF!")

            if (terceiro_lugar['interesse']) == 'sim':
                tecnico = terceiro_lugar['nome']
                nacionalidade = terceiro_lugar['nacionalidade']

            else:
                print(f"O {terceiro_lugar['nome']} não aceitou a proposta da CBF e outros nomes serão analisados. Cuida, CBF!")
                print(f"Nenhum técnico aceitou a maior seleção do mundo!? Que humilhação, Sr. Samir Xaud!!!")
                escolhido = False

if escolhido:
    if nacionalidade != 'brasileiro':
        print(f"{tecnico} será o quarto estrangeiro a treinar o Brasil. Que honra para o {nacionalidade}!")

    if tecnico == 'Ancelotti':
        print("Depois de uma longa novela, Carlo Ancelotti continuará como o treinador da Seleção Brasileira! Estamos bem servidos!")

    elif tecnico == 'Jorge Jesus':
        print("JESUS VOLTOU!!! Será que ele conseguirá repetir na seleção o sucesso que obteve no Flamengo?")

    elif tecnico == 'Felipão':
        print("FELIPÃO DE NOVO!? Vem mais um 7x1 por aí?")

    else:
        print(f"O técnico {nacionalidade} {tecnico} irá treinar o Brasil. Não era o nome que esperávamos, mas torcemos para que faça um bom trabalho!")
