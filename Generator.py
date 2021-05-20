import pygame,sys, random

from Display import *
from Mediator import *
from Enemy import *
from FastEnemy import *


class Generator:

    WAVE = 1

    def __init__(self):
        self.timer = 0

        self.wait_for_spawn = random.randint(300,600)
        self.player = self.find_player()


    
    def loop(self):
        self.timer += 1


        if self.timer > self.wait_for_spawn:
            self.timer = 0
            self.wait_for_spawn = random.randint(300,600)
            self.spawn('enemy')


    def spawn(self, type_enemy):
        pos = self.player.pos.copy()
        pos[0] += random.randint(-Display.WINDOW_SIZE[0], Display.WINDOW_SIZE[0])
        pos[1] += random.randint(-Display.WINDOW_SIZE[1], Display.WINDOW_SIZE[1])

        if type_enemy == 'enemy':
            Mediator.ALL_GAMEOBJECTS.append(Enemy(pos))
        elif type_enemy == 'fast_enemy':
            Mediator.ALL_GAMEOBJECTS.append(FastEnemy(pos))

    




    def find_player(self):

        for object in Mediator.ALL_GAMEOBJECTS:
            if object.get_id() == 'player':
                return object







