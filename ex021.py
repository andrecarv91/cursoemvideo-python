import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('C:/Users/André/Documents/Projects/cursoemvideo-python/Haydn_Cello_Concerto_D-1.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
