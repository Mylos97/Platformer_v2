import pygame
from Cell import *
from Display import *
from Player import *
from Mediator import *

class Maze:

    ROOM_SIZE = 24
    MAZE_LENGTH = 2
    SQUARE_SIZE = 48

    def __init__(self):
        self.cells = []
        self.file = open("map2.txt",'w')
        self.create_txt_file(self.file)


        #self.maze = self.load_map("map2.txt")
        #self.create_maze_algorithm()
        self.create_square_map()
        #self.generate_maze()

    def generate_maze(self):
        x , y = 0,0

        for row in self.maze:
            
            for value in row:
                if value == 'a' or value == '8':
                    temp_cell = Cell(x, y)
                    Mediator.ALL_WALLS.append(temp_cell)

                x += 1

            y += 1
            x = 0

    def load_map(self, path):
        f = open(path,'r')
        data = f.read()
        data = data.split('\n')
        game_map = []

        for row in data:
            game_map.append(list(row))
        
        return game_map
    
    def create_map(self):
        pass

    
    def create_wall_top_and_bottom(self, file):
        for i in range(24):
            file.write("8")

        file.write("\n")
    
    def create_wall_left_and_right(self, file):
        file.write("a")

        for i in range(22):
            file.write(" ")

        file.write("a")
        file.write("\n")

    def create_txt_file(self, file):
        for i in range(3):
            self.create_room(file)
        
    
    def create_room(self, file):
        self.create_wall_top_and_bottom(file)

        for i in range(14):
            self.create_wall_left_and_right(file)

        #self.create_wall_top_and_bottom(file)


    def create_square_map(self):

        for i in range(Maze.SQUARE_SIZE + 1):
            for j in range(Maze.SQUARE_SIZE + 1):
                if i == 0 or i == Maze.SQUARE_SIZE:
                    Mediator.ALL_WALLS.append(Cell(i,j))
                elif j == 0 or j == Maze.SQUARE_SIZE:
                    Mediator.ALL_WALLS.append(Cell(i,j))





    def create_maze_algorithm(self):
        
        for i in range(Maze.ROOM_SIZE * Maze.MAZE_LENGTH + 1):
            for j in range(Maze.ROOM_SIZE * Maze.MAZE_LENGTH + 1):

                if i % Maze.ROOM_SIZE == 0:
                    Mediator.ALL_WALLS.append(Cell(i,j))
                elif j % Maze.ROOM_SIZE == 0:
                    Mediator.ALL_WALLS.append(Cell(i,j))



        for cell in Mediator.ALL_WALLS:

            if not cell.x == 0 and not cell.x == Maze.ROOM_SIZE* Maze.MAZE_LENGTH:
                if not cell.y == 0 and not cell.y == Maze.ROOM_SIZE * Maze.MAZE_LENGTH:
                    print(cell.x,end= " ")
                    print(cell.y)

                    if cell.x % Maze.ROOM_SIZE == (Maze.ROOM_SIZE/2)-1:
                        Mediator.ALL_WALLS.remove(cell)
                    elif cell.x % Maze.ROOM_SIZE == Maze.ROOM_SIZE/2:
                        Mediator.ALL_WALLS.remove(cell)
                    elif cell.x % Maze.ROOM_SIZE == (Maze.ROOM_SIZE/2)+1:
                        Mediator.ALL_WALLS.remove(cell)                    
                    
                    
                    if cell.y % Maze.ROOM_SIZE == (Maze.ROOM_SIZE/2)-1:
                         Mediator.ALL_WALLS.remove(cell)                    
                    elif cell.y % Maze.ROOM_SIZE == Maze.ROOM_SIZE/2:
                         Mediator.ALL_WALLS.remove(cell)
                    elif cell.y % Maze.ROOM_SIZE == (Maze.ROOM_SIZE/2)+1:
                         Mediator.ALL_WALLS.remove(cell)                         

        
            




    
