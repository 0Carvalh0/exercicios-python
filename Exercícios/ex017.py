import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (ca ** 2 + co ** 2) ** (1 / 2)
# hip = math.hypot(co, ca)

print("A hipotenusa vai medir {:.2f}".format(hi))
