import pygame, copy, math, sys
from GameObject import *
from Display import *
from Bullet import *
from Mediator import *
from Bomb import *
from Missile import *
from Camera import *

class Player(GameObject):
    
    PLAYER_HEALTH = 100
    PLAYER_DEAD = False
    FPS_COUNTER = 0

    def __init__(self,pos):
        super().__init__(pos)
        self.size = (16,16)
        self.accel_speed = 0.35
        self.top_speed = 9
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        self.id = 'player'
        self.img = pygame.image.load("Graphics/Player.png")
        self.img_copy = self.img.copy()
        
        self.bomb_timer = 0
        self.bullet_timer = 0
        self.missile_timer = 0
        self.missile_cooldown = 30

    def loop(self, DT):
        Player.FPS_COUNTER += 1
        
        self.key_input()
        self.mouse_input()
        
        self.vel[0] = 17*self.vel[0]/DT
        self.vel[1] = 17*self.vel[1]/DT
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]


        self.trail_counter += 1

        if self.trail_counter > self.trail_limit:
            self.trail_counter = 0
            self.append_trail(self.img_copy, pygame.Rect.copy(self.rect))

        self.bullet_timer += 1
        self.bomb_timer += 1
        self.missile_timer += 1

        self.check_border()

        if Player.PLAYER_HEALTH <= 0:
            Player.PLAYER_DEAD = True


    def draw(self, camera):
        self.draw_trail(camera)
        Display.SCREEN.blit(self.img, (camera.apply_offset(self.rect)))


    def key_input(self):
        self.vel = [0,0]
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.accel[0] -= self.accel_speed

            if self.accel[0] <= -self.top_speed:
                self.accel[0] = -self.top_speed

            self.vel[0] = self.accel[0]

        else:
            if self.accel[0] < 0:
                self.accel[0] += self.accel_speed*2

                if self.accel[0] >= 0:
                    self.accel[0] = 0
                self.vel[0] = self.accel[0]

        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.accel[0] += self.accel_speed 

            if self.accel[0] >= self.top_speed:
                self.accel[0] = self.top_speed

            self.vel[0] = self.accel[0]


        else:
            if self.accel[0] > 0:
                self.accel[0] -= self.accel_speed*2

                if self.accel[0] <= 0:
                    self.accel[0] = 0

                self.vel[0] = self.accel[0]


        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.accel[1] -= self.accel_speed 

            if self.accel[1] <= -self.top_speed:
                self.accel[1] = -self.top_speed

            self.vel[1] = self.accel[1]


        else:
            if self.accel[1] < 0:
                self.accel[1] += self.accel_speed*2

                if self.accel[1] >= 0:
                    self.accel[1] = 0
                self.vel[1] = self.accel[1]

        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.accel[1] += self.accel_speed 

            if self.accel[1] >= self.top_speed:
                self.accel[1] = self.top_speed
            
            self.vel[1] = self.accel[1]


        else:
            if self.accel[1] > 0:
                self.accel[1] -= self.accel_speed*2

                if self.accel[1] <= 0:
                    self.accel[1] = 0

                self.vel[1] = self.accel[1]

        if keystate[pygame.K_SPACE] and self.bomb_timer > 10:
            x_y = [self.rect.x,self.rect.y]
            self.bomb_timer = 0
            Mediator.ALL_GAMEOBJECTS.append(Bomb(x_y.copy()))



        if keystate[pygame.K_ESCAPE]:
            sys.exit()
    
    def mouse_input(self):
        if pygame.mouse.get_pressed(num_buttons=3)[0] and 4 < self.bullet_timer:
            self.bullet_timer = 0
            mx, my = pygame.mouse.get_pos()
            dir = (mx - Display.WINDOW_SIZE[0]/2, my - Display.WINDOW_SIZE[1]/2)
            length = math.hypot(*dir)

            if length == 0.0:
                print("lenght 0.0")
                dir = (0,1)
            else:
                dir = (dir[0]/length, dir[1]/length)
            
            angle = math.degrees(math.atan2(-dir[1],dir[0]))
            x_y = [self.rect.x,self.rect.y]
            Mediator.ALL_GAMEOBJECTS.append(Bullet(copy.deepcopy(x_y), dir, "player_bullet"))

        if pygame.mouse.get_pressed(num_buttons=3)[2] and self.missile_cooldown < self.missile_timer:
            self.missile_timer = 0
            mx, my = pygame.mouse.get_pos()
            dir = (mx - Display.WINDOW_SIZE[0]/2, my - Display.WINDOW_SIZE[1]/2)
            length = math.hypot(*dir)

            if length == 0.0:
                print("length 0.0")
                dir = (0,1)
            else:
                dir = (dir[0]/length, dir[1]/length)

            angle = math.degrees(math.atan2(-dir[1], dir[0]))
            x_y = [self.rect.x,self.rect.y]
            Mediator.ALL_GAMEOBJECTS.append(Missile(copy.deepcopy(x_y), dir))
            

            
    def collision(self):
        for collision in self.collision_ids:
            if collision == 'enemy_bullet' or collision == 'fast_enemy_bullet':
                Camera.SCREEN_SHAKE = True
                Player.PLAYER_HEALTH -= 10
        
        self.collision_ids.clear()