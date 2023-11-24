print("\033[31m-" * 20)
frase = input("Digite uma frase: ").strip().upper()
print("-" * 20, "\033[m")

print("\033[34;2mA letra\033[m \033[35mA\033[34m aparece \033[32m{}\033[34m vezes na frase.".format(frase.count("A")))
print("A primeira letra \033[35mA\033[34m apareceu na posição \033[32m{}\033[m".format(frase.find("A") + 1))
print("\033[34mA última letra \033[35mA\033[34m apareceu na posição \033[32m{}\033[m".format(frase.rfind("A") + 1))
