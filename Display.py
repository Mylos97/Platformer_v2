import pygame

class Display:
    WINDOW_SIZE = (1024,768)
    SCREEN = pygame.display.set_mode(WINDOW_SIZE,0,32)
    GAME_SIZE = (WINDOW_SIZE[0]*3,WINDOW_SIZE[1]*3)
    PLATFORM_RECT = pygame.Rect(0, 0, GAME_SIZE[0], GAME_SIZE[1])