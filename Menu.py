import pygame

from Display import *

class Menu:

    MENU_ON = True

    def __init__(self):
        self.font = pygame.font.Font("Font/EndlessBossBattleRegular-v7Ey.ttf", 32)
        self.font_big = pygame.font.Font("Font/EndlessBossBattleRegular-v7Ey.ttf", 64)
        self.selected = 0
        self.img_title = self.font_big.render('The Square', True, (255,255,255))
        self.img_play = self.font.render('Play', True, (0,200,0))

    def draw_menu(self):
        Display.SCREEN.fill((0, 0, 0))

        Display.SCREEN.blit(self.img_title, (Display.WINDOW_SIZE[0]*0.2,Display.WINDOW_SIZE[1]*0.1))

        Display.SCREEN.blit(self.img_play, (Display.WINDOW_SIZE[0]*0.2,Display.WINDOW_SIZE[1]*0.3))



    def menu_input(self):
        keypressed = pygame.key.get_pressed()

        if keypressed[pygame.K_UP]:
            self.selected -= 1
        
        if keypressed[pygame.K_DOWN]:
            self.selected += 1

        if keypressed[pygame.K_RETURN]:
            Menu.MENU_ON = False

    def loop_menu(self):
        self.draw_menu()
        self.menu_input()

