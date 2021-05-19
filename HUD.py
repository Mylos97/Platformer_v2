import pygame

from Display import *
from Player import *

class HUD:

    def __init__(self, player):
        self.player = player
        self.rect = pygame.Rect(int(Display.WINDOW_SIZE[0]*0.05),int(Display.WINDOW_SIZE[1]*0.05), Display.WINDOW_SIZE[0]*0.75, Display.WINDOW_SIZE[1]*0.05)

        self.surf_img = pygame.Surface((self.rect.width,self.rect.height))
        self.surf_img.fill((255,255,255))
        self.surf_img.set_alpha(150)
    
    def draw(self):
        Display.SCREEN.blit(self.surf_img, self.rect)

    def update_HUD(self):
        if not Player.PLAYER_HEALTH <= 0:
            self.rect.width = Display.WINDOW_SIZE[0]*0.75*(Player.PLAYER_HEALTH/100)
        else:
            self.rect.width = 1


        self.surf_img = pygame.Surface((self.rect.width,self.rect.height))
        self.surf_img.fill((255,255,255))
        self.surf_img.set_alpha(150)
