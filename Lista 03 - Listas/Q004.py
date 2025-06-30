print("Go! Go! Power Rangers!")

sequencia = input()

lista_tudo = sequencia.split('-')

robocin = False

# Listas para cada tipo
tipo1_nomes = []
tipo1_poderes = []

tipo2_nomes = []
tipo2_poderes = []

tipo3_nomes = []
tipo3_poderes = []

# Atribui cada elemento a uma lista
i = 0

while i < len(lista_tudo):
    nome = lista_tudo[i]
    poder = int(lista_tudo[i+1])


    if nome == 'robocin':
        robocin = True

    if poder <= 10:
        tipo3_nomes.append(nome)
        tipo3_poderes.append(poder)
    
    elif 10 < poder <= 30:
        tipo2_nomes.append(nome)
        tipo2_poderes.append(poder)
    
    elif poder > 30:
        tipo1_nomes.append(nome)
        tipo1_poderes.append(poder)

    i += 2

# variáveis individuais para os maiores de cada tipo
maior_tipo1 = ''
maior_tipo2 = ''
maior_tipo3 = ''
poderes_maior_tipo1 = poderes_maior_tipo2 = poderes_maior_tipo3 = 0
segundo_maior_tipo1 = ''
segundo_maior_tipo2 = ''
segundo_maior_tipo3 = ''
poder_segundo_maior1 = poder_segundo_maior2 = poder_segundo_maior3 = -1

# condição de parada (robocin estar no meio)
if robocin:
    print("Os rangers encontraram o zord lendário!!!! O Robocin!!!! Eles não precisam mais de outros zords!")

