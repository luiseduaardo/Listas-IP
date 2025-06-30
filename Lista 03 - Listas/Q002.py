# inputs iniciais
nivel_jinwoo = int(input())
qtd_criaturas = int(input())

# variáveis globais e lista
acabar = False
morreu = False
lista_criaturas = []

# loop que continua até o fim do programa
for i in range(qtd_criaturas):
    nome_criatura = input()
    nivel_criatura = int(input())

    # primeira condição de parada
    if nivel_criatura >= nivel_jinwoo:
        acabar = True
        morreu = True
    
    else:
        acao = input()

        # adicionar criatura ao exército
        if acao == 'Erga-se':
            lista_criaturas.append(nome_criatura)
            nivel_jinwoo += nivel_criatura // 3

# outputs finais
if morreu:
    print(f"Jin-Woo foi derrotado por {nome_criatura}...")

else:
    print("Jin-Woo sobreviveu à caçada, um verdadeiro Monarca das Sombras mesmo!")

print("===== Exército das Sombras de Jin-Woo =====")

if len(lista_criaturas) == 0:
    print("Jin-Woo não conseguiu formar seu exército...")  

# output exército final e quantidades
else:
    auxiliar = []
    for i in range(len(lista_criaturas)):
        item = lista_criaturas[i]

        jacontado = False

        for j in range(len(auxiliar)):
            if item == auxiliar[j]:
                jacontado = True
        
        if not jacontado:
            # MELHORIA: uso da função .count()
            contador = lista_criaturas.count(item)
            
            print(f"{item}: {contador}")
        
            auxiliar.append(item)
