import pygame
pygame.mixer.init()

pygame.mixer.music.load("doom_music.mp3")
pygame.mixer.music.play(-1)  # loop infinito
