# Contabiliza 1
nome_1 = str(input())
indicou_1 = str(input())

pontuacao_1 = len(nome_1)
if 'cin' in nome_1:
    pontuacao_1 += 10
    if indicou_1 != 'felino espião':
        print("Os melhores nomes são aqueles que fazem referência a minha casinha :)")

if 'gato' in nome_1 or indicou_1 == 'felino espião':
    pontuacao_1 = 0
    if indicou_1 == 'felino espião':
        print("Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.")

# Contabiliza 2
nome_2 = str(input())
indicou_2 = str(input())

pontuacao_2 = len(nome_2)
if 'cin' in nome_2:
    pontuacao_2 += 10
    if indicou_2 != 'felino espião':
        print("Os melhores nomes são aqueles que fazem referência a minha casinha :)")

if 'gato' in nome_2 or indicou_2 == 'felino espião':
    pontuacao_2 = 0
    if indicou_2 == 'felino espião':
        print("Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.")

# Contabiliza 3
nome_3 = str(input())
indicou_3 = str(input())

pontuacao_3 = len(nome_3)

if 'cin' in nome_3:
    pontuacao_3 += 10
    if indicou_3 != 'felino espião':
        print("Os melhores nomes são aqueles que fazem referência a minha casinha :)")

if 'gato' in nome_3 or indicou_3 == 'felino espião':
    pontuacao_3 = 0
    if indicou_3 == 'felino espião':
        print("Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.")

# Mostra ranking de nomes
print("RANKING DOS NOMES:")
if pontuacao_1 > pontuacao_2 and pontuacao_1 > pontuacao_3:
    print(f"Primeiro lugar: {nome_1}")
    if pontuacao_2 > pontuacao_3:
        print(f"Segundo lugar: {nome_2}")
        print(f"Terceiro lugar: {nome_3}")
    else:
        print(f"Segundo lugar: {nome_3}")
        print(f"Terceiro lugar: {nome_2}")

elif pontuacao_2 > pontuacao_1 and pontuacao_2 > pontuacao_3:
    print(f"Primeiro lugar: {nome_2}")
    if pontuacao_1 > pontuacao_3:
        print(f"Segundo lugar: {nome_1}")
        print(f"Terceiro lugar: {nome_3}")
    else:
        print(f"Segundo lugar: {nome_3}")
        print(f"Terceiro lugar: {nome_1}")

else:
    print(f"Primeiro lugar: {nome_3}")
    if pontuacao_1 > pontuacao_2:
        print(f"Segundo lugar: {nome_1}")
        print(f"Terceiro lugar: {nome_2}")
    else:
        print(f"Segundo lugar: {nome_2}")
        print(f"Terceiro lugar: {nome_1}")
