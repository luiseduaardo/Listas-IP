dia_semana = str(input())
turno = str(input())

if dia_semana == 'segunda-feira' or dia_semana == 'sexta-feira':
    hora = int(input())

local = str(input())
humor = str(input())

# Outputs dia da semana
if dia_semana == 'segunda-feira' and hora < 7:
    print("Byte acordou em plena madrugada, quem tá acordado(a) pra levar ele essa hora?!")
elif dia_semana == 'sexta-feira' and hora >= 16:
    print("SEXTOU, quem vai levar Byte pra bater pata por aí??")

# Outputs local
if local == 'labirinto':
    print("Byte quer passear num labirinto, cuidado pra não se perder!")

# Outputs humor
if humor == 'pura energia':
    print("Byte está energizado com a ideia de passear, leve uma bolinha pra ele!")
elif humor == 'calminho':
    print("Byte está calminho, o passeio vai ser na paz, pode confiar!")
elif humor == 'rebelde':
    print("Byte está se comportando mal hoje, vamos ver quem terá coragem para acompanhá-lo em seu passeio")

# Acompanhante
if local == 'labirinto':
    if humor != 'rebelde':
        print("A prof. Fernanda Madeiral aceitou o desafio: labirinto caótico, uma Python no caminho… e Byte como companheiro. Afinal, o que pode dar errado?")
    else:
        print("Mestre Iyoda e Byte adentram o labirinto. Uma missão ousada e um destino desconhecido.")

elif turno == 'manhã' and dia_semana != 'segunda-feira':
    print(f"Nesta manhã de {dia_semana}, é o Prof. Sergio Soares quem comanda o passeio com Byte")
    
elif local == 'parque' or local == 'bosque':
    if dia_semana == 'segunda-feira' and turno == 'manhã':
        print(f"{dia_semana}: uns indo pro trabalho, outros lidando com o Byte. Prof. Ricardo Massa escolheu a segunda opção. Força, guerreiro. {local}, aí vamos nós.")
    elif turno == 'tarde':
        print(f"Sol da tarde, coleira na mão: prof. Ricardo Massa entra em cena para o passeio com Byte.")
    elif turno == 'noite':
        print(f"Quando a noite cai e Byte chama, Mestre Iyoda atende. Que o {local} esteja preparado para essa dupla!")
