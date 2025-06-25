lista_suspeitos = []

# locais, horários de abertura e nível de segurança (index atrelados entre si)
lista_locais = ["Torre Eiffel", "Museu do Louvre", "Catacumbas de Paris", "Biblioteca Nacional", "Galeria Lafayette", "Parque dos Príncipes", "Catedral de Notre-Dame", "Jardim de Luxemburgo", "Padaria Dupain Cheng"]
horarios_abertura = [900, 800, 1000, 700, 1000, 600, 800, 600, 400]
horarios_fechamento = [2300, 1800, 2000, 2200, 2100, 2300, 1830, 1900, 2000]
segurancas = ["Média", "Alta", "Baixa", "Média", "Alta", "Baixa", "Alta", "Média", "Baixa"]

# input de 6 suspeitos e suas respectivas informações
for i in range(6):
    suspeito = input()
    auxiliar = suspeito.split(' - ')
    auxiliar[1] = auxiliar[1].replace(':', '')
    lista_suspeitos.append(auxiliar)

# Prioridade 1 - locais que não existem
locais_invalidos = []
nomes_invalidos = []

for j in range(6):
    if lista_suspeitos[j][2] not in lista_locais:
        locais_invalidos.append(lista_suspeitos[j][2])
        nomes_invalidos.append(lista_suspeitos[j][0])

if len(locais_invalidos) == 1:
    print(f"Esse lugar {locais_invalidos[0]} nem existe! {nomes_invalidos[0]} com certeza foi akumatizado!")

elif len(locais_invalidos) > 1:
    locais_invalidos.sort()
    nomes_invalidos.sort()
    print(f"{', '.join(locais_invalidos)} nem existem! {', '.join(nomes_invalidos)} estão mentindo!")

else:
    # Prioridade 2 - fora do horário de funcionamento
    locais_fechados = []
    nomes_fechados = []
    horas = []

    for i in range(6):
        nome = lista_suspeitos[i][0]
        hora = int(lista_suspeitos[i][1])
        local = lista_suspeitos[i][2]

        for j in range(len(lista_locais)):
            if local == lista_locais[j]:
                if hora < horarios_abertura[j] or hora > horarios_fechamento[j]:
                    locais_fechados.append(local)
                    nomes_fechados.append(nome)
                    horas.append(lista_suspeitos[i][1][:2] + ':' + lista_suspeitos[i][1][2:])
        
    if len(locais_fechados) == 1:
        print(f"{locais_fechados[0]} nem estava aberto às {horas[0]}! {nomes_fechados[0]} recebeu memórias falsas!")
    
    elif len(locais_fechados) > 1:
        locais_fechados.sort()
        nomes_fechados.sort()
        print(f"{', '.join(locais_fechados)} estavam fechados nesse horário! {', '.join(nomes_fechados)} podem ter sido manipulados pelo Hawk Moth!")

    else:
        # Prioridade 3 - Segurança baixa
        nomes_baixa = []

        for i in range(6):
            nome = lista_suspeitos[i][0]
            local = lista_suspeitos[i][2]

            for j in range(len(lista_locais)):
                if local == lista_locais[j] and segurancas[j] == 'Baixa':
                    nomes_baixa.append(nome)
        
        if len(nomes_baixa) == 1:
            print(f"{nomes_baixa[0]} estava em um local de segurança baixa... Ele pode ter mentido!")
        
        elif len(nomes_baixa) > 1:
            nomes_baixa.sort()
            print(f"{', '.join(nomes_baixa)} estavam em locais de segurança baixa... Eles podem estar forjando um álibi!")
        
        else:
            # Prioridade 4 - Álibe / testemunhas
            nome_test = []

            for i in range(6):
                nome = lista_suspeitos[i][0]
                suspeita = lista_suspeitos[i][3]

                if suspeita == 'nenhuma':
                    nome_test.append(nome)
            
            if len(nome_test) == 1:
                print(f"{nome_test[0]} não teve testemunha para confirmar o álibi. É o mais suspeito até agora.")
            
            elif 1 < len(nome_test) < 6:
                nome_test.sort()
                print(f"{', '.join(nome_test)} não foram confirmados por ninguém. O Hawk Moth pode vir atrás deles de novo")
            
            elif len(nome_test) == 6:
                print("Ninguém viu ninguém… estranho!!")
            
            else:
                print("Poxa vida, todos os àlibis parecem válidos… mas algo continua errado")
