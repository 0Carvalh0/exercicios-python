vel = float(input("Qual é a velocidade atual do carro? "))

if vel > 80:
    mul = (vel - 80) * 7
    print("\033[31;1mMULTADO!\033[0;31m Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de \033[33;1mR${:.2f}!".format(mul))
print("\033[32;1mTenha um bom dia! Dirija com segurança!\033[m")
