"""

"""
import pytest 

from typing import List
import warnings 

def make_board(rows: int, cols: int) -> List[List[str]]:
    
    return [["-" for col in range(cols)] for row in range(rows)]


class Snake:
    
    
    def __init__(self,width: int, height: int, food: List[List[int]]):
        
        self.board = make_board(height, width)
        if food[0] == [0,0]:
            msg = "Cannot start food on top left corner. Snake starts here."
            raise ValueError(msg)
        self.width = width
        self.height = height
        self.food_position = food
        self.snake_position = [0,0]
        self.snake_length = 1
        
    def __repr__(self):
        
        to_return = ""
        
        for row in self.board:
            to_return += f"{row}\n"
        return to_return
        
        
    def move_food(self):
        
        if self.food_position:
            position = self.food_position[0]
            self.food_position.remove(position)
            if self.food_position:
                new_position = self.food_position[0]
                self.board[new_position[0]][new_position[1]] = "F"   
            
            else:
                msg = "No more food to move. Snake WINS!"
                warnings.warn(msg)
        else:
            msg = "No more food to move. Snake WINS!"
            warnings.warn(msg)


    def _draw_snake(self, position: List[int]) -> None:
        self.board[position[0]][position[1]] = "S"
        
    def start_game(self):
        
        self._draw_snake([0, 0])
        self.board[self.food_position[0][0]][self.food_position[0][0]] = 'F'
            
    def _check_snake_on_boarder(self):
        """
        return codes:
        ------------
            1 = snake is on right border (cant move right)
            2 = snake is on left border (cant move left)
            3 = snake is on last row (cant move down)
            4 = snake is on first row 9cant move up)
            
            0 = snake free to move any direction
        """
        if (self.snake_position[1] == (self.height - 1)):
            return 1
        elif (self.snake_position[1] == 0):
            return 2
        elif (self.snake_position[0] == (self.width - 1)):
            return 3
        elif (self.snake_position[0] == 0):
            return 4
        return 0
    
    def _check_snake_eat_tail(self, position):
        if self.board[position[0]][position[1]] == "S":
            return True
    
    def _did_snake_eat_food(self):
        return self.food_position[0] == self.snake_position
            
    def move(self, direction: str) -> int:
        
        direction = direction.upper()
        choices = 'R L D U'.split()
        
        msg = "Can only move right, left, down, or up!!!"
        assert direction in choices, ValueError(msg)
        
        msg_border = "Snake is on border, can't move that direction"
        msg_tail = "Snake can't move that way without eating its tail"
        
        if direction == 'R':
            if self._check_snake_on_boarder() == 1:
                warnings.warn(msg_border)
            elif self._check_snake_eat_tail([self.snake_position[0],self.snake_position[1]+1]):
                warnings.warn(msg_tail)
            else:
                self.snake_position[1] += 1
        elif direction == 'L':
            if self._check_snake_on_boarder() == 2:
                warnings.warn(msg_border)
            elif self._check_snake_eat_tail([self.snake_position[0],self.snake_position[1]-1]):
                warnings.warn(msg_tail)
            else:
                self.snake_position[1] -= 1
        elif direction == 'D':
            if self._check_snake_on_boarder() == 3:
                warnings.warn(msg_border)
            elif self._check_snake_eat_tail([self.snake_position[0]+1,self.snake_position[1]]):
                warnings.warn(msg_tail)
            else:
                self.snake_position[0] += 1
        else:
            if self._check_snake_on_boarder() == 4:
                warnings.warn(msg_border)
            elif self._check_snake_eat_tail([self.snake_position[0]-1,self.snake_position[1]]):
                warnings.warn(msg_tail)
            else:
                self.snake_position[0] -= 1

        self.snake_length += 1
        
        if self._did_snake_eat_food():
            self.move_food()
            
        self._draw_snake(self.snake_position)
                
            


############################

def test_make_board():
    
    board = make_board(5, 5)
    
    expected = (5, 5)
    actual = (len(board), len(board[0]))
    
    assert actual == expected

if __name__ == "__main__":
    
    #pytest.main()
    
    new_game = Snake(11, 11, [[10,10], [9, 7], [3, 4]])
    

    new_game.start_game()
    print(new_game)
    new_game.move("R")
    print(new_game)
    new_game.move("R")
    new_game.move("R")
    new_game.move("R")
    new_game.move("R")
    new_game.move("R")
    new_game.move("R")
    new_game.move("R")
    new_game.move("R")
    new_game.move("R")
    print(new_game)
    new_game.move("D")
    new_game.move("D")
    new_game.move("D")
    new_game.move("D")
    new_game.move("D")
    new_game.move("D")
    new_game.move("D")
    new_game.move("D")
    new_game.move("D")
    new_game.move("D")
    print(new_game)
    print(new_game.snake_position)
    print(new_game.food_position[0])
    new_game.move("L")
    new_game.move("L")
    new_game.move("L")
    new_game.move("U")
    print(new_game)
    print(new_game.snake_position)
    print(new_game.food_position[0])
    new_game.move("U")
    new_game.move("U")
    new_game.move("U")
    new_game.move("U")
    new_game.move("U")
    new_game.move("U")
    new_game.move("L")
    new_game.move("L")
    new_game.move("L")
    print(new_game)
    