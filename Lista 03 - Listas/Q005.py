print("Vamos lá, Vanellope! Vou te ajudar a montar um carro CINistro!")

# listas iniciais
lista_elementos = []
lista_qualidade = []
lista_descartados = []

acabar = False

# Categorias válidas
rodas_validas = ['Mentos', 'Jujuba']
estrutura_valida = ['Doce largo', 'Bolo de rolo', 'Barra de chocolate', 'Banda de ovo de Páscoa']
volantes_validos = ['Pretzel', 'Donuts']

# Inicializar partes do carro
rodas = ''
rodas_qualidade = ''
estrutura = ''
estrutura_qualidade = ''
volante = ''
volante_qualidade = ''

while not acabar:
    entrada = input()

    # condição de parada
    if entrada == 'Recursos Esgotados':
        acabar = True

    # rei doce roubando ingredientes = descartar todos os elementos do carro
    elif entrada == 'O REI DOCE ESTÁ ROUBANDO TODOS OS INGREDIENTES!':
        print("Ah não!! Ele vai destruir seu carro, Vanellope! CUIDADO")
        if rodas != '':
            lista_descartados.append(rodas)
            rodas = ''
            rodas_qualidade = ''
        if estrutura != '':
            lista_descartados.append(estrutura)
            estrutura = ''
            estrutura_qualidade = ''
        if volante != '':
            lista_descartados.append(volante)
            volante = ''
            volante_qualidade = ''

    else:
        nome, qualidade = entrada.split(' - ')

        if qualidade == 'estragado':
            lista_descartados.append(nome)

        # RODAS
        elif nome in rodas_validas:
            # Se não houver nenhuma atribuição para roda
            if rodas == '':
                rodas = nome
                rodas_qualidade = qualidade
            # Rodas de qualidade mediana
            elif qualidade == 'alta qualidade' and rodas_qualidade != 'alta qualidade':
                lista_descartados.append(rodas)
                rodas = nome
                rodas_qualidade = qualidade
            # Qualquer outra atribuição, isto é, qualidade estragada (segunda verificação)
            else:
                lista_descartados.append(nome)

        # ESTRUTURA
        elif nome in estrutura_valida:
            # Se não houver nenhuma atribuição para estrutura
            if estrutura == '':
                estrutura = nome
                estrutura_qualidade = qualidade
            # Estrutura de qualidade mediana
            elif qualidade == 'alta qualidade' and estrutura_qualidade != 'alta qualidade':
                lista_descartados.append(estrutura)
                estrutura = nome
                estrutura_qualidade = qualidade
            # Qualquer outra atribuição, isto é, qualidade estragada (segunda verificação)
            else:
                lista_descartados.append(nome)

        # VOLANTE
        elif nome in volantes_validos:
            # Se não houver nenhuma atribuição para volante
            if volante == '':
                volante = nome
                volante_qualidade = qualidade
            # Voltante de qualidade mediana
            elif qualidade == 'alta qualidade' and volante_qualidade != 'alta qualidade':
                lista_descartados.append(volante)
                volante = nome
                volante_qualidade = qualidade
            # Qualquer outra atribuição, isto é, qualidade estragada (segunda verificação)
            else:
                lista_descartados.append(nome)

        else:
            lista_descartados.append(nome)

# sem estruturas atribuidas
if rodas == '' or estrutura == '' or volante == '':
    print("Sinto muito, Vanellope. Não consegui te ajudar dessa vez.")

else:
    # pelo menos um dos elementos de alta qualidade
    if 'alta qualidade' in [rodas_qualidade, estrutura_qualidade, volante_qualidade]:
        print(f"Conseguimos! Impossível você não ganhar essa corrida, Vanellope!\nPara fazer o carro você utilizou {estrutura} para ser a estrutura do carro, {volante} para o volante, {rodas} para compor as rodas!")
    else:
        print("Pelo menos anda! Você consegue!")

if len(lista_descartados) > 0:
    print("Alguns doces foram descartados. São eles:")
    print(", ".join(lista_descartados))
