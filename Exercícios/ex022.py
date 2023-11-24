from time import sleep
nome = input("Digite seu nome completo: ").strip()

print("-" * 20)
print("Analisando seu nome...")
print("-" * 20)
sleep(2)
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))

# print("Seu primeiro nome tem ao todo {} letras".format(nome.find(" ")))
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))
