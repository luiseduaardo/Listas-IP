def expressao_prefixa(sequencia):
    tokens = sequencia.split(' ')
    pilha = []

    for token in reversed(tokens): # lê a sequência de trás pra frente e adiciona à pilha caso encontre um número
        if token.isdigit():
            pilha.append(int(token))
        
        else: # realiza as operações caso encontre um operador
            operando1 = pilha.pop()
            operando2 = pilha.pop()

            if token == '+':
                pilha.append(operando1 + operando2)

            elif token == '-':
                pilha.append(operando1 - operando2)

            elif token == '*':
                pilha.append(operando1 * operando2)

            elif token == '/':
                pilha.append(int(operando1 / operando2))
    
    return int(pilha[0])

def primo(numero): # calcula se é primo ou não (método da força bruta)
    if numero <= 1:
        return False
    else:
        for i in range(2, int(numero**0.5) + 1): # verifica somente até raiz quadrada
            if numero % i == 0:
                return False
        return True

def converte_binario_decimal(binario): # conversão binário --> decimal
    if type(binario) == int:
        binario = str(binario)
    return int(binario, 2)

def processar_coordenadas(decimal, ordem): # processa a coordenadas
    return decimal % ordem

def distancia_esfera(esferax, esferay, gokux, gokuy): # distância euclidiana entre as esferas
    distancia = ((esferax - gokux)**2 + (esferay - gokuy)**2)**0.5
    return distancia

# Início do programa (main)
# mensagens iniciais
print("🟠 Vamos conquistar as esferas do dragão! 🟠")
print('-' * 74)
print()

# inputs iniciais
ordem_matriz = int(input())
localizacao_goku = input()
localizacao_goku = localizacao_goku.replace("(", '').replace(")", '')
localizacao_goku = localizacao_goku.split(", ")

x_goku = int(localizacao_goku[0])
y_goku = int(localizacao_goku[1])

input() # linha vazia

continua_decodificacao = True
qtd_esferas = 1

coordenadas_esferas = []

# loop de decodificação
while continua_decodificacao:
    primeira_linha = input() # verifica a condição de parada ou as linhas iniciais ---...---

    if primeira_linha == 'Todos os bits foram decodificados': # condição de parada
        continua_decodificacao = False

    else:
        # cálculo da coordenada x
        expressao = input()
        seq_binaria_x = ''

        while expressao != '':
            resultado = expressao_prefixa(expressao)
        
            if primo(resultado):
                seq_binaria_x += '1'
            else:
                seq_binaria_x += '0'

            expressao = input()

        valor_decimal_x = converte_binario_decimal(seq_binaria_x)
        coordenada_x = processar_coordenadas(valor_decimal_x, ordem_matriz)

        print(f'Coordenada x da {qtd_esferas}ª esfera do dragão obtida pelo código binário {seq_binaria_x}: {coordenada_x}')

        # cálculo da coordenada y
        seq_binaria_y = ''
        expressao = input()
        while expressao != '':
            resultado = expressao_prefixa(expressao)
        
            if primo(resultado):
                seq_binaria_y += '1'
            else:
                seq_binaria_y += '0'

            expressao = input()
            
        valor_decimal_y = converte_binario_decimal(seq_binaria_y)
        coordenada_y = processar_coordenadas(valor_decimal_y, ordem_matriz)

        print(f'Coordenada y da {qtd_esferas}ª esfera do dragão obtida pelo código binário {seq_binaria_y}: {coordenada_y}')
        print(f'As coordenadas da {qtd_esferas}ª esfera do dragão são: ({coordenada_x}, {coordenada_y})')
        print()

        coordenadas_esferas.append([coordenada_x, coordenada_y])

        qtd_esferas += 1

print('-' * 74)
print()

# gerador de matriz
matriz = []

for i in range(ordem_matriz):
    linha = []
    for j in range(ordem_matriz):
        if i == x_goku and j == y_goku:
            linha.append('G')
        elif [i, j] in coordenadas_esferas:
            linha.append('☆')
        else:
            linha.append('.')
    matriz.append(linha)

for i in range(len(matriz)):
    print(' '.join(matriz[i]))
print()

# Descobre a trajetória completa do goku
esferas_restantes = coordenadas_esferas.copy()
trajeto = [f"({x_goku}, {y_goku})"]
pos_atual_x, pos_atual_y = x_goku, y_goku

while esferas_restantes:
    esfera_proxima = esferas_restantes[0]
    idx_proxima_esfera = 0
    distancia_minima = distancia_esfera(esfera_proxima[0], esfera_proxima[1], pos_atual_x, pos_atual_y)

    for i in range(1, len(esferas_restantes)):
        esfera_atual = esferas_restantes[i]
        dist_aux = distancia_esfera(esfera_atual[0], esfera_atual[1], pos_atual_x, pos_atual_y)

        if dist_aux < distancia_minima:
            distancia_minima = dist_aux
            esfera_proxima = esfera_atual
            idx_proxima_esfera = i

    pos_atual_x, pos_atual_y = esfera_proxima[0], esfera_proxima[1]
    trajeto.append(f"({pos_atual_x}, {pos_atual_y})")
    esferas_restantes.pop(idx_proxima_esfera)

print("Trajetória completa de Goku:", ' -> '.join(trajeto))

print("Missão cumprida! Conseguimos todas as esferas do dragão!🟠🐉")
