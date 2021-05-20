import pygame, math

from GameObject import *
from Display import *
from Mediator import *
from Bullet import *

class Missile(GameObject):

    def __init__(self, pos, dir ):
        super().__init__(pos)
        self.pos[0] += 8
        self.pos[1] += 8
        self.vel = [dir[0]*3,dir[1]*3]
        self.accel = [dir[0]*3,dir[1]*3]
        self.id = 'missile'

        self.life_time = 0
        self.img = pygame.image.load("Graphics\Missile.png")

        angle = math.degrees(math.atan2(-dir[1], dir[0])) + 90 
        self.roti_img = pygame.transform.rotate(self.img, angle)

        self.rect = pygame.Rect(-99999, -999999, self.img.get_width(), self.img.get_height())
        
        self.target = self.find_target()
        
        self.wind_speed = 1
        self.life_time = 0
        self.show_frames = 0
        self.update_speed = 0

    
    def loop(self, DT):
        self.img.set_alpha(255- math.pow(self.life_time,1.08))

        self.vel[0] = self.accel[0]*self.wind_speed
        self.vel[1] = self.accel[1]*self.wind_speed

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.show_frames > 5:
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]


        self.cap_acceleration()

        ## wait some time before finding enemy
        if self.life_time > 30 and self.update_speed > 10:
            self.update_speed = 0
            if not self.target == 'none':
                self.follow_object(self.target)

                angle = math.degrees(math.atan2(self.target.rect.y - self.rect.y, self.target.rect.x - self.rect.x))
                
                ## Make top 0 and get rid of -
                angle = abs(angle - 90) 

                self.roti_img = pygame.transform.rotate(self.img, angle)


        ## update rect so the image does not move 
        self.rect = self.roti_img.get_rect(center=(self.pos))

        self.update_speed += 1
        self.life_time += 1
        self.show_frames += 1


        if random.randint(0, 3) == 5:
            self.wind_speed -= 0.02
        
        if self.img.get_alpha() == 0:
            self.explode()
            self.remove()

    def draw(self, camera):
        if self.show_frames > 5: 
            Display.SCREEN.blit(self.roti_img, camera.apply_offset(self.rect))


    def collision(self):
        for collision in self.collision_ids:

            if collision == 'enemy' or collision == 'fast_enemy':
                self.explode()
                self.remove()

        self.collision_id = 'none'

    def explode(self):
        angles = [[0,1],[1,0],[0,-1],[-1,0]]
        for angle in angles:
            Mediator.ALL_GAMEOBJECTS.append(Bullet(self.pos.copy(), angle, "missile_bullet_red"))
