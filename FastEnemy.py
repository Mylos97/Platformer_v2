import pygame
from Enemy import *
from GameObject import *
from Display import *
from Mediator import *

class FastEnemy(Enemy):


    def __init__(self, pos):
        super().__init__(pos)
        self.img = pygame.image.load("Graphics\Enemy_Fast.png")
        self.target = self.find_player()

        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.img.get_width(),self.img.get_height())
        self.id = 'fast_enemy'
        self.trail_images = 5
        self.trail_limit = 8
        self.hitpoints = 50
        self.start_hitpoints = 50

        self.timer = 0
        self.shoot_coldown = 10
        self.top_speed = 3


    def loop(self, DT):
        self.vel[0] = self.accel[0]
        self.vel[1] = self.accel[1]

        self.pos[0] += 17*self.vel[0]/DT
        self.pos[1] += 17*self.vel[1]/DT
        
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

        self.follow_object_enemy(self.target)

        self.cap_acceleration()


        if self.distance < 10:
            self.vel[0] = 0
            self.vel[1] = 0
            self.accel[0] = 0
            self.accel[1] = 0

        if self.timer > self.shoot_coldown:
            self.timer = 0
            bullets = [[0,1],[1,0],[-1,0],[0,-1]]
            for b in bullets:
                Mediator.ALL_GAMEOBJECTS.append(Bullet(self.pos.copy(), b, "fast_enemy_bullet"))
        
        self.timer += 1

        if self.hitpoints <= 0:
            self.remove()
    


    def draw(self, camera):
        self.draw_healtbar(camera)
        Display.SCREEN.blit(self.img, camera.apply_offset(self.rect))


    def collision(self):
        i = 0
        for collision in self.collision_ids:
            if collision == 'player_bullet':
                self.hitpoints -= 1
                self.accel[0] += self.collision_vels[i][0]*0.25
                self.accel[1] += self.collision_vels[i][1]*0.25

            if collision == 'missile':
                self.hitpoints -= 1
                self.accel[0] += self.collision_vels[i][0]*0.4
                self.accel[1] += self.collision_vels[i][1]*0.4

            i += 1
        
        self.collision_ids.clear()
        self.collision_vels.clear()

