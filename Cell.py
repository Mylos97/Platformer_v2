import pygame
from GameObject import *
from GameObject import *

class Cell(GameObject):
    
    CELL_SIZE = 64
    CELL_IMAGE = pygame.image.load("Graphics/Wall.png")

    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        self.neighbors = []
        self.rect = pygame.Rect(self.x * Cell.CELL_SIZE,self.y * Cell.CELL_SIZE,Cell.CELL_SIZE,Cell.CELL_SIZE)
        self.id = 'wall'

    def add_neighbor(self, cell):
        self.neighbors.append(cell)

    def get_neighbors(self):
        return self.neighbors
    
    def get_rect(self):
        return self.rect
    
    def draw(self, camera):
        Display.SCREEN.blit(Cell.CELL_IMAGE, camera.apply_offset(self.rect))
    