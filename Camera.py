from random import randint
import pygame, random
from Display import * 

class Camera:

    SCREEN_SHAKE = False
    SCREEN_SHAKE_TIMER = 0

    def __init__(self, width, height):
        self.camera = pygame.Rect(0,0,width,height)
        self.width = width
        self.height = height




    def apply_offset(self, entity_rect):
        return entity_rect.move(self.camera.topleft)

    def update_offset(self, target_rect):
        if not Camera.SCREEN_SHAKE: 
            x = - target_rect.centerx + int(Display.WINDOW_SIZE[0]/2) 
            y = - target_rect.centery + int(Display.WINDOW_SIZE[1]/2)

            self.camera = pygame.Rect(x, y, self.width,self.height)

        else:
            ## Screen shake every 4 frames ##
            if Camera.SCREEN_SHAKE_TIMER%4 == 0:
                ## Screen shake ##
                x = - target_rect.centerx + int(Display.WINDOW_SIZE[0]/2) + random.randint(-8,8) 
                y = - target_rect.centery + int(Display.WINDOW_SIZE[1]/2) + random.randint(-8,8) 
            else:
            ## Normal camera pos ##
                x = - target_rect.centerx + int(Display.WINDOW_SIZE[0]/2) 
                y = - target_rect.centery + int(Display.WINDOW_SIZE[1]/2) 

            self.camera = pygame.Rect(x, y, self.width,self.height)
            
            Camera.SCREEN_SHAKE_TIMER += 1

            if Camera.SCREEN_SHAKE_TIMER > 12:
                Camera.SCREEN_SHAKE_TIMER = 0
                Camera.SCREEN_SHAKE = False


             