num_lin = int(input("Número de linhas: "))
num_col = int(input("Número de colunas: "))

matriz = []

for i in range(num_lin):
    linha_matriz = []
    for j in range(num_col):
        linha_matriz.append(int(input(f"Elemento {i} x {j}: ")))
    matriz.append(linha_matriz)

print("MATRIZ NORMAL:")
for linha in range(num_lin):
    print(matriz[linha])

print("\nMATRIZ TRANSPOSTA:")

matriz_t = []

for k in range(num_col):
    linha_matriz_t = []
    for l in range(num_lin):
        linha_matriz_t.append(matriz[l][k])
    matriz_t.append(linha_matriz_t)

for linha_t in range(num_col):
    print(matriz_t[linha_t])
