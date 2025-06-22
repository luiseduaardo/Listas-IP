# Frase introdutória
print("🎾🏆 Bem-vindo ao Torneio Fatorial Ping Pong Championship! 🧮🏓\nHoje, o jovem Lavoi enfrentará seu maior desafio: CÁLCULOS!\n")

# Input
# Início do fatorial com laço while
numero_inicio = -1
loop_inicio = True
count_inicio = 0
while loop_inicio:
    if count_inicio == 0:
        numero_inicio = int(input("Qual será o número que marcará o INÍCIO dessa tabuada fatorial?\n"))
    else:
        numero_inicio = int(input())

    count_inicio += 1
    
    if numero_inicio >= 0:
        print(f"O número {numero_inicio} é ótimo como número inicial!")
        loop_inicio = False
    else:
        print(f"O número {numero_inicio} é inválido! O INÍCIO NÃO pode ser NEGATIVO.")

print()

# Fim do fatorial
numero_fim = -1
loop_fim = True
count_fim = 0
while loop_fim:
    if count_fim == 0:
        numero_fim = int(input("Qual será o número que marcará o FIM dessa tabuada fatorial?\n"))
    else:
        numero_fim = int(input())
    
    count_fim += 1

    if numero_fim >= numero_inicio:
        print(f"O número {numero_fim} é ótimo como número final!")
        loop_fim = False
    else:
        print(f"O número {numero_fim} é inválido! O FIM NÃO pode ser MENOR que o número inicial {numero_inicio}.")

print()

# Número sagrado
numero_sagrado = -1
loop_sagrado = True
count_sagrado = 0
while loop_sagrado:
    if count_sagrado == 0:
        numero_sagrado = int(input("Qual será o número cujo FATORIAL será calculado?\n"))
    else:
        numero_sagrado = int(input())
    
    count_sagrado += 1

    if numero_sagrado >= 0:
        print(f"O número {numero_sagrado} é ótimo para o cálculo do fatorial!")
        loop_sagrado = False
    else:
        print(f"O número {numero_sagrado} é inválido! Números válidos são maiores ou iguais a zero.")

print()

# Variáveis globais
numeros = numero_fim - numero_inicio + 1

# Loop
while numero_inicio != numero_fim + 1:
    calculo_fatorial = numero_inicio * numero_sagrado
    valor_fatorial = 1

    # Fatorial
    for i in range(calculo_fatorial, 1, -1):
        valor_fatorial *= i

    # Printar valor do fatorial
    print(f"({numero_inicio} * {numero_sagrado})! = {valor_fatorial}")

    numero_inicio += 1

# Frase final
print("\n🏁 Jornada Finalizada! Lavoi completou todos os estágios do desafio!\n🏓 Que sua energia vital continue brilhando nas próximas batalhas!")
