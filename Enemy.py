import pygame, math
from GameObject import *
from Display import *
from Player import *
from Main import *

class Enemy(GameObject):

    def __init__(self, pos):
        super().__init__(pos)
        self.size = [32,32]
        self.top_speed = 2
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        self.id = 'enemy'
        self.img = pygame.image.load("Graphics/Enemy.png")
    
    def loop(self, DT):
        self.vel[0] = self.accel[0]
        self.vel[1] = self.accel[1]

        self.pos[0] += 17*self.vel[0]/DT
        self.pos[1] += 17*self.vel[1]/DT
        
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])

        self.x_d = self.rect.centerx - Player.PLAYER_RECT.centerx
        self.y_d = self.rect.centery - Player.PLAYER_RECT.centery

        self.distance = math.sqrt(math.pow(self.x_d, 2) + math.pow(self.y_d, 2))
        self.x_n = (self.x_d/self.distance)
        self.y_n = (self.y_d/self.distance)

        self.accel[0] -= self.x_n
        self.accel[1] -= self.y_n

        if self.accel[0] >= self.top_speed:
            self.accel[0] = self.top_speed
        
        if self.accel[0] <= -self.top_speed:
            self.accel[0] = -self.top_speed

        if self.accel[1] >= self.top_speed:
            self.accel[1] = self.top_speed
        
        if self.accel[1] <= -self.top_speed:
            self.accel[1] = -self.top_speed

        if self.distance < 50:
            self.vel[0] = 0
            self.vel[1] = 0
            self.accel[0] = 0
            self.accel[1] = 0

        self.hit_timer += 1

    def draw(self,camera):
        Display.SCREEN.blit(self.img, (camera.apply_offset(self.rect)))

    def collision(self):
        if self.collision_id == 'player_bullet' and self.hit_timer > 3:
            self.hit_timer = 0
            print(Player.FPS_COUNTER)
            print(self.collision_vel)
            self.accel[0] += self.collision_vel[0]*2
            self.accel[1] += self.collision_vel[1]*2
            self.collision_vel.clear()
        
        
        self.collision_id = 'none'
