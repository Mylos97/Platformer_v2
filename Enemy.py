import pygame, math
from GameObject import *
from Display import *
from Player import *
from Bullet import *

class Enemy(GameObject):

    def __init__(self, pos):
        super().__init__(pos)
        self.size = [32,32]
        self.top_speed = 2
        self.id = 'enemy'
        self.img = pygame.image.load("Graphics/Enemy_big.png")
        self.img_copy = self.img.copy()
        self.target = self.find_player()


        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.img.get_width(),self.img.get_height())

        self.trail_images = 3
        self.trail_limit = 5
        self.hitpoints = 100
        self.start_hitpoints = 100

        self.timer = 0
        self.shoot_coldown = 60



    
    def loop(self, DT):
        self.vel[0] = self.accel[0]
        self.vel[1] = self.accel[1]

        self.pos[0] += 17*self.vel[0]/DT
        self.pos[1] += 17*self.vel[1]/DT
        
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

        self.follow_object_enemy(self.target)


        self.cap_acceleration()

        if self.distance < 50:
            self.vel[0] = 0
            self.vel[1] = 0
            self.accel[0] = 0
            self.accel[1] = 0

        if self.timer > self.shoot_coldown:
            self.timer = 0
            new_pos = [self.pos[0] + self.img.get_width()/4, self.pos[1] + self.img.get_height()/4]
            dir = self.shoot_towards_object(self.target)
            bullets = [[1,0],[0.1, - 0.5]]
            #[dir[0]*math.cos(320) - dir[1]*math.sin(320), dir[0] * math.sin(320) + dir[1] * math.cos(320)]
            Mediator.ALL_GAMEOBJECTS.append(Bullet(new_pos,bullets[0],"enemy_bullet"))
            
            Mediator.ALL_GAMEOBJECTS.append(Bullet(new_pos,bullets[1],"enemy_bullet"))



        if self.trail_counter > self.trail_limit:
            self.trail_counter = 0 
            self.append_trail(self.img_copy, self.rect.copy())

        self.trail_counter += 1
        self.hit_timer += 1
        self.timer += 1 



        self.check_border()

        if self.hitpoints <= 0:
            self.remove()

    def draw(self,camera):
        self.draw_trail(camera)
        self.draw_healtbar(camera)
        Display.SCREEN.blit(self.img, (camera.apply_offset(self.rect)))

    def collision(self):
        i = 0
        for collision in self.collision_ids:
            if collision == 'player_bullet':
                self.hit_timer = 0
                self.hitpoints -= 1
                self.accel[0] += self.collision_vels[i][0]
                self.accel[1] += self.collision_vels[i][1]

            
            if collision == 'missile':
                self.hit_timer = 0
                self.accel[0] += self.collision_vels[i][0]
                self.accel[1] += self.collision_vels[i][1]
            
            i += 1
            
        self.collision_vels.clear()
        self.collision_ids.clear()
