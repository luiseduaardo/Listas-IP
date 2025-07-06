def fusao_fun(primeira_string, segunda_string, categoria):
    segunda_string = segunda_string.lower()
    primeira_string = primeira_string.lower()

    # primeira string
    if len(primeira_string) <= 4: # tamanho da string menor ou igual a 4
        caracteres_prim = primeira_string[0]
    
    else: # tamanho da string maior que 4
        qtd_caracteres_primeira = (len(primeira_string) + 1) // 2 
        caracteres_prim = primeira_string[:qtd_caracteres_primeira]

    # segunda string
    if len(segunda_string) <= 4: # tamanho da segunda string menor que 4
        if len(segunda_string) == 3:
            caracteres_seg = segunda_string[1:]
        else:
            caracteres_seg = segunda_string[-3:]

    else: # tamanho da segunda string maior que 4
        qtd_caracteres_segunda = ((len(segunda_string) + 1) // 2) - 1
        caracteres_seg = segunda_string[-qtd_caracteres_segunda:]

    fusao = caracteres_prim + caracteres_seg
    tipo_fusao = fusao_tipagem(caracteres_prim, caracteres_seg, fusao)
    print_tipo_funcao(tipo_fusao, fusao, categoria)

    if tipo_fusao == 'imperfeita':
        tipo_fusao = ''
        # primeira string
        if len(primeira_string) <= 4: # tamanho da string menor ou igual a 4
            caracteres_prim = primeira_string[:2]
    
        else: # tamanho da string maior que 4
            qtd_caracteres_primeira = (len(primeira_string) + 1) // 2 + 1
            caracteres_prim = primeira_string[:qtd_caracteres_primeira]

        fusao = caracteres_prim + caracteres_seg
        tipo_fusao = fusao_tipagem(caracteres_prim, caracteres_seg, fusao)
        print_tipo_funcao(tipo_fusao, fusao, categoria)

        if len(fusao) > 4:
            caracteres_prim = caracteres_prim[:-1]

        if tipo_fusao == 'imperfeita':
            tipo_fusao = ''
            # segunda string
            if len(segunda_string) <= 4: # tamanho da segunda string menor que 4
                caracteres_seg = segunda_string[-3:]

            else: # tamanho da segunda string maior que 4
                qtd_caracteres_segunda = ((len(segunda_string) + 1) // 2)
                caracteres_seg = segunda_string[-qtd_caracteres_segunda:]
            
            fusao = caracteres_prim + caracteres_seg

            tipo_fusao = fusao_tipagem(caracteres_prim, caracteres_seg, fusao)
            print_tipo_funcao(tipo_fusao, fusao, categoria, ultimo = True)

            if tipo_fusao == 'imperfeita':
                fusao = ''

    return fusao

def fusao_tipagem(primeiro_caracteres, segundo_caracteres, fusao): # define tipo de fusão (perfeita ou imperfeita)
    vogais = ['a', 'e', 'i', 'o', 'u']
    consoantes = [
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
        'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
    ]

    ultima_primeira = primeiro_caracteres[-1].lower()
    primeira_segunda = segundo_caracteres[0].lower()

    if (ultima_primeira in consoantes and primeira_segunda in consoantes) or (ultima_primeira in vogais and primeira_segunda in vogais) or (len(fusao) <= 3):
        return 'imperfeita'
    else:
        return 'perfeita'

def print_tipo_funcao(tipagem, nome_fusao, personagens, ultimo = False): # printa com base no tipo de função de de personagem
    if tipagem == 'imperfeita':
        print(f"A sincronização foi um desastre... {nome_fusao.capitalize()} é uma fusão imperfeita!")
        if ultimo:
            print(f"Aparentemente essa combinação é incompatível...")

    elif tipagem == 'perfeita':
        if personagens == 'herois':
            print(f"Fusão realizada com sucesso! {nome_fusao.capitalize()} entra em combate para derrotar o exército de vilões!")
        elif personagens == 'viloes':
            print(f"Fusão realizada com sucesso! {nome_fusao.capitalize()} entra em combate com sede de destruir Satan City!")

def incremento_poder(nome_fusao):
    return len(nome_fusao) * 250 + 1000

def descobrir_categoria(nome): # define categoria do nome
    if nome in herois:
        return 'herois'
    elif nome in viloes:
        return 'viloes'

herois = [
    'Gohan',
    'Goku',
    'Goten',
    'Kuririn',
    'Piccolo',
    'Tenshinhan',
    'Trunks',
    'Uub',
    'Vegeta',
    'Yamcha'
]

viloes = [
    'Babidi',
    'Baby',
    'Broly',
    'Buu',
    'Cell',
    'Cooler',
    'Frieza',
    'Hit',
    'Janemba',
    'Zamasu'
]

lista_jafundidos = []
acabar = False

poder_herois = poder_viloes = 0

# loop de execução da fusão
while not acabar:
    valido = True

    nome1 = input()
    while (nome1 not in herois) and (nome1 not in viloes) and (nome1 not in lista_jafundidos):
        nome1 = input()
    print(f"{nome1} se elege para participar da fusão!")

    nome2 = input()
    while (nome2 not in herois) and (nome2 not in viloes) and (nome2 not in lista_jafundidos):
        nome2 = input()
    print(f"{nome2} se elege para participar da fusão!")

    if nome1 in lista_jafundidos:
        print(f"{nome1} já participou de uma fusão. Fusão inválida.")
        valido = False
    
    if nome2 in lista_jafundidos:
        print(f"{nome2} já participou de uma fusão. Fusão inválida.")
        valido = False

    if valido:
        categoria_1 = descobrir_categoria(nome1)
        categoria_2 = descobrir_categoria(nome2)

        if categoria_1 != categoria_2:
            print("Heróis e vilões não se misturam! As auras dos dois participantes são incompatíveis.")
            valido = False

        if valido:
            tipo = categoria_1

            if ((nome1 == 'Goku' and nome2 == 'Vegeta') or (nome1 == 'Vegeta' and nome2 == 'Goku')):
                resultado_fusao = 'Vegito'
                print_tipo_funcao('perfeita', resultado_fusao, tipo)
            elif ((nome1 == 'Goten' and nome2 == 'Trunks') or (nome1 == 'Trunks' and nome2 == 'Goten')):
                resultado_fusao = 'Gotenks'
                print_tipo_funcao('perfeita', resultado_fusao, tipo)
            else:
                resultado_fusao = fusao_fun(nome1, nome2, tipo)

            if resultado_fusao != '':
                if tipo == 'herois':
                    poder_herois += incremento_poder(resultado_fusao)

                elif tipo == 'viloes':
                    poder_viloes += incremento_poder(resultado_fusao)
            
                if poder_herois > 8000:
                    print("O poder dos heróis... É mais de 8000! Eles derrotam os vilões e conseguem selar o portal.")
                    acabar = True
                elif poder_viloes > 8000:
                    print("Os vilões são fortes demais! Satan City está em apuros!")
                    acabar = True

                lista_jafundidos.append(nome1)
                lista_jafundidos.append(nome2)
                if tipo == 'herois':
                    herois.remove(nome1)
                    herois.remove(nome2)
                else:
                    viloes.remove(nome1)
                    viloes.remove(nome2)
