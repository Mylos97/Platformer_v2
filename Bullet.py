import pygame, math

from pygame.constants import BLEND_RGB_ADD
from GameObject import *
from Particle import *
from Display import *
from Mediator import *

class Bullet(GameObject):

    def __init__(self, pos, dir, bullet_type = "standard"):
        super().__init__(pos)
        self.pos[0] += 4
        self.pos[1] += 4
        self.size = [8,8]
        self.lifetime = 120
        self.vel = [int(dir[0]*6), int(dir[1]*6)]
        self.bullet_type = bullet_type
        self.timer = 0
        self.id = bullet_type
        self.img = pygame.image.load("Graphics/Bullet.png")
        self.wait_frames = 0
        self.show_frames = 3
        self.radius_lighting = self.img.get_width()

        self.rect = pygame.Rect(-99999,-99999,self.img.get_width(),self.img.get_height())

        self.rect_lighting = pygame.Rect(-99999,-99999,self.radius_lighting,self.radius_lighting)
        self.rect_lighting2 = pygame.Rect(-99999,-99999,self.radius_lighting,self.radius_lighting)
        self.lighting_int = 10


        self.rotate_int = 0
        self.update_image()

 
    def loop(self, DT):
        self.img.set_alpha(int(255 - math.pow(self.timer,1.2)))

        self.pos[0] += self.vel[0]*self.wind_speed
        self.pos[1] += self.vel[1]*self.wind_speed

        if self.wait_frames > 2:
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]

            self.rect_lighting.x = self.pos[0] - self.radius_lighting
            self.rect_lighting.y = self.pos[1] - self.radius_lighting

            self.rect_lighting2.x = self.pos[0] - self.radius_lighting*2
            self.rect_lighting2.y = self.pos[1] - self.radius_lighting*2

        self.wait_frames += 1
        self.timer += 1

        if self.bullet_type == 'missile_bullet_red':
            self.vel[0] *= 0.98
            self.vel[1] *= 0.98

        if self.timer%12 == 0:
            self.lighting_int -= 1
        

        
        if self.apply_wind_speed and random.randint(0, 2) == 1:
            self.wind_speed -= 0.01

        if self.img.get_alpha() == 0:
            self.remove()

        

    def draw(self, camera):
        if self.wait_frames > self.show_frames:
                Display.SCREEN.blit(self.rect_surf(self.radius_lighting*5, (self.lighting_int,self.lighting_int,self.lighting_int)), camera.apply_offset(self.rect_lighting2), special_flags = BLEND_RGB_ADD)

                Display.SCREEN.blit(self.rect_surf(self.radius_lighting*3, (self.lighting_int,self.lighting_int,self.lighting_int)), camera.apply_offset(self.rect_lighting), special_flags = BLEND_RGB_ADD)
                Display.SCREEN.blit(self.img,camera.apply_offset(self.rect))
                



    def collision(self):

        for collision in self.collision_ids:
            if collision == 'enemy' and not self.bullet_type == 'enemy_bullet':
                if len(Mediator.PARTICLES) < 25:
                    for i in range (random.randint(3,6)):
                        Mediator.PARTICLES.append(Particle(self.pos.copy(),self.vel.copy(),'test'))
                self.remove()
            
            if collision == 'fast_enemy' and not self.bullet_type == 'fast_enemy_bullet':
                if len(Mediator.PARTICLES) < 25:
                    for i in range(random.randint(3, 5)):
                        Mediator.PARTICLES.append(Particle(self.pos.copy(),self.vel.copy(),'test'))
                    
                self.remove()


            if collision == 'player' and not self.bullet_type == 'player_bullet':
                if len(Mediator.PARTICLES) < 25:
                    for i in range (random.randint(3,5)):
                        Mediator.PARTICLES.append(Particle(self.pos.copy(),self.vel.copy(),'test'))

                self.remove()
            
        self.collision_ids.clear()

    def update_image(self):
        if self.bullet_type == 'bomb_bullet_orange':

            self.img = pygame.image.load("Graphics/Bullet_Orange.png")
            self.rect = pygame.Rect(-99999,-99999,self.img.get_width(),self.img.get_height())
        
        elif self.bullet_type == 'enemy_bullet':
            self.img = pygame.image.load("Graphics/Enemy_Bullet_Brown.png")
            self.vel[0] = (self.vel[0]/6)*3 
            self.vel[1] = (self.vel[1]/6)*3
            self.rect = pygame.Rect(-99999,-99999,self.img.get_width(),self.img.get_height())
            self.show_frames = 8

        elif self.bullet_type == "fast_enemy_bullet":
            self.img = pygame.image.load("Graphics/Fast_Enemy_Bullet.png")
            self.vel[0] = (self.vel[0]/6)*2
            self.vel[1] = (self.vel[1]/6)*2
            self.rect = pygame.Rect(-99999,-99999,self.img.get_width(),self.img.get_height())
            self.show_frames = 6
            self.apply_wind_speed = True







        elif self.bullet_type == 'missile_bullet_red':

            self.img = pygame.image.load("Graphics/Bullet_Yellow.png")

            self.vel[0] = (self.vel[0]/6)*4
            self.vel[1] = (self.vel[1]/6)*4
            self.timer += 35
            self.rect = pygame.Rect(-99999,-99999,self.img.get_width(),self.img.get_height())
        