else:
    # Maior do tipo 1
    for i in range(len(tipo1_nomes)):
        if i == 0:
            maior_tipo1, poderes_maior_tipo1 = tipo1_nomes[i], tipo1_poderes[i]
        else:
            if tipo1_poderes[i] > poderes_maior_tipo1:
                maior_tipo1, poderes_maior_tipo1 = tipo1_nomes[i], tipo1_poderes[i]
    
    # Maior do tipo 2
    for j in range(len(tipo2_nomes)):
        if j == 0:
            maior_tipo2, poderes_maior_tipo2 = tipo2_nomes[j], tipo2_poderes[j]
        else:
            if tipo2_poderes[j] > poderes_maior_tipo2:
                maior_tipo2, poderes_maior_tipo2 = tipo2_nomes[j], tipo2_poderes[j]

    # Maior do tipo 3
    for k in range(len(tipo3_nomes)):
        if k == 0:
            maior_tipo3, poderes_maior_tipo3 = tipo3_nomes[k], tipo3_poderes[k]
        else:
            if tipo3_poderes[k] > poderes_maior_tipo3:
                maior_tipo3, poderes_maior_tipo3 = tipo3_nomes[k], tipo3_poderes[k]

    # Segundo maior do tipo 1
    for l in range(len(tipo1_poderes)):
        if tipo1_nomes[l] != maior_tipo1:
            if poder_segundo_maior1 == -1 or tipo1_poderes[l] > poder_segundo_maior1:
                segundo_maior_tipo1 = tipo1_nomes[l]
                poder_segundo_maior1 = tipo1_poderes[l]

    # Segundo maior do tipo 2
    for m in range(len(tipo2_poderes)):
        if tipo2_nomes[m] != maior_tipo2:
            if poder_segundo_maior2 == -1 or tipo2_poderes[m] > poder_segundo_maior2:
                segundo_maior_tipo2 = tipo2_nomes[m]
                poder_segundo_maior2 = tipo2_poderes[m]

    # Segundo maior do tipo 3
    for n in range(len(tipo3_poderes)):
        if tipo3_nomes[n] != maior_tipo3:
            if poder_segundo_maior3 == -1 or tipo3_poderes[n] > poder_segundo_maior3:
                segundo_maior_tipo3 = tipo3_nomes[n]
                poder_segundo_maior3 = tipo3_poderes[n]

    # Distribuição dos zords:
    if maior_tipo1 != '':
        print("Zord do Ranger Vermelho:", maior_tipo1)
    else:
        print("Ranger Vermelho ficou sem zord!")

    if segundo_maior_tipo1 != '':
        print("Zord do Ranger Verde:", segundo_maior_tipo1)
    else:
        print("Ranger Verde ficou sem zord!")

    if maior_tipo2 != '':
        print("Zord da Ranger Rosa:", maior_tipo2)
    else:
        print("Ranger Rosa ficou sem zord!")

    if segundo_maior_tipo2 != '':
        print("Zord do Ranger Preto:", segundo_maior_tipo2)
    else:
        print("Ranger Preto ficou sem zord!")

    if maior_tipo3 != '':
        print("Zord do Ranger Azul:", maior_tipo3)
    else:
        print("Ranger Azul ficou sem zord!")

    if segundo_maior_tipo3 != '':
        print("Zord da Ranger Amarela:", segundo_maior_tipo3)
    else:
        print("Ranger Amarela ficou sem zord!")

    # Ordena as listas em ordem decrescente - selection sort
    # Lista 1
    for i in range(len(tipo1_poderes)):
        for j in range(i+1, len(tipo1_poderes)):
            if tipo1_poderes[i] < tipo1_poderes[j]:
                aux_poder = tipo1_poderes[i]
                tipo1_poderes[i] = tipo1_poderes[j]
                tipo1_poderes[j] = aux_poder

                # Troca os nomes para manter pareados
                aux_nome = tipo1_nomes[i]
                tipo1_nomes[i] = tipo1_nomes[j]
                tipo1_nomes[j] = aux_nome

    # Lista 2
    for i in range(len(tipo2_poderes)):
        for j in range(i+1, len(tipo2_poderes)):
            if tipo2_poderes[i] < tipo2_poderes[j]:
                aux_poder = tipo2_poderes[i]
                tipo2_poderes[i] = tipo2_poderes[j]
                tipo2_poderes[j] = aux_poder

                # Troca os nomes para manter pareados
                aux_nome = tipo2_nomes[i]
                tipo2_nomes[i] = tipo2_nomes[j]
                tipo2_nomes[j] = aux_nome

    # Lista 3
    for i in range(len(tipo3_poderes)):
        for j in range(i+1, len(tipo3_poderes)):
            if tipo3_poderes[i] < tipo3_poderes[j]:
                aux_poder = tipo3_poderes[i]
                tipo3_poderes[i] = tipo3_poderes[j]
                tipo3_poderes[j] = aux_poder

                # Troca os nomes para manter pareados
                aux_nome = tipo3_nomes[i]
                tipo3_nomes[i] = tipo3_nomes[j]
                tipo3_nomes[j] = aux_nome

    # Printa os zords de cada tipo
    # MELHORIA: printar nomes usando .join
    if len(tipo1_nomes) == 0:
        print("Não temos nenhum zord do tipo 1 :(")
    else:
        print("Zords do tipo 1:", ", ".join(tipo1_nomes))

    if len(tipo2_nomes) == 0:
        print("Não temos nenhum zord do tipo 2 :(")
    else:
        print("Zords do tipo 2:", ", ".join(tipo2_nomes))

    if len(tipo3_nomes) == 0:
        print("Não temos nenhum zord do tipo 3 :(")
    else:
        print("Zords do tipo 3:", ", ".join(tipo3_nomes))

    # Verificar se todos os rangers têm zords
    if maior_tipo1 != '' and segundo_maior_tipo1 != '' and maior_tipo2 != '' and segundo_maior_tipo2 != '' and maior_tipo3 != '' and segundo_maior_tipo3 != '':
        print("Os Rangers estão prontos para montar o Megazord e derrotar Rita!")
    else:
        print("Ai ai ai, essa não!! Não temos zords suficientes para formar o Megazord! Os ranger não vão conseguir derrotar Rita!")
