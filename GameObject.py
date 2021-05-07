import pygame, math

from Display import *
from Mediator import *

class GameObject:

    def __init__(self, pos):
        self.screen = Display.SCREEN
        self.pos = pos
        self.vel = [0,0]
        self.accel = [0,0]
        self.top_speed = 3

        self.rect = pygame.Rect(0,0,0,0)
        self.id = None


        self.collision_id = 'none'
        self.collision_vel = []
        
        self.trail_img = []
        self.trail_rect = []
        self.trail_counter = 0
        self.trail_limit = 5
        self.trail_images = 7
        self.hit_timer = 0
        self.target = self.find_player()

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





    ## Only for checking collions on walls
    def check_collision_walls(self, rect, movement):
        collision_types = {'top': False, 'bottom': False , 'right': False, 'left': False}

        ## Check for x direction ##
        rect.x += movement[0]
        hit_list = self.collision_walls(rect)

        for wall in hit_list:
            if movement[0] > 0:
                rect.right = wall.left
                collision_types['right'] = True
            if movement[0] < 0:
                rect.left = wall.right
                collision_types['left'] = True
        
        ## Check for y direction ##
        rect.y += movement[1]
        hit_list = self.collision_walls(rect)
        
        for wall in hit_list:
            if movement[1] > 0:
                rect.bottom = wall.top
                collision_types['bottom'] = True
            if movement[1] < 0:
                rect.top = wall.bottom
                collision_types['top'] = True
        
        return rect, collision_types


    ## Returns a list of rects that collide with the object
    def collision_walls(self, rect):
        hit_list = []

        for wall in Mediator.CURRENT_WALLS:
            if rect.colliderect(wall.get_rect()):
                hit_list.append(wall.get_rect())
        
        return hit_list
    
    def find_target(self):
        for object in Mediator.ALL_GAMEOBJECTS:
            if object.get_id() == 'enemy':
                return object

    def find_player(self):
        for object in Mediator.ALL_GAMEOBJECTS:
            print(len(Mediator.ALL_GAMEOBJECTS))
            if object.get_id() == 'player':
                print("i use")
                return object

    def follow_object(self, object):
        self.x_d = self.rect.centerx - object.rect.centerx
        self.y_d = self.rect.centery - object.rect.centery

        self.distance = math.sqrt(math.pow(self.x_d, 2) + math.pow(self.y_d, 2))
        self.x_n = (self.x_d/self.distance)
        self.y_n = (self.y_d/self.distance)

        self.accel[0] -= self.x_n
        self.accel[1] -= self.y_n
        
