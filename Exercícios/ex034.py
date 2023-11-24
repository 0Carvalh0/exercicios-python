sal = float(input("Qual é o salário do funcionário? \033[32;1mR$"))

if sal >= 1250:
    aum = (sal * 10 / 100) + sal
else:
    aum = (sal * 15 / 100) + sal
print("\033[mQuem ganhava \033[32;1mR${:.2f}\033[m passa a ganhar \033[32;1mR${:.2f}\033[m agora.".format(sal, aum))
