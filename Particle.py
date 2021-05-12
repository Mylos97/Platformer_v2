import pygame, random
from GameObject import *
from Display import *

class Particle(GameObject):
    COLORS = {"player_bullet" : (140,255,251), "test" : (0,0,0)}

    def __init__(self, pos, start_vel ,type_bullet):
        super().__init__(pos)
        self.color = Particle.COLORS[type_bullet]
        self.spread = 2

        
        self.vel[0] = -random.uniform(-0.2,0.2)*start_vel[0] + random.uniform(-self.spread,self.spread)
        self.vel[1] = -random.uniform(-0.2,0.2)*start_vel[1] + random.uniform(-self.spread,self.spread)
        self.timer = 0
        self.size = [random.randint(3,5),random.randint(3,5)]
        self.life_time = random.randint(20,50)
        self.id = 'particle'
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.surf_img = pygame.Surface((self.size[0],self.size[1]))
        self.surf_img.fill(self.color)
        self.surf_img.set_alpha(180)




    
    def loop(self, DT):
        self.timer += 1
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])


        self.surf_img.set_alpha(180 - self.timer*7)

        if self.timer > self.life_time:
            self.remove()
        

    def draw(self, camera):
        Display.SCREEN.blit(self.surf_img, camera.apply_offset(self.rect))