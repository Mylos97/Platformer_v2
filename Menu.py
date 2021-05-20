import pygame,sys

from Display import *

class Menu:

    MENU_ON = True

    def __init__(self):
        self.font = pygame.font.Font("Font/EndlessBossBattleRegular-v7Ey.ttf", 32)
        self.font_big = pygame.font.Font("Font/EndlessBossBattleRegular-v7Ey.ttf", 64)
        self.selected = 0
        self.img_title = self.font_big.render('The Square', True, (255,255,255))
        self.img_play_select = self.font.render('Play', True, (0,200,0))
        self.img_options_select = self.font.render('Options', True, (150,150,150))
        self.img_quit_select = self.font.render('Quit', True, (200,0,0))

        self.img_play_not = self.font.render('Play', True, (0,130,0))
        self.img_options_not = self.font.render('Options', True, (110,110,110))
        self.img_quit_not = self.font.render('Quit', True, (130,0,0))

        self.wait_for_key = 10

    def draw_menu(self):
        Display.SCREEN.fill((0, 0, 0))

        Display.SCREEN.blit(self.img_title, (Display.WINDOW_SIZE[0]*0.2,Display.WINDOW_SIZE[1]*0.1))

        if self.selected == 0:
            Display.SCREEN.blit(self.img_play_select, (Display.WINDOW_SIZE[0]*0.2,Display.WINDOW_SIZE[1]*0.4))
        else:
            Display.SCREEN.blit(self.img_play_not, (Display.WINDOW_SIZE[0]*0.2,Display.WINDOW_SIZE[1]*0.4))
        
        if self.selected == 1:
            Display.SCREEN.blit(self.img_options_select, (Display.WINDOW_SIZE[0]*0.2,Display.WINDOW_SIZE[1]*0.5))
        else:
            Display.SCREEN.blit(self.img_options_not, (Display.WINDOW_SIZE[0]*0.2,Display.WINDOW_SIZE[1]*0.5))

        if self.selected == 2:
            Display.SCREEN.blit(self.img_quit_select, (Display.WINDOW_SIZE[0]*0.2,Display.WINDOW_SIZE[1]*0.6) )
        else:
            Display.SCREEN.blit(self.img_quit_not, (Display.WINDOW_SIZE[0]*0.2,Display.WINDOW_SIZE[1]*0.6) )

    def menu_input(self):
        self.wait_for_key += 1

        keypressed = pygame.key.get_pressed()

        if keypressed[pygame.K_UP] and self.wait_for_key > 8:
            self.wait_for_key = 0
            self.selected -= 1
        
        if keypressed[pygame.K_DOWN] and self.wait_for_key > 8:
            self.wait_for_key = 0
            self.selected += 1


        ## Start game ##
        if self.selected == 0:
            if keypressed[pygame.K_RETURN] and self.wait_for_key > 8:
                Menu.MENU_ON = False
        
        ## Quit Game ##
        if self.selected == 2:
            if keypressed[pygame.K_RETURN] and self.wait_for_key > 8:
                sys.exit()

        if keypressed[pygame.K_ESCAPE]:
            sys.exit()

        if self.selected > 2:
            self.selected = 0
        
        if self.selected < 0: 
            self.selected = 2

    def loop_menu(self):
        self.draw_menu()
        self.menu_input()

