km = float(input("\033[31;1mQual é a distância da sua viagem?\033[m "))

print("Você está prestes a começar uma viagem de \033[33;1m{}Km.\033[m".format(km))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
# preço = km * 0.50 if km <= 200 else km * 0.45 if in line

print("E o preço da sua passagem será de \033[32;1mR${:.2f}".format(preço))
