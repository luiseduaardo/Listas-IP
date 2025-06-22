# Mesada e cotação
mesada_dolar = int(input())
cotacao_dolar = float(input())
mesada_reais = mesada_dolar * cotacao_dolar

# Input - gastos
gasto_racao = int(input())
gasto_aluguel = int(input())
gasto_onibus = int(input())

gasto_total = gasto_racao + gasto_aluguel + gasto_onibus

# Output - gastos
if gasto_total > mesada_reais:
    print("Eu acho melhor você ir morar comigo no Cin! O RU é só 4 reais e lá no DA tem saco de dormir!")
elif gasto_total == mesada_reais:
    print("Vai dar pra alugar sua casa, mas sugiro que você vá trabalhar se quiser gastar com outra coisa!")
else:
    print("Me chama pra sua casa um dia pra gente comer Pedigree! Com essa grana dá pra alugar uma ManCão!")

# Maiores gastos
if gasto_racao > gasto_onibus and gasto_racao > gasto_aluguel:
    print("A inflaCão deu pros cachorros, viu! Sugiro que você vá no Coffee Break dos calouros e leve toda a comida!")
    maior_gasto = "Ração"
elif gasto_aluguel > gasto_onibus and gasto_aluguel > gasto_racao:
    print("Não está fácil pra ninguém... Tenta dividir o aluguel com algum estudante aí!")
    maior_gasto = "Aluguel"
elif gasto_onibus > gasto_aluguel and gasto_onibus > gasto_racao:
    print("Você consegue voar, por que quer orçamento de ônibus? Vai ser feliz!")
    maior_gasto = "Ônibus"

# Relatório
print(f"MESADA (dólares): {mesada_dolar:.2f} dólares")
print(f"MESADA (reais): {mesada_reais:.2f} reais")
print(f"MAIOR GASTO: {maior_gasto}")
