# input número de ondas
numero_ondas = int(input())

# inicializa pontuação e tamanho de onda
herois_pont = viloes_pont = 0
maior_onda = 0

# lista da maior onda
lista_maior_onda = []

# flag para indicar de quem é a maior onda
viloes = False
herois = False

for i in range(numero_ondas):
    onda_atual = i
    sequencia = input()
    pre_ordem = sequencia.split(', ')
    ordem = []
    
    # splita a onda atual do segundo ao penúltimo herói e adiciona em outra lista
    for j in range(1, (len(pre_ordem) - 1)):
        aux = pre_ordem[j].split('-')
        ordem.append(aux)

    # inicializa variável de qtd de heróis
    herois_qtd = viloes_qtd = 0

    # define a quantidade de heróis por onda
    for k in range(len(ordem)):
        if ordem[k][0] == 'H':
            herois_qtd += 1
        elif ordem[k][0] == 'V':
            viloes_qtd += 1
     
    diferenca = herois_qtd - viloes_qtd

    # condicionais de pontuação de onda
    if abs(diferenca) > maior_onda:
        maior_onda = abs(diferenca)
        idx_maior_onda = onda_atual + 1
        lista_maior_onda = pre_ordem
        if diferenca > 0:
            herois = True
            viloes = False
        else:
            herois = False
            viloes = True

    if diferenca > 0:
        herois_pont += 1
    
    elif diferenca < 0:
        viloes_pont += 1

# output final
if herois or viloes:
    if herois:
        print(f"🌀Onda {idx_maior_onda} foi a menos acirrada e a mais favorável para os heróis!")
    elif viloes:
        print(f"🌀Onda {idx_maior_onda} foi a menos acirrada e a mais favorável para os vilões!")

    print("Participantes analisados:", ", ".join(lista_maior_onda))

else:
    print("🌀Nenhuma onda foi selecionada como a menos acirrada e a mais favorável para nenhum do dois lados!")

# resultado geral das ondas
print(f"Agora vamos ao resultado geral das ondas...\nHeróis: {herois_pont} | Vilões: {viloes_pont}")

if herois_pont > viloes_pont:
    print("Ufa, os heróis dominaram! Central City está seguro outra vez")
elif herois_pont < viloes_pont:
    print("Ah, não. Os vilões vão dominar Central City e mandar todos os heróis embora!")
else:
    print("Ninguém é mais forte que ninguém. Heróis e vilões vão ter que entrar em consenso para viverem no mesmo espaço")
