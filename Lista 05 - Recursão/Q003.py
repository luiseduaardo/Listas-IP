def aprimorar_arma(comandos, poder, afinidade, atributos_base, tipo_arma, nome_arma):
    if len(comandos) == 0:
        return poder, afinidade

    comando_atual = comandos[0]
    resto_dos_comandos = comandos[1:]
    
    if comando_atual == '+':
        novo_poder = poder

        if tipo_arma == 'normal':
            novo_poder = poder + 3

        return aprimorar_arma(resto_dos_comandos, novo_poder, afinidade, atributos_base, tipo_arma, nome_arma)
    
    elif comando_atual == '-':
        novo_poder = poder
        if tipo_arma == 'especial':
            novo_poder = poder + 5
        return aprimorar_arma(resto_dos_comandos, novo_poder, afinidade, atributos_base, tipo_arma, nome_arma)
    
    elif comando_atual in ('S', 'D', 'I', 'F', 'A'):
        atributo_upado = ''
        if comando_atual == 'S':
            atributo_upado = 'força'
        elif comando_atual == 'D':
            atributo_upado = 'destreza'
        elif comando_atual == 'I':
            atributo_upado = 'inteligência'
        elif comando_atual == 'F':
            atributo_upado = 'fé'
        elif comando_atual == 'A':
            atributo_upado = 'arcano'

        atributo_bonus_afinidade = ''
        if afinidade == 'fogo':
            atributo_bonus_afinidade = 'força'
        elif afinidade == 'físico':
            atributo_bonus_afinidade = 'destreza'
        elif afinidade == 'mágico':
            atributo_bonus_afinidade = 'inteligência'
        elif afinidade == 'dourado':
            atributo_bonus_afinidade = 'fé'
        elif afinidade == 'oculto':
            atributo_bonus_afinidade = 'arcano'

        bonus_de_poder = 0
        if (atributo_upado in atributos_base) and (atributo_upado == atributo_bonus_afinidade):
            bonus_de_poder = 2
        elif (atributo_upado in atributos_base) or (atributo_upado == atributo_bonus_afinidade):
            bonus_de_poder = 1
            
        novo_poder = poder + bonus_de_poder
        return aprimorar_arma(resto_dos_comandos, novo_poder, afinidade, atributos_base, tipo_arma, nome_arma)
    
    elif isinstance(comando_atual, list):
        poder_antes = poder
        afinidade_antes = afinidade

        nova_afinidade = afinidade
        if afinidade == 'fogo':
            nova_afinidade = 'dourado'
        elif afinidade == 'dourado':
            nova_afinidade = 'oculto'
        elif afinidade == 'oculto':
            nova_afinidade = 'físico'
        elif afinidade == 'físico':
            nova_afinidade = 'mágico'
        elif afinidade == 'mágico':
            nova_afinidade = 'fogo'

        resultado, valor_retornado = aprimorar_arma(comando_atual, poder, nova_afinidade, atributos_base, tipo_arma, nome_arma)

        if resultado == "REVERTER":
            poder_no_momento_da_reversao = valor_retornado
            poder = poder_antes
            afinidade = afinidade_antes
            print("Hmm, não acho que isso vai funcionar...")
            print(f"{nome_arma}: {poder_no_momento_da_reversao} -> {poder}")
            print(f"Afinidade revertida para {afinidade}")
        else:
            poder = resultado
            afinidade = valor_retornado
            
        return aprimorar_arma(resto_dos_comandos, poder, afinidade, atributos_base, tipo_arma, nome_arma)
    
    elif comando_atual == 'R':
        return "REVERTER", poder
    
    else:
        return aprimorar_arma(resto_dos_comandos, poder, afinidade, atributos_base, tipo_arma, nome_arma)

print("Não aguento mais morrer para a Malenia, Blade of Miquella...")
print("Vou refazer minha build!")
print("")

lista_armas = []
loop_entradas = True

while loop_entradas:
    entrada = input()
    if entrada != 'finalizar':
        arma = entrada.split(' - ')
        nome = arma[0]
        tipo = arma[1]
        poder = int(arma[2])
        afinidade = arma[3]
        atributos_base = arma[4:]
        arma_formatada = [nome, tipo, poder, afinidade, atributos_base]
        lista_armas.append(arma_formatada)
    else:
        loop_entradas = False

inventario_final = []

for arma_atual in lista_armas:
    nome = arma_atual[0]
    tipo = arma_atual[1]
    poder_inicial = arma_atual[2]
    afinidade_inicial = arma_atual[3]
    atributos_base = arma_atual[4]
    
    comandos_de_aprimoramento = eval(input())

    poder_final, afinidade_final = aprimorar_arma(comandos_de_aprimoramento, poder_inicial, afinidade_inicial, atributos_base, tipo, nome)
    
    inventario_final.append([nome, poder_final, afinidade_final])
    print(f"{nome} aprimorado!")

arma_fogo = arma_dourado = arma_fisico = arma_magico = arma_oculto = 0

print("Inventário:")
for arma_da_vez in inventario_final:
    nome_arma_final = arma_da_vez[0]
    poder_arma_final = arma_da_vez[1]
    afinidade_arma_final = arma_da_vez[2]

    print(f"- {nome_arma_final}: {poder_arma_final}")
    print(f"- afinidade: {afinidade_arma_final}")

    if afinidade_arma_final == 'fogo':
        print("Fogo... é uma das fraquezas da Malenia!!!")
        arma_fogo += 1
    elif afinidade_arma_final == 'dourado':
        print("É, não acho que uma arma de fé vá me ajudar muito...")
        arma_dourado += 1
    elif afinidade_arma_final == 'físico':
        arma_fisico += 1
    elif afinidade_arma_final == 'mágico':
        arma_magico += 1
    elif afinidade_arma_final == 'oculto':
        arma_oculto += 1

print("")

if arma_fogo > 0 and arma_fogo > arma_dourado and arma_fogo > arma_fisico and arma_fogo > arma_magico and arma_fogo > arma_oculto:
    print("Muitas armas de fogo, ela não vai ter chance!")
elif arma_dourado > 0 and arma_dourado > arma_fogo and arma_dourado > arma_fisico and arma_dourado > arma_magico and arma_dourado > arma_oculto:
    print("Acho que vou ter que refazer meus aprimoramentos...")
else:
    print("Analisando meu inventário agora, acho que consigo vencer, pode vir, Malenia, Blade of Miquella!!")
