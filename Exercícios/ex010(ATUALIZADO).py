real = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = real / 4.99 #cotação do dolar no dia 09/09/2023

print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))
