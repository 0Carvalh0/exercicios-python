print("\033[35;1m-=" * 20)
print("ANALISADOR DE TRIÂNGULOS")
print("-=" * 20, "\033[m")

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima \033[32;1mPODEM FORMAR\033[m um triângulo!")
else:
    print("Os segmentos acima \033[31;1mNÃO PODEM FORMAR\033[m um triângulo")
