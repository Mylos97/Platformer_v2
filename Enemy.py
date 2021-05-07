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
        self.img_copy = self.img.copy()
        self.target = self.find_player()
        print(self.target.get_id())
        self.trail_images = 3
        self.trail_limit = 5

    
    def loop(self, DT):
        self.vel[0] = self.accel[0]
        self.vel[1] = self.accel[1]

        self.pos[0] += 17*self.vel[0]/DT
        self.pos[1] += 17*self.vel[1]/DT
        
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

        self.follow_object(self.target)


        self.cap_acceleration()

        if self.distance < 50:
            self.vel[0] = 0
            self.vel[1] = 0
            self.accel[0] = 0
            self.accel[1] = 0

        if self.trail_counter > self.trail_limit:
            self.trail_counter = 0 
            self.append_trail(self.img_copy, self.rect.copy())

        self.trail_counter += 1
        self.hit_timer += 1
        
        self.check_border()

    def draw(self,camera):
        self.draw_trail(camera)
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
