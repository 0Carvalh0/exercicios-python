n = int(input("\033[35;1mMe diga um número qualquer:\033[m "))
res = n % 2

if res == 0:
    print("O número {} é \033[34;1mPAR!\033[m".format(n))
else:
    print("O número {} é \033[34;1mÍMPAR!\033[m".format(n))
