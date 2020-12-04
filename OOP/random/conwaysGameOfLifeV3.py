"""
conways game of life
--------------------


"""
import pytest
from typing import List

class Cell:
    
    def __init__(self, alive: bool):
        
        self.alive = alive
        
    def __repr__(self):
        
        if self.alive:
            return "+"
        return "-"
    
    def kill(self):
        self.alive = False
    
    def revive(self):
        self.alive = True
        

CellMatrix = List[List[Cell]]


def _make_cell_matrix(cols: int, rows: int) -> CellMatrix:
    
    from random import choice
    
    choices = (True, False)
    
    return [[Cell(choice(choices)) for i in range(cols)] for j in range(rows)]



class GameOfLife:
    
    def __init__(self, cols: int, rows: int):
        
        self.cols = cols
        self.rows = rows
        self.board = _make_cell_matrix(cols, rows)
        
        
    def __repr__(self):
        
        pretty_board = ""
        
        for row in self.board:
            pretty_board += f"{row}\n"
            
        return pretty_board
    
    def is_alive(self, row: int , col: int) -> bool:
        
        return self.board[row][col].alive
    
    
    def check_neighbourhood(self, row: int, col:int) -> int:
        """
        above: (row-1, col-1), (row-1, col), (row-1, col+1)
        same: (row, col-1), (row, col+1)
        below: (row+1, col-1, (row+1, col), (row+1, col+1)
        
        """
        indexes = range(1, 9)
        to_sum = [(row-1, col-1), (row-1, col), (row-1, col+1),
                  (row, col-1), (row, col+1),
                  (row+1, col-1), (row+1, col), (row+1, col+1)]
                   
                   
        neighbourhood = {k:v for (k,v) in zip(indexes, to_sum)}
                   
        if row == 0:
            neighbourhood[1], neighbourhood[2], neighbourhood[3] = 0, 0, 0
        
        if row == self.rows-1:
            neighbourhood[6], neighbourhood[7], neighbourhood[8] = 0, 0, 0
        
        if col == 0:
            neighbourhood[1], neighbourhood[4], neighbourhood[6] = 0, 0, 0
        
        if col == self.cols-1:
            neighbourhood[3], neighbourhood[5], neighbourhood[8] = 0, 0, 0
            
            
        neighbourhood_sum = 0
        
        for index in neighbourhood:
            if neighbourhood[index] != 0:
                neighbourhood_sum += self.board[neighbourhood[index][0]][neighbourhood[index][1]].alive
                
                
        return neighbourhood_sum
    
    
    def update_cell_state(self, row: int, col: int) -> None:
        
        """
        Rules:
            Any living cell with fewer than two living neighbors dies.
            Any living cell with exactly two or exactly three living neighbors remains alive.
            Any living cell with more than three living neighbors dies.
            Any dead cell with exactly three living neighbors becomes alive.
        """
        
        neighbourhood_sum = self.check_neighbourhood(row, col)
        
        if self.board[row][col].alive:
            if neighbourhood_sum < 2:
                self.board[row][col].kill()
            elif neighbourhood_sum > 3:
                self.board[row][col].kill()
        else:
            if neighbourhood_sum == 3:
                self.board[row][col].revive()
                
                
                
    def play(self, turns: int) -> None:
        
        while turns >= 1:
            
            print(self)
            
            for i in range(self.rows):
                for j in range(self.cols):
                    self.update_cell_state(i, j)
            
            print(self)
            turns -= 1
                
                
        






#######################################
def test_make_call_matrix():
    
    cols = 6
    rows = 6
    
    matrix = _make_cell_matrix(cols, rows)
    
    expected = (6, 6)
    actual = (len(matrix), len(matrix[0]))
    
    assert actual == expected
    
    
    
    
    
if __name__ == "__main__":
    
    #pytest.main()
    
    game = GameOfLife(10, 10)
                   
    
    print(game)
    print(game.is_alive(1, 0))
    print(game.check_neighbourhood(0,0))
    
    game.play(5)
                   
    