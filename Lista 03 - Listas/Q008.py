equipes = int(input())
lista_geral = []

# alfabetos atrelados com bases no index da letra
alfabeto_codificado = ['k', 'q', 'f', 'm', 'x', 'e', 't', 'z', 'r', 'h', 'v', 'n', 'd', 'l', 'j', 'a', 's', 'u', 'y', 'b', 'g', 'w', 'p', 'o', 'i', 'c']
alfabeto_descodificado = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# adiciona sublistas a lista geral com base na quantidade de equipes
for i in range(equipes):
    lista_geral.append([])

acabou = False # flag de parada

while not acabou:
    acao = input()

    # condição de parada
    if acao == 'FIM':
        acabou = True

    # adicionar novo membro à equipe
    elif acao == 'adicionar':
        print("Quem será o próximo integrante do time?")
        entrada = input()
        partes = entrada.split(' - ')
        nome_codificado = partes[0]
        poder = int(partes[1])
        time = int(input())

        # decodificador de nome
        nome_decodificado = ''
        for letra in nome_codificado:
            if letra == ' ':
                nome_decodificado += ' '
            else:
                for i in range(len(alfabeto_codificado)):
                    if letra == alfabeto_codificado[i]:
                        nome_decodificado += alfabeto_descodificado[i]
        
        # condicionais com base no nome decodificado
        if nome_decodificado == 'rex splode':
            print("Eu vou te detonar!")
        
        elif nome_decodificado == 'atom eve':
            print("Eu reescrevo a matéria... incluindo a SUA.")
        
        elif nome_decodificado == 'duplikate':
            print("Quantas de mim você acha que consegue lidar?")
        
        elif nome_decodificado == 'robot':
            print("Minha lógica diz que você vai perder.")

        lista_geral[time].append([nome_decodificado, poder])

    # ação de encontrar metamorfo - substitui algum membro da equipe
    elif acao == 'metamorfo':
        print("Atenção!!! Metamorfo encontrado, quem deverá ser removido do time?")
        nome_remover = input()
        print("Quem você gostaria de colocar no lugar?")
        nome_substituir = input()
        partes = nome_substituir.split(' - ')
        nome_codificado = partes[0]
        poder = int(partes[1])
        time = int(input())

        i = 0
        while i < len(lista_geral[time]):
            if lista_geral[time][i][0] == nome_remover:
                lista_geral[time].pop(i)
            else:
                i += 1

        # decodificador de nome
        nome_decodificado = ''
        for letra in nome_codificado:
            if letra == ' ':
                nome_decodificado += ' '
            else:
                for i in range(len(alfabeto_codificado)):
                    if letra == alfabeto_codificado[i]:
                        nome_decodificado += alfabeto_descodificado[i]
        
        # print com base no nome
        if nome_decodificado == 'rex splode':
            print("Eu vou te detonar!")
        
        elif nome_decodificado == 'atom eve':
            print("Eu reescrevo a matéria... incluindo a SUA.")
        
        elif nome_decodificado == 'duplikate':
            print("Quantas de mim você acha que consegue lidar?")
        
        elif nome_decodificado == 'robot':
            print("Minha lógica diz que você vai perder.")

        lista_geral[time].append([nome_decodificado, poder])

# Nomes do Teen Team
teen_team_nomes = ['rex splode', 'atom eve', 'duplikate', 'robot']

for i in range(equipes):
    nomes_do_time = []
    for heroi in lista_geral[i]:
        nomes_do_time.append(heroi[0])

    # Verifica se o teen team está completo no time
    teen_completo = True
    for nome in teen_team_nomes:
        if nome not in nomes_do_time:
            teen_completo = False

    if teen_completo:
        print("O teen team esta completo, Cecil esta muito contente!")
        for j in range(len(lista_geral[i])):
            lista_geral[i][j][1] *= 1.1  # CORREÇÃO: aumenta 10% do poder e não +10 pontos

melhor_poder = -1
melhor_time = -1

for i in range(equipes):
    soma_poderes = 0
    for poder in lista_geral[i]:
        soma_poderes += poder[1]

    if soma_poderes > melhor_poder:
        melhor_poder = soma_poderes
        melhor_time = i

viltrumitas = [['general kregg',110],['conquista',100], ['anissa', 90]]

# ordenar heróis do melhor time pelo poder decrescente (selection sort)
herois_ordenados = []
nome_herois_ordenados = []

for heroi in lista_geral[melhor_time]:
    herois_ordenados.append(heroi)

for i in range(len(herois_ordenados)):
    for j in range(i+1, len(herois_ordenados)):
        if herois_ordenados[i][1] < herois_ordenados[j][1]:
            auxliar = herois_ordenados[i]
            herois_ordenados[i] = herois_ordenados[j]
            herois_ordenados[j] = auxliar
    nome_herois_ordenados.append(herois_ordenados[i][0])

# print das equipes
print(f"Aqui está o poderoso time da terra: {', '.join(nome_herois_ordenados[:3])}")

vitorias_herois = 0
vitorias_viltrumitas = 0

duelos = len(herois_ordenados)
if len(viltrumitas) < duelos:
    duelos = len(viltrumitas)

# duelos de cada rodada
for rodada in range(duelos):
    heroi = herois_ordenados[rodada][0]
    poder_heroi = herois_ordenados[rodada][1]
    viltrumita = viltrumitas[rodada][0]
    poder_viltrumita = viltrumitas[rodada][1]

    print(f"{rodada + 1} Duelo: {heroi} X {viltrumita}")

    if poder_heroi > poder_viltrumita:
        vitorias_herois += 1
    elif poder_heroi < poder_viltrumita:
        vitorias_viltrumitas += 1
    # empate não conta pontos

# print final de vitórias
if vitorias_herois > vitorias_viltrumitas:
    print("A terra venceu!")
else:
    print("Infelizmente o imperio viltrumita conquistou a terra!")
