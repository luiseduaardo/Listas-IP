nome_cao_1 = str(input())
pontuacao_1_1 = int(input())
pontuacao_1_2 = int(input())
pontuacao_1_3 = int(input())
soma_1 = pontuacao_1_1 + pontuacao_1_2 + pontuacao_1_3

fim = False

if nome_cao_1 == "Byte":
    print("Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!")
    fim = True

if not fim:
    if soma_1 == 30:
        print(f"Com uma pontuação perfeita, {nome_cao_1} conquista o título de mascote do CIn!")
        fim = True

    elif soma_1 < 15:
        print(f"Infelizmente {nome_cao_1} está fora da disputa")

if not fim:
    nome_cao_2 = str(input())
    pontuacao_2_1 = int(input())
    pontuacao_2_2 = int(input())
    pontuacao_2_3 = int(input())
    soma_2 = pontuacao_2_1 + pontuacao_2_2 + pontuacao_2_3

    if nome_cao_2 == "Byte":
        print("Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!")
        fim = True

    if soma_2 == 30:
        print(f"Com uma pontuação perfeita, {nome_cao_2} conquista o título de mascote do CIn!")
        fim = True

    elif soma_2 < 15:
        print(f"Infelizmente {nome_cao_2} está fora da disputa")

if not fim:
    nome_cao_3 = str(input())
    pontuacao_3_1 = int(input())
    pontuacao_3_2 = int(input())
    pontuacao_3_3 = int(input())
    soma_3 = pontuacao_3_1 + pontuacao_3_2 + pontuacao_3_3

    if nome_cao_3 == "Byte":
        print("Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!")
        fim = True

    if soma_3 == 30:
        print(f"Com uma pontuação perfeita, {nome_cao_3} conquista o título de mascote do CIn!")
        fim = True

    elif soma_3 < 15:
        print(f"Infelizmente {nome_cao_3} está fora da disputa")

if not fim:
    if soma_1 > soma_2 and soma_1 > soma_3:
        print(f"Após uma disputa acirrada, o novo mascote do CIn é {nome_cao_1}!")
    elif soma_2 > soma_1 and soma_2 > soma_3:
        print(f"Após uma disputa acirrada, o novo mascote do CIn é {nome_cao_2}!")
    elif soma_3 > soma_2 and soma_3 > soma_1:
        print(f"Após uma disputa acirrada, o novo mascote do CIn é {nome_cao_3}!")
