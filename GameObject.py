from Display import *
from Mediator import *

class GameObject:

    def __init__(self, pos):
        self.screen = Display.SCREEN
        self.pos = pos
        self.vel = [0,0]
        self.accel = [0,0]
        self.rect = None
        self.id = None


        self.collision_id = 'none'
        self.collision_vel = []
        
        self.trail_img = []
        self.trail_rect = []
        self.trail_counter = 0
        self.trail_limit = 5

        self.hit_timer = 0

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
        if len(self.trail_img) > 7:
            self.trail_img.pop(7)
            self.trail_rect.pop(7)
    
    def draw_trail(self, camera):
        alpha = 160
        i = 0

        for img in self.trail_img:
            img.set_alpha(alpha)
            Display.SCREEN.blit(img, camera.apply_offset(self.trail_rect[i]))
            i += 1
            alpha -= 30
            



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
