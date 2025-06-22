humor = str(input())

senta_vezes = int(input())
patinha_vezes = int(input())
fica_vezes = int(input())
pega_vezes = int(input())

comando = str(input())

if comando == 'Senta':
    senta_vezes += 1
elif comando == 'Dá a patinha':
    patinha_vezes += 1
elif comando == 'Fica':
    fica_vezes += 1
elif comando == 'Pega':
    pega_vezes += 1

senta_aprendeu = True
if senta_vezes < 3:
    senta_aprendeu = False

patinha_aprendeu = True
if patinha_vezes < 3:
    patinha_aprendeu = False

fica_aprendeu = True
if fica_vezes < 3:
    fica_aprendeu = False

pega_aprendeu = True
if pega_vezes < 3:
    pega_aprendeu = False 

if comando == 'Senta':
    if senta_aprendeu and humor != 'Brincalhão':
        print("Byte é o melhor")
    elif humor == 'Brincalhão':
        print("Ele parece estar muito animado para isso!")
    else:
        print("Parece que ele não aprendeu esse truque ainda")

elif comando == 'Dá a patinha':
    if patinha_aprendeu:
        print("Ele é um bom garoto!")
    else:
        print("Parece que ele não aprendeu esse truque ainda")

elif comando == 'Fica':
    if fica_aprendeu and humor != 'Brincalhão':
        print("Ele está aprendendo")
    elif humor == 'Brincalhão':
        print("Ele não consegue ficar parado")
    else:
        print("Parece que ele não aprendeu esse truque ainda")

if comando == 'Pega':
    if pega_aprendeu and humor != 'Preguiçoso':
        print("Ele é muito ágil!")
    elif humor == 'Preguiçoso':
        print("Quem não tem seu momento de preguiça?")
    else:
        print("Parece que ele não aprendeu esse truque ainda")

if senta_aprendeu or patinha_aprendeu or fica_aprendeu or pega_aprendeu:
    print(f"O nosso novo mascote estava {humor} e aprendeu o(s) seguinte(s) truque(s):")
    if senta_aprendeu:
        print("Senta")

    if patinha_aprendeu:
        print("Dá a patinha")

    if fica_aprendeu:
        print("Fica")

    if pega_aprendeu:
        print("Pega")
