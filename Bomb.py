import pygame, math
from GameObject import *
from Display import *
from Mediator import *
from Bullet import *

class Bomb(GameObject):

    def __init__(self, pos):
        super().__init__(pos)
        self.img = pygame.image.load("Graphics/Bomb.png")
        self.rect = pygame.Rect(pos[0], pos[1], self.img.get_width(), self.img.get_height())
        self.id = 'bomb'
        self.vel = [0,0]

        self.life_time = 0
        self.alpha_remove = 255


    def loop(self, DT):
        self.life_time += 1

        self.img.set_alpha(255-int(self.life_time**1.12))

        if self.img.get_alpha() == 0:
            self.bomb_explode()
            self.remove()

    def draw(self, camera):
        Display.SCREEN.blit(self.img, camera.apply_offset(self.rect))

    def bomb_explode(self):

        bomb_angles = [[0,1], [math.sqrt(2)/2,math.sqrt(2)/2], [1,0] , [math.sqrt(2)/2,-math.sqrt(2)/2] ,[0,-1], [-math.sqrt(2)/2,-math.sqrt(2)/2] ,[-1,0], [-math.sqrt(2)/2,math.sqrt(2)/2]]        
        for i in range(len(bomb_angles)):
            Mediator.ALL_GAMEOBJECTS.append(Bullet(self.pos.copy(),bomb_angles[i].copy(),"bomb_bullet_orange"))
    
    def collision(self):
        if self.collision_id == 'enemy':
            self.bomb_explode()
            self.remove()

        self.collision_id = 'none'



