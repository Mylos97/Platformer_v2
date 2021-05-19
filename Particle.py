import pygame, random

from pygame.constants import BLEND_RGB_ADD
from GameObject import *
from Display import *

class Particle(GameObject):
    COLORS = {"player_bullet" : (140,255,251), "test" : (100,100,100)}

    def __init__(self, pos, start_vel ,type_bullet):
        super().__init__(pos)
        self.color = (random.randint(90,180),random.randint(150,250),random.randint(90,180))
        
        self.spread = 2

        self.alive = True
        self.vel[0] = -random.uniform(-0.2,0.2)*start_vel[0] + random.uniform(-self.spread,self.spread)
        self.vel[1] = -random.uniform(-0.2,0.2)*start_vel[1] + random.uniform(-self.spread,self.spread)
        self.timer = 0
        self.size = [random.randint(3,5),random.randint(3,5)]
        self.life_time = random.randint(20,50)
        self.id = 'particle'
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.surf_img = pygame.Surface((self.size[0],self.size[1]))
        self.surf_img.fill(self.color)
        self.surf_img.set_alpha(random.randint(140,250))



        self.lighting_rect = pygame.Rect(-99999,-9999, self.size[0] + 1, self.size[1] + 1)

    
    def loop(self, DT):
        self.timer += 1
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        self.lighting_rect.x = self.pos[0] - 1
        self.lighting_rect.y = self.pos[1] - 1

        self.surf_img.set_alpha(180 - self.timer*random.randint(5,7))

        self.vel[0] *= 0.95
        self.vel[1] *= 0.95


        if self.surf_img.get_alpha() == 0:
            self.alive = False
        

    def draw(self, camera):
        Display.SCREEN.blit(self.rect_surf(self.size[0],(5,5,5)), camera.apply_offset(self.lighting_rect) , special_flags = BLEND_RGB_ADD)
        Display.SCREEN.blit(self.surf_img, camera.apply_offset(self.rect))