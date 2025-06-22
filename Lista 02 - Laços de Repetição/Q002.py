# Definir variáveis iniciais
uniforme = isotonico = raquete = toalha = sabotagem_count = 0
acabou = False
sabotagem = False

# Laço de repetição enquanto estiver recebendo entradas
while not acabou:
    # Input
    entrada = str(input())

    # Sabotagem - retorna para o começo do laço e pergunta qual material foi sabotado
    if entrada == 'Sabotagem':
        sabotagem = True
        sabotagem_count += 1
    
    # Encerra o laço
    elif entrada == 'FIM':
        acabou = True

    # Outputs
    # Uniforme
    elif entrada == 'Uniforme':
        if sabotagem:
            uniforme -= 1
            print("O sueco está roubando as camisas de Hugo!")
        # Caso seja contabilizado o uniforme
        else:
            uniforme += 1
            print(f"Tava faltando camisa! Agora temos {uniforme} uniforme(s)")
        sabotagem = False
    
    # Isotônico
    elif entrada == 'Isotônico':
        if sabotagem:
            isotonico -= 1
            print("O sueco está sabotando a hidratação de Hugo!")
        # Caso seja contabilizado o isotônico
        else:
            isotonico += 1
            print(f"Bora garantir a hidratação! Agora temos {isotonico} isotônico(s)")
        sabotagem = False

    # Raquete contabilizada
    elif entrada == 'Raquete':
        if sabotagem:
            raquete -= 1
            print("O sueco está roubando as raquetes de Hugo!")
        # Caso seja contabilizado a raquete
        else:
            raquete += 1
            print(f"Mais uma raquete saindo! Agora temos {raquete} raquete(s)")
        sabotagem = False

    # Toalha contabilizada
    elif entrada == 'Toalha':
        if sabotagem:
            toalha -= 1
            print("O sueco está roubando as toalhas de Hugo!")
        # Caso seja contabilizado a toalha
        else:
            toalha += 1
            print(f"Mais uma toalha saindo! Agora temos {toalha} toalha(s)")
        sabotagem = False

# Imprimir relatório
total_materiais = uniforme + raquete + toalha + isotonico

print(f"""Bora ver o relatório final dos materiais!
Uniforme: {uniforme} unidade(s).
Isotônico: {isotonico} unidade(s).
Raquete: {raquete} unidade(s).
Toalha: {toalha} unidade(s).""")

# Total de materiais for 0 e houver sabotagem
if total_materiais == 0 and sabotagem_count != 0:
    print("Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!")

# Total de materiais for 0 e sem sabotagem
elif total_materiais == 0 and sabotagem_count == 0:
    print("Vish... Parece que vão faltar materiais para garantir a vitória do nosso atleta.")

# Tem materiais, mas não todos
elif total_materiais != 0 and (uniforme == 0 or isotonico == 0 or raquete == 0 or toalha == 0):
    print("Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!")

# Casos restantes
else:
    print("Tudo pronto! Não vai faltar nada para mais um título de Hugo Calderano!")
