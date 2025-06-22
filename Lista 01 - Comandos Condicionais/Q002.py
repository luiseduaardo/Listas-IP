nome = str(input())

a1 = int(input())
n1 = a1

a2 = int(input())
n2 = a2

a3 = int(input())
n3 = a3

a4 = int(input())
n4 = a4 * (10 / 6)

a5 = int(input())
n5 = a5 * (10 / 6)

a6 = int(input())
n6 = a6 * (10 / 6)

media_geral = (n1 + n2 + n3 + n4 + n5 + n6) / 6
print(f"A média de {nome} é {media_geral:.1f}")

# Verifica constância
if n1 <= n2 and n2 <= n3 and n3 <= n4 and n4 <= n5 and n5 <= n6:
    print("Progresso constante! Parabéns pelo esforço!")
else:
    print("Alerta! Queda no rendimento.")

# Verifica se fez as listas
contador = 0

if n1 == 0:
  contador += 1
if n2 == 0:
  contador += 1
if n3 == 0:
  contador += 1
if n4 == 0:
  contador += 1
if n5 == 0:
  contador += 1
if n6 == 0:
  contador += 1

if contador >= 2:
  print("Alerta! Múltiplas listas não respondidas.")

# Verifica a média
if media_geral >= 8:
    print('Parabéns pelo excelente desempenho! Continue "au" sim.')
elif 7 <= media_geral < 8:
    print("Parabéns pelo bom desempenho!")
else:
    print("Alerta! Desempenho abaixo do esperado.")
