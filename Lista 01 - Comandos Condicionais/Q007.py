cin_x, cin_y = 500, 100
velocidade_byte = 2

lugar = str(input())

if lugar == 'Concha Acústica da UFPE':
    lugar_x, lugar_y = 400, 500
    mensagem_final = "Aqui é muito grande mesmo! Muitos eventos ocorrem por aqui!"

elif lugar == 'Laguinho da UFPE':
    lugar_x, lugar_y = 300, 1000
    mensagem_final = "Nossa, mas esse lago é longe hein?!"

elif lugar == 'Hospital das Clínicas':
    lugar_x, lugar_y = 1000, 1000
    mensagem_final = "Um dos hospitais mais importantes do estado também fica na área do Campus da UFPE!"


elif lugar == 'Ginásio e Pista de Atletismo da UFPE':
    lugar_x, lugar_y = 800, 100
    mensagem_final = "Que legal! O Ginásio é bem perto do CIn!"

distancia = 2 * ((cin_x - lugar_x)**2 + (cin_y - lugar_y)**2)**(1/2)
tempo_s = distancia / velocidade_byte
tempo_m = (tempo_s / 60) + 15

print(f"Byte visitou {lugar}, caminhou {distancia:.0f} metros e gastou {tempo_m:.0f} minutos passeando!")
print(mensagem_final)
