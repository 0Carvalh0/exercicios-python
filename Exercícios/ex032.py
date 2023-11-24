from datetime import date
ano = int(input("Qua ano quer analisar? Coloque 0 para analisar o ano atual: "))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\033[32mO ano {} \033[1mê\033[0;1;33m BISSEXTO".format(ano))
else:
    print("\033[31mO ano {} \033[1mNÃO\033[0;31m é \033[33;1mBISSEXTO".format(ano))
