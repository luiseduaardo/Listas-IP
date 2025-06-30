# variáveis globais e lista geral
entrada = ''
lista = []
encerrar = False

# Loop para entrada
while not encerrar:
    entrada = input()

    # condicionais    
    if entrada == 'Anotar ingrediente':
        ingrediente = input()
        lista.append(ingrediente)
    
    elif entrada == 'Ingrediente Urgente!':
        ingrediente = input()
        lista.insert(0, ingrediente)

    elif entrada == 'Saci disse que já tem':
        ingrediente = input()

        for i in lista:
            if i == ingrediente:
                lista.remove(i)
            
    elif entrada == 'Deixar para depois':
        ingrediente = input()

        index_i = lista.index(ingrediente)
        ingrediente_final = lista.pop(index_i)
        lista.append(ingrediente_final)
    
    elif entrada == 'Saci trocou a ordem':
        index_a = int(input())
        index_b = int(input())

        lista[index_a], lista[index_b] = lista[index_b], lista[index_a]
    
    elif entrada == 'Organizar a lista':
        ingrediente_1 = input()
        ingrediente_2 = input()

        index_i1 = lista.index(ingrediente_1)
        index_i2 = lista.index(ingrediente_2)

        lista[index_i1], lista[index_i2] = lista[index_i2], lista[index_i1]

    elif entrada == 'Ler a lista para a vovó':
        for ingrediente in lista:
            if ingrediente == lista[len(lista) - 1]:
                print(f'{ingrediente}')
            else:
                print(f'{ingrediente}, ', end = '')
    
    elif entrada == 'E por hoje é só, pessoal!':
        encerrar = True
        # MELHORIA: print da lista usando função .join()
        print("Pronto, vovó! A lista de compras para o bolo de Narizinho está pronta. Podemos ir ao mercado. A lista final é:", ", ".join(lista))
