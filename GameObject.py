import pygame, math

from pygame import transform

from Display import *
from Mediator import *



class GameObject:

    def __init__(self, pos):
        self.pos = pos
        self.vel = [0,0]
        self.accel = [0,0]
        self.wind_speed = 1
        self.apply_wind_speed = False
        self.top_speed = 3

        self.rect = pygame.Rect(0,0,0,0)
        self.id = None

        self.collision_ids = []
        self.collision_vels = []
        
        self.trail_img = []
        self.trail_rect = []
        self.trail_counter = 0
        self.trail_limit = 5
        self.trail_images = 7
        
        self.wind_speed = 1
        
        self.hit_timer = 0
        self.hitpoints = 1
        self.start_hitpoints = 1

        self.healt_bar = pygame.Rect(self.pos[0], self.pos[1], 20, 2)
        self.healt_bar_img = pygame.Surface((self.healt_bar.w,self.healt_bar.h))

    def loop(self, DT = None):
        pass
    
    def loop_x(self):
        pass
    
    def loop_y(self):
        pass

    def draw(self, camera):
        pass
    
    def get_rect(self):
        return self.rect 

    def collision(self):
        pass
    
    def remove(self):
        Mediator.TO_BE_REMOVED.append(self)

    def get_id(self):
        return self.id
    
    def append_trail(self, img, rect):
        self.trail_img.insert(0, img)
        self.trail_rect.insert(0, rect)
        if len(self.trail_img) > self.trail_images:
            self.trail_img.pop(self.trail_images)
            self.trail_rect.pop(self.trail_images)
    
    def draw_trail(self, camera):
        alpha = 140
        i = 0

        for img in self.trail_img:
            img.set_alpha(alpha)
            Display.SCREEN.blit(img, camera.apply_offset(self.trail_rect[i]))
            i += 1
            alpha -= (140/self.trail_images)
            
    def check_border(self):
        if self.pos[0] > Display.GAME_SIZE[0]:
            self.pos[0] = Display.GAME_SIZE[0]
        
        if self.pos[0] < 0:
            self.pos[0] = 0
        
        if self.pos[1] > Display.GAME_SIZE[1]:
            self.pos[1] = Display.GAME_SIZE[1]
    
        if self.pos[1] < 0:
            self.pos[1] = 0

    def cap_acceleration(self):
        if self.accel[0] >= self.top_speed:
            self.accel[0] = self.top_speed
        
        if self.accel[0] <= -self.top_speed:
            self.accel[0] = -self.top_speed

        if self.accel[1] >= self.top_speed:
            self.accel[1] = self.top_speed
        
        if self.accel[1] <= -self.top_speed:
            self.accel[1] = -self.top_speed
    
    def find_target(self):
        target = 'none'
        temp_distance = 1000000
        distance = 1000000
        
        for object in Mediator.ALL_GAMEOBJECTS:

            if object.get_id() == 'enemy' or object.get_id() == 'fast_enemy':
                temp_distance = math.sqrt(math.pow(self.pos[0] - object.pos[0], 2) + math.pow(self.pos[1] - object.pos[1], 2))

                if temp_distance < distance:
                    distance = temp_distance 
                    target = object
        
        return target

    def find_player(self):
        for object in Mediator.ALL_GAMEOBJECTS:
            if object.get_id() == 'player':
                return object

    def follow_object(self, object):
        self.x_d = self.rect.centerx - object.rect.centerx
        self.y_d = self.rect.centery - object.rect.centery

        self.distance = math.sqrt(math.pow(self.x_d, 2) + math.pow(self.y_d, 2))
        self.x_n = (self.x_d/self.distance)
        self.y_n = (self.y_d/self.distance)

        self.accel[0] -= self.x_n
        self.accel[1] -= self.y_n
    
    def shoot_towards_object(self, object):
        x_d = self.rect.centerx - object.rect.centerx
        y_d = self.rect.centery - object.rect.centery

        distance = math.sqrt(x_d**2 + y_d**2)

        x_n = x_d/distance
        y_n = y_d/distance

        return [-x_n,-y_n]

    def shoot_transform_angle(self, dir, angle):
        
        transformed = [-1*(dir[0]*math.cos(angle) - dir[1]*math.sin(angle)), -1*(dir[0] * math.sin(angle) + dir[1] * math.cos(angle))]
        print(transformed)
        return transformed


    def follow_object_enemy(self, object):
        self.x_d = self.rect.centerx - object.rect.centerx
        self.y_d = self.rect.centery - object.rect.centery

        self.distance = math.sqrt(math.pow(self.x_d, 2) + math.pow(self.y_d, 2))
        self.x_n = (self.x_d/self.distance)
        self.y_n = (self.y_d/self.distance)

        self.accel[0] -= self.x_n*0.1
        self.accel[1] -= self.y_n*0.1
    
    def update_healhbar(self):

        if not self.hitpoints <= 0:
            self.healt_bar.w = self.img.get_width()/2*(self.hitpoints/self.start_hitpoints)
            self.healt_bar.x = self.pos[0] + self.img.get_width() / 4
            self.healt_bar.y = self.pos[1] - 8
            self.healt_bar_img = pygame.Surface((self.healt_bar.w, self.healt_bar.h))
            self.healt_bar_img.fill((0,255,0))

        else:
            self.healt_bar.w = 1
            self.healt_bar.x = self.pos[0] + self.img.get_width() / 4
            self.healt_bar.y = self.pos[1] - 8
            self.healt_bar_img = pygame.Surface((self.healt_bar.w, self.healt_bar.h))
            self.healt_bar_img.fill((0,255,0))



    def draw_healtbar(self, camera): 
        self.update_healhbar()
        Display.SCREEN.blit(self.healt_bar_img, camera.apply_offset(self.healt_bar))


    ##For lights ##    
    def rect_surf(self, radius, color):
        surf = pygame.Surface((radius+1, radius+1))
        pygame.draw.rect(surf, color, pygame.Rect(0,0,radius,radius))

        surf.set_colorkey((0,0,0))

        return surf