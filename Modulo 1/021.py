import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('21.wav')
pygame.mixer.music.play()
pygame.event.wait()