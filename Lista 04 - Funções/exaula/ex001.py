from random import randint

def jogo_adivinhacao():
    num = randint(0, 100)
    chute = int(input("Chute um número no intervalo de 1 à 100: "))
    acertou = False

    while not acertou:
        if chute == num:
            print("parabéns, você acertou o número: ")
            acertou = True
        elif chute > num:
            chute = int(input("Tente um número menor: "))
        else:
            chute = int(input("Tente um número maior: "))
    else:
        print("fim de jogo")

acabar = False
while not acabar:
    jogo_adivinhacao()

    continuar = input("Deseja continuar? ")

    if continuar == 'não':
        acabar = True
