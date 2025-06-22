print("A partida de revanche de Hugo Calderano contra a China, Potência Mundial do Tênis de Mesa, está prestes a começar!")

# Define inputs (enquanto o adversário não for chinês, seguir perguntando)
nacionalidade_atleta = ''
nome_atleta = ''

while nacionalidade_atleta != 'Chinês':
    nacionalidade_atleta = str(input())
    nome_atleta = str(input())

    if nacionalidade_atleta == 'Chinês':
        print(f"{nome_atleta} foi convocado para vingar o massacre feito durante o mundial de Tênis de Mesa!")
    else:
        print(f"O {nome_atleta} não poderá disputar a partida, pois sua nacionalidade não é chinesa!")

# Define variáveis globais
acabar_partida = False
pontos_hugo = pontos_chines = 0

while not acabar_partida:
    numero_chines = int(input())
    numero_hugo = int(input())

    if numero_chines > numero_hugo:
        pontos_chines += 1
        if numero_chines >= 2 * numero_hugo:
            pontos_chines += 1
            print("Que bela jogada, essa merece ponto extra!")
        else:
            print("Vamos Hugo, não deixe ele vencer!")
    
    elif numero_hugo > numero_chines:
        pontos_hugo += 1
        if numero_hugo >= 2 * numero_chines:
            pontos_hugo += 1
            print("Que bela jogada, essa merece ponto extra!")
        else:
            print("Hugo Calderano marcou um ponto de maneira esplendida!")
    
    elif numero_chines == numero_hugo:
        pontos_hugo += 1
        print("A bola bateu na rede e felizmente caiu no lado adversário!!! Hugo marca mais um ponto!")

    if (pontos_chines - pontos_hugo >= 3) or (pontos_hugo - pontos_chines >= 3):
        acabar_partida = True

if pontos_hugo == 3:
    print("Hugo Calderano mostrou o porquê ele é o atual campeão mundial, uma partida relâmpago!")
elif 3 < pontos_hugo <= 10:
    print("Não demorou muito, mas o resultado era esperado, Hugo Calderano vence!")
elif pontos_hugo > 10:
    print("Demorou, mas o previsto aconteceu! Hugo Calderano não deixa dúvidas do porquê ele é o Campeão Mundial!")

print(f"Placar Final: {pontos_hugo}x{pontos_chines}\n")

#Após o final da partida, a CTTA irá premiar Hugo Calderano pelo seu ótimo desempenho. O prêmio será uma maquete de uma mesa de tênis de mesa, que terá a largura definida pela quantidade de pontos do Hugo Calderano e o seu comprimento definido pela quantidade de pontos do seu adversário. Uma rede deve cortar a mesa ao meio do comprimento.

#Obs. 1: Se o comprimento for par, reduza 1 unidade do comprimento para ser possível encontrar o meio para a rede.

#Obs. 2: Caso o comprimento seja menor ou igual 2, ele será completado minimamente para que seja possível construir a maquete. Ou seja, valerá 3.

#Obs. 3: Entenda a largura como sendo paralelo ao eixo x e o comprimento como sendo paralelo o eixo y.'''

comprimento = pontos_chines
largura = pontos_hugo

if comprimento <= 2:
    comprimento = 3

if comprimento % 2 == 0:
    comprimento -= 1

linha_rede = comprimento // 2 + 1

print("Aqui está o merecido prêmio de Hugo Calderano:")

print("-" * largura)

for linha in range(2, comprimento):
    print("|", end = '')
    if linha == linha_rede:
        print("#" * (largura - 2), end = '')
    else:
        print(" " * (largura - 2), end = '')
    print("|")

print("-" * largura)
