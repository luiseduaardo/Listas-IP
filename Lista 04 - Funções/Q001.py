def calcular_distancia(x, y):
    distancia = ((x ** 2) + (y ** 2))**(1/2)
    return distancia

numero_objetos = int(input())
lista_distancias = []
lista_index = []

for i in range(numero_objetos):
    nome_objeto = input()
    coordenada_x = int(input())
    coordenada_y = int(input())

    if nome_objeto == 'rocha':
        print("Radar: Rocha detectada! Bulma resmunga: 'Só um pedregulho cósmico... Sem valor para mim!'")

    elif nome_objeto == 'árvore':
        print("Radar: Árvore à vista! Bulma comenta: 'Interessante, mas não brilha como uma esfera. Próximo alvo!'")

    elif nome_objeto == 'nave':
        print("Radar: Sinal de nave! Bulma alerta: 'Pode ser Pilaf ou a Patrulha Vermelha! Melhor ficar atenta, mas o foco são as esferas!'")

    elif nome_objeto == 'esfera':
        distancia = calcular_distancia(coordenada_x, coordenada_y)

        lista_distancias.append(distancia)
        lista_index.append(i)

    else:
        print(f"Radar: Detectado um(a) {nome_objeto}. Não parece ser uma esfera... Continuando a busca.")

if len(lista_distancias) == 0:
    print("Radar varreu a área. Nenhuma esfera do dragão à vista desta vez!")

else:
    distancia_prioritaria = min(lista_distancias)
    idx_prioritaria = lista_index[lista_distancias.index(distancia_prioritaria)] + 1

    print(f"ALVO PRIORITÁRIO: Esfera | Distância: {distancia_prioritaria:.2f}m | Detecção Original: {idx_prioritaria}°")
