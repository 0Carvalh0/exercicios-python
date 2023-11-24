import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
print("\033[31mVocê esta ouvindo ODISSEIA - LVCAS!")
pygame.event.wait()
