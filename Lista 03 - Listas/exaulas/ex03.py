lista = [8, 3, 9, 1, 2, 3]
tam_lista = len(lista)
meio_lista = int(tam_lista / 2)

lista1 = lista[0:meio_lista]
lista2 = lista[meio_lista:]

lista3 = []

for i in range(meio_lista):
    lista3.append(lista1[i] + lista2[i])

print(lista)
print(lista1)
print(lista2)
print(lista3)
