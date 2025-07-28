ASCII_CHARS = (
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
    '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
    '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
)

def descriptografa(criptografado): # faz o processo reverso de encriptação
    tamanho = len(criptografado)
    if tamanho % 2 == 0:
        len_primeira_parte = len_segunda_parte = tamanho // 2
    
    else:
        len_primeira_parte = tamanho // 2
        len_segunda_parte = tamanho - len_primeira_parte - 1

    primeira_parte = criptografado[:len_primeira_parte]
    segunda_parte = criptografado[len_segunda_parte:]

    segunda_parte = rotacionar(segunda_parte, 1)

    string_completa = primeira_parte + segunda_parte
    lista_string = list(string_completa)

    lista_string.reverse()

    string_completa = ''
    for char in lista_string:
        string_completa += char

    string_completa = rotacionar(string_completa, -3)

    return string_completa

def rotacionar(string, val_shift):
    len_ascii = len(ASCII_CHARS)
    lista_string = list(string)

    palavra_final = ''

    for char in lista_string:
        for ascii_c in ASCII_CHARS:
            if char == ascii_c:
                idx_ascii = ASCII_CHARS.index(ascii_c)
                idx_pos_deslocamento = (idx_ascii + val_shift) % len_ascii
                carac = ASCII_CHARS[idx_pos_deslocamento]
    
                palavra_final += carac

    return palavra_final

numero_jogadores = int(input())

selecao = dict()

for i in range(numero_jogadores):
    criptografado = input()
    descriptografado = descriptografa(criptografado)

    selecao.update({f'{criptografado}' : f'{descriptografado}'})

for cryp, decryp in selecao.items():
    print(f"Criptografada: {cryp}\nDescriptografada: {decryp}")
    print("-" * 50)

felipao = False
remover_felipao = []

for chave, jogador in selecao.items():
    if jogador == 'Ronaldo':
        print("Ronaldo Fenômeno detectado! Autor dos gols na final!")
    elif jogador == 'Ronaldinho':
        print("Ronaldinho Gaúcho chegou! Chamem o inglês que ele vai chutar do meio-campo...")
    elif jogador == 'Cafu':
        print("Capitão Cafu presente! O único a jogar 3 finais de Copa seguidas!")
    elif jogador == 'Marcos':
        print("Marcos está na área! O paredão do Brasil em 2002!")
    elif jogador == 'Luiz Felipe Scolari':
        print("Técnico reconhecido: Luiz Felipe Scolari — o comandante do penta!")
        felipao = True
        remover_felipao.append(chave)
    else:
        print(f"{jogador} está confirmado na escalação!")

for remover in remover_felipao:
    del selecao[remover]

print()

selecao_completa = False
tamanho_selecao = len(selecao.values())

if tamanho_selecao >= 11:
    selecao_completa = True

if not selecao_completa:
    print("!!!!!!!!!! Escalação incompleta! !!!!!!!!!!")
    print(f"Só foram encontrados {tamanho_selecao} jogadores. Faltam jogadores para completar o time.")

else:
    print("++++++++++ Escalação Confirmada ++++++++++")
    print("Escalação Oficial da Seleção Brasileira — Copa do Mundo 2002")

    print("==================================================")
    for jogador in selecao.values():
        print(f"->{jogador}")
    print("==================================================")

if not felipao:
    print("!!!!!!!!!! Técnico não encontrado! !!!!!!!!!!")
    print("Como vamos jogar sem treinar? Como vamos ganhar o penta?")

else:
    print("========== Técnico ==========\nLuiz Felipe Scolari (Felipão)")

if felipao and selecao_completa:
    print("===== Tudo pronto! Rumo ao Penta! =====")
    print("Escalação completa com técnico confirmado.")
    print("Que comece o espetáculo, Brasil rumo ao penta!")
