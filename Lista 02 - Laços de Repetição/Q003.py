# Variáveis globais
classica = caneta = classineta = 0
nome1, pontos1 = '', -1
nome2, pontos2 = '', -1
nome3, pontos3 = '', -1

# Input na quantidade de pessoas
entrevistados = int(input())

# Laço de repetição com a quantidade de pessoas entrevistadas
for i in range(entrevistados):
    # Input no voto
    voto = str(input())

    # Condicionais para aumentar votos
    if voto == 'Clássica':
        classica += 1
    elif voto == 'Caneta':
        caneta += 1
    elif voto == 'Classineta':
        classineta += 1

# Definir ranking
if classica > caneta and classica > classineta:
    nome1, pontos1 = 'Clássica', classica
    if caneta > classineta:
        nome2, pontos2 = 'Caneta', caneta
        nome3, pontos3 = 'Classineta', classineta
    else:
        nome2, pontos2 = 'Classineta', classineta
        nome3, pontos3 = 'Caneta', caneta

elif caneta > classica and caneta > classineta:
    nome1, pontos1 = 'Caneta', caneta
    if classica > classineta:
        nome2, pontos2 = 'Clássica', classica
        nome3, pontos3 = 'Classineta', classineta
    else:
        nome2, pontos2 = 'Classineta', classineta
        nome3, pontos3 = 'Clássica', classica

else:
    nome1, pontos1 = 'Classineta', classineta
    if classica > caneta:
        nome2, pontos2 = 'Clássica', classica
        nome3, pontos3 = 'Caneta', caneta
    else:
        nome2, pontos2 = 'Caneta', caneta
        nome3, pontos3 = 'Clássica', classica

# Output com ranking
print("Estamos calculando... tão rápido quanto dar Run no Dikastis...")
print(f"1º lugar: {nome1} ({pontos1} votos)")
print(f"2º lugar: {nome2} ({pontos2} votos)")
print(f"3º lugar: {nome3} ({pontos3} votos)")

# Condicional diferença de votos
if nome1 == 'Clássica' and (pontos1 - pontos2) >= 5:
    print("Podemos ver que a influência do grande Hugo Calderano foi disseminada pelos corredores do CIn!")
