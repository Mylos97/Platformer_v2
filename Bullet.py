import pygame, math
from GameObject import *
from Display import *

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

        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        self.id = 'player_bullet'
        self.img = pygame.image.load("Graphics/Bullet.png")
        self.wait_frames = 0

        self.update_image()

 
    def loop(self, DT):
        self.img.set_alpha(int(255 - math.pow(self.timer,1.2)))

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        
        self.wait_frames += 1
        self.timer += 1

        if self.img.get_alpha() == 0:
            self.remove()

    def draw(self, camera):
        if self.wait_frames > 2:
            Display.SCREEN.blit(self.img,camera.apply_offset(self.rect))

    def collision(self):
        print(self.collision_id)

        if self.collision_id == 'enemy':
            self.remove()
        
        self.collision_id = 'none'

    def update_image(self):
        if self.bullet_type == 'bomb_bullet_orange':
            self.img = pygame.image.load("Graphics/Bullet_Orange.png")


