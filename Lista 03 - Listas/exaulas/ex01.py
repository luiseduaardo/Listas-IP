produtos_vendidos = ['martelo', 'alicate', 'chave de fenda', 'chave estrela', 'tesoura']
produtos_estoque = ['martelo', 'alicate', 'martelo', 'martelo', 'chave de fenda', 'alicate', 'chave estrela']

produto = input("Qual produto você deseja consultar? ")

# Verifica se a loja vende
vende_produto = False

for prod_vendido in produtos_vendidos:
    if prod_vendido == produto:
        vende_produto = True

if vende_produto:
    # Consulta o estoque para ver disponibilidade
    contador = 0
    for prod_estoque in produtos_estoque:
        if prod_estoque == produto:
            contador += 1
    
    if contador == 0:
        print(f"Estamos sem estoque de {produto}!")
    else:
        print(f"Nós temos {contador} unidades de {produto} na nossa loja!")

else:
    print(f"Não vendemos {produto} na nossa loja!")
