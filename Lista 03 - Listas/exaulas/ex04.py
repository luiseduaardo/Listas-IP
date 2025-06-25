projeto = 'O comando for & o t*pico de estudo deste projeto. Ele & #til para iterar sobre objetos iter@veis. Muitos problemas podem ser resolvidos com o aux!lio do comando for.'

print(f"Projeto corrompido: {projeto}\n")

for letra in '@&!*#':
    if letra == '@':
        projeto = projeto.replace('@', 'á')
    elif letra == '&':
        projeto = projeto.replace('&', 'é')
    elif letra == '!':
        projeto = projeto.replace('!', 'í')
    elif letra == '*':
        projeto = projeto.replace('*', 'ó')
    elif letra == '#':
        projeto = projeto.replace('#', 'ú')

print(f"Projeto corrigido: {projeto}\n")
