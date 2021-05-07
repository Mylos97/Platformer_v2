import pygame
import sys
from Mediator import *
from Player import *
from Display import *
from Enemy import *
from Maze import *
from Camera import *

class Main:

    def main():
        RUNNING = True
        pygame.init()

        CLOCK = pygame.time.Clock()
        FPS = 60
        DT = 0
        FPS_COUNTER = 0
        player = Player([100, 100])
        camera = Camera(1024*16, 768*16)
        cell = Cell(20, 0)
        maze = Maze()
        Mediator.ALL_GAMEOBJECTS.append(player)
        enemy = Enemy([200, 400])
        Mediator.ALL_GAMEOBJECTS.append(enemy)
        Mediator.ALL_WALLS.append(cell)

        while RUNNING:
            Display.SCREEN.fill((200, 200, 200))
            camera.update_offset(player.get_rect())
            pygame.draw.rect(Display.SCREEN, (238,238,238), camera.apply_offset(Display.PLATFORM_RECT))
            DT = CLOCK.tick(FPS)

            for object in Mediator.ALL_GAMEOBJECTS:
                object.loop(DT)
                object.draw(camera)

            Mediator.collisions(Mediator)

            for object in Mediator.COLLISIONS:
                object.collision()


            Mediator.COLLISIONS.clear()
            Mediator.ALL_GAMEOBJECTS = [object for object in Mediator.ALL_GAMEOBJECTS if object not in Mediator.TO_BE_REMOVED]
            Mediator.TO_BE_REMOVED.clear()


            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            
    
    if __name__ == "__main__":
        main()

