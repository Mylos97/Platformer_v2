import pygame

class Display:
    WINDOW_SIZE = (1024,768)
    SCREEN = pygame.display.set_mode(WINDOW_SIZE,0,32)
    GAME_SIZE = (WINDOW_SIZE[0]*2,WINDOW_SIZE[1]*2)