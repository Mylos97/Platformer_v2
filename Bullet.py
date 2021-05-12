import pygame, math
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

        self.id = 'player_bullet'
        self.img = pygame.image.load("Graphics/Bullet.png")
        self.wait_frames = 0
        self.rect = pygame.Rect(-99999,-99999,self.img.get_width(),self.img.get_height())

        self.rotate_int = 0
        self.update_image()

 
    def loop(self, DT):
        self.img.set_alpha(int(255 - math.pow(self.timer,1.2)))

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.wait_frames > 2:
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]
        
        self.wait_frames += 1
        self.timer += 1

        if self.img.get_alpha() == 0:
            self.remove()

        if self.bullet_type == 'missile_bullet_red':
            self.vel[0] *= 0.98
            self.vel[1] *= 0.98
        

    def draw(self, camera):
        if self.wait_frames > 2:
                Display.SCREEN.blit(self.img,camera.apply_offset(self.rect))



    def collision(self):
        if self.collision_id == 'enemy':
            for i in range (random.randint(3,7)):
                Mediator.ALL_GAMEOBJECTS.append(Particle(self.pos.copy(),self.vel.copy(),'test'))
            self.remove()
        
        self.collision_id = 'none'

    def update_image(self):
        if self.bullet_type == 'bomb_bullet_orange':

            self.img = pygame.image.load("Graphics/Bullet_Orange.png")
            self.rect = pygame.Rect(-99999,-99999,self.img.get_width(),self.img.get_height())

        elif self.bullet_type == 'missile_bullet_red':

            self.img = pygame.image.load("Graphics/Bullet_Yellow.png")

            self.vel[0] = (self.vel[0]/6)*4
            self.vel[1] = (self.vel[1]/6)*4
            self.timer += 35
            self.rect = pygame.Rect(-99999,-99999,self.img.get_width(),self.img.get_height())




