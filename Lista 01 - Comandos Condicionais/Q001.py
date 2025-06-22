fome = input("O Byte está com fome?\n")

if fome == 'sim':
  comida = input("O que você vai dar para ele comer?\n")
  if comida == 'carne' or comida == 'ração' or comida == 'petisco':
    print(f"Byte comeu {comida} e está feliz!")
    print("Depois desse banquete, Byte pode tirar um cochilo feliz")
  else:
    print(f"Byte não gosta de {comida}")
    print("Byte se irritou e foi dormir pra ver se sonha com suas refeições prediletas...")

elif fome == 'não':
  print("Já que Byte não está com fome, ele pode passear")
  chuva = input("Está chovendo?\n")
  if chuva == 'sim':
    print("Já que está chovendo, Byte vai ter que brincar em casa")
  elif chuva == 'não':
    print("Byte está indo passear")
  else:
    print("Insira uma resposta válida")

else:
  print("Insira uma resposta válida")