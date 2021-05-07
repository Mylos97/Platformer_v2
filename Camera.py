import pygame
from Display import * 

class Camera:

    def __init__(self, width, height):
        self.camera = pygame.Rect(0,0,width,height)
        self.width = width
        self.height = height

    def apply_offset(self, entity_rect):
        return entity_rect.move(self.camera.topleft)

    def update_offset(self, target_rect):
        x = - target_rect.centerx + int(Display.WINDOW_SIZE[0]/2) 
        y = - target_rect.centery + int(Display.WINDOW_SIZE[1]/2)

        ## Stop the scrolling outside of map 
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - Display.WINDOW_SIZE[0]), x)
        y = max(-(self.height - Display.WINDOW_SIZE[1]), y)


        self.camera = pygame.Rect(x, y, self.width,self.height)