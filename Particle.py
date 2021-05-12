import pygame, random
from GameObject import *
from Display import *

class Particle(GameObject):
    COLORS = {"player_bullet" : (140,255,251), "test" : (0,0,0)}

    def __init__(self, pos, start_vel ,type_bullet):
        super().__init__(pos)
        self.color = Particle.COLORS[type_bullet]
        self.vel[0] = -random.uniform(0.1,0.35)*start_vel[0] + random.uniform(-0.5,0.5)
        self.vel[1] = -random.uniform(0.1,0.35)*start_vel[1] + random.uniform(-0.5,0.5)
        self.timer = 0
        self.size = [random.randint(3,5),random.randint(3,5)]
        self.life_time = random.randint(20,50)
        self.id = 'particle'
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        print(self.pos)
        self.surf_img = pygame.Surface((self.size[0],self.size[1]))
        self.surf_img.fill(self.color)
        self.surf_img.set_alpha(180)


    
    def loop(self, DT):
        self.timer += 1
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])


        self.surf_img.set_alpha(180 - self.timer*6)

        if self.timer > self.life_time:
            self.remove()
        

    def draw(self, camera):
        Display.SCREEN.blit(self.surf_img, camera.apply_offset(self.rect))