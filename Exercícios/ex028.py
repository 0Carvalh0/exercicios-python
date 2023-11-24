from random import randint
from time import sleep
print("\033[33;1m-=-" * 20, "\033[m")
print("\033[34;1mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m")
print("\033[33;1m-=-" * 20, "\033[m")

n = int(randint(0, 5))
num = int(input("Em que número eu pensei? "))
print("\033[35;1mPROCESSANDO...\033[m")
sleep(2)
if num == n:
    print("\033[32;1mVOCÊ GANHOU! Você conseguiu me vencer!\033[m")
else:
    print("\033[31;1mGANHEI! Eu pensei no número {} e não no {}!".format(n, num))
