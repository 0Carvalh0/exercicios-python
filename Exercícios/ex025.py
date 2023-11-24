print("-" * 20)
nome = str(input("\033[31;1mQual é seu nome completo?\033[m ")).strip()
print("-" * 20)

print("Seu nome tem \033[34;1mSilva\033[m? \033[32;1m{}".format("SILVA" in nome.upper()))
