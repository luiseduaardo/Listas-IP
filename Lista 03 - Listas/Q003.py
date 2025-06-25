# variáveis globais e listas utilizadas
armas_disponiveis = []
armas_usadas = []
acabou = False
perdeu = False
golpes_thanos = 0

# input da quantidade de armas
qtd_armas = int(input())

# loop inicial para ter input de quantidade de armas
for i in range(qtd_armas):
    arma = input()
    armas_disponiveis.append(arma)

# loop até o fim
while not acabou:
    usar_arma = input()

    # condicionais se não acabar
    if usar_arma != 'fim':
        # arma dentro das armas disponíveis
        if usar_arma in armas_disponiveis:
            idx = armas_disponiveis.index(usar_arma)
            arma_utilizada = armas_disponiveis.remove(armas_disponiveis[idx])
            armas_usadas.append(usar_arma)
            print(f"{usar_arma} usado(a) com sucesso!")
        
        # arma fora das armas disponíveis
        elif usar_arma not in armas_disponiveis:
            golpes_thanos += 1
            # arma não disponível e já usada
            if usar_arma in armas_usadas:
                print(f"{usar_arma} já foi usado(a)!")
            else:
                print(f"{usar_arma} não está disponível!")

    # condição de parada
    if usar_arma == 'fim':
        acabou = True
        print(f"Batalha encerrada! Os Vingadores utilizaram {len(armas_usadas)} arma(s).")

        if golpes_thanos == 0:
            print(f"Vitória! Os Vingadores salvaram o UNIVERSO!\n\nTony Stark:\nSalvar o mundo de novo? Vou precisar de um aumento.\n\nThor:\nEspero que tenha cerveja depois disso!\n\nHomem-Aranha:\nPosso dizer que ajudei, né? Tipo… oficialmente?\nDá pra postar isso no Insta dos Vingadores?")
        elif golpes_thanos == 1:
            print(f"Os Vingadores sofreram um golpe do Thanos!\nVitória por pouco! Os Vingadores ganharam...\n\nTony Stark:\nQuase que eu fico sem troco para o cafezinho.\n\nThor:\nEsse quase foi o meu momento de “não consegui”. Mas consegui, então vale cerveja!\n\nPeter Quill (Star-Lord):\nCara, quase perdi o ritmo do meu walkman!")
        elif golpes_thanos >= 2:
            print(f"Os Vingadores sofreram {golpes_thanos} golpes do Thanos!\nDerrota... Os Vingadores não conseguiram todas as armas necessárias.\n\nTony Stark:\nEssa não foi das melhores ideias...\n\nThor:\nCulpa do humano. Eu sabia que devíamos ter chamado o Hulk.")
