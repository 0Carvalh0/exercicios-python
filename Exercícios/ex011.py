lar = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
a = lar * alt

print("Sua parede tem dimensão de {}x{} e sua área é de {}m².".format(lar, alt, a))
t = a / 2
print("Para pintar essa parede, você precisará de {}l de tinta.".format(t))
