from HUD import HUD
from pygame.constants import *
import pygame
import sys
from Mediator import *
from Player import *
from Display import *
from Enemy import *
from FastEnemy import *
from Camera import *
from Menu import *


class Main:


    def fog():
        surf = pygame.Surface((Display.WINDOW_SIZE[0],100))
        pygame.draw.rect(surf, (0,0,0), pygame.Rect(0,0,Display.WINDOW_SIZE[0],100))
        surf.set_colorkey((0,0,0))
        Display.SCREEN.blit(surf,pygame.Rect(0,0,Display.WINDOW_SIZE[0],100) , special_flags = BLEND_RGB_SUB)

#        surf = pygame.Surface((radius+1, radius+1))
#        pygame.draw.rect(surf, color, pygame.Rect(0,0,radius,radius))

#        surf.set_colorkey((0,0,0))
#        Display.SCREEN.blit(, dest)

    def main():
        RUNNING = True
        pygame.init()

        CLOCK = pygame.time.Clock()
        FPS = 60
        DT = 0
        FPS_COUNTER = 0
        player = Player([100, 100])
        camera = Camera(1024*16, 768*16)
        Mediator.ALL_GAMEOBJECTS.append(player)
        enemy = Enemy([200, 400])
        enemy2 = FastEnemy([600,400])
        Mediator.ALL_GAMEOBJECTS.append(enemy)  
        Mediator.ALL_GAMEOBJECTS.append(enemy2)  

        hud = HUD(player)
        menu = Menu()


        while RUNNING:


            if Menu.MENU_ON:
                menu.loop_menu()

            else:
                if Player.PLAYER_DEAD == True:
                    Player.PLAYER_HEALTH = 100
                    RUNNING = Menu.MENU_ON = True



                Display.SCREEN.fill((0, 0, 0))


                camera.update_offset(player.get_rect())


                DT = CLOCK.tick(FPS)

                for object in Mediator.ALL_GAMEOBJECTS:
                    object.loop(DT)
                    object.draw(camera)



                Mediator.collisions(Mediator)
                for object in Mediator.COLLISIONS:
                    object.collision()

                i = 0
                for particle in Mediator.PARTICLES:
                    particle.loop(DT)
                    particle.draw(camera)
                    if particle.alive == False:
                        Mediator.PARTICLES.pop(i)
                    i += 1

                
                Mediator.COLLISIONS.clear()
                
                Mediator.ALL_GAMEOBJECTS = [object for object in Mediator.ALL_GAMEOBJECTS if object not in Mediator.TO_BE_REMOVED]

                Mediator.TO_BE_REMOVED.clear()

                hud.update_HUD()
                hud.draw()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    
    if __name__ == "__main__":
        main()

    