nome = input("\033[31mDigite seu nome completo:\033[m ").strip().split()

print("\033[34mMuito prazer em te conhecer!\033[m")
print("Seu primeiro nome é \033[36m{}\033[m".format(nome[0]))
print("Seu último nome é \033[36m{}\033[m".format(nome[len(nome) - 1]))
