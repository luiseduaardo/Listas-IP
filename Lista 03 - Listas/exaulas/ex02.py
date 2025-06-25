produtos_vendidos = ['martelo', 'alicate', 'chave de fenda', 'chave estrela', 'tesoura']
produtos_estoque = ['martelo', 'alicate', 'martelo', 'martelo', 'chave de fenda', 'alicate', 'chave estrela']

for prod_vendido in produtos_vendidos:
    contador = 0
    for prod_estoque in produtos_estoque:
        if prod_estoque == prod_vendido:
            contador += 1
    print(f"Existe(m) {contador} {prod_vendido}(s) no nosso estoque!")
