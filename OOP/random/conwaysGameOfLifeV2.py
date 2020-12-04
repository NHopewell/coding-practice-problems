"""
conwaysGameOfLife.py
====================

Contains classes and functions needed to simulate conways game of life

Rules:

    Any living cell with fewer than two living neighbors dies.
    Any living cell with exactly two or exactly three living neighbors remains alive.
    Any living cell with more than three living neighbors dies.
    Any dead cell with exactly three living neighbors becomes alive.
    
    
"""
import pytest
from typing import List


class Cell:
    
    def __init__(self, alive: bool):
        
        self.alive = alive
        
    def __repr__(self):
        
        if self.alive:
            return "Alive"
        return "Dead-"
        
        #return str(int(self.alive))
        
        
    def revive(self):
        self.alive = True

    def kill(self):
        self.alive = False
       

CellMatrix = List[List[Cell]]

def make_board(cols: int, rows: int) -> CellMatrix:
    
    from random import choice
    
    choices = (True, False)
    
    return [[Cell(choice(choices)) for i in range(cols)] for j in range(rows)]


class GameOfLife:
    
    def __init__(self, cols: int, rows: int):
        self.board = make_board(cols, rows)
        self.rows = rows
        self.cols = cols
        
        
    def __str__(self):
        
        board = ""
        for row in self.board:
            board += f"{row}\n"
            
        return board
    
    
    def is_alive(self, col: int, row: int) -> bool:
        return self.board[row][col].alive
  

    def set_alive(self, col: int, row: int) -> None:
        self.board[row][col].revive()
        
        
    def set_dead(self, col: int, row: int) -> None:
        self.board[row][col].kill()
        
        
    def _check_neighbour_sum(self, col: int, row: int) -> int:
        """
        Rules:

            Any living cell with fewer than two living neighbors dies.
            Any living cell with exactly two or exactly three living neighbors remains alive.
            Any living cell with more than three living neighbors dies.
            Any dead cell with exactly three living neighbors becomes alive.
        """
        
        
        neighbours = {
            1: [row-1, col-1], 
            2: [row-1, col],
            3: [row-1, col+1], 
            4: [row, col-1],   
            5: [row, col+1],   
            6: [row+1, col-1], 
            7: [row+1, col],
            8: [row+1, col+1]  
        }
        
        if row == 0:
            neighbours[1], neighbours[2], neighbours[3] = 0, 0, 0
        
        if row == len(self.board)-1:
            neighbours[6], neighbours[7], neighbours[8] = 0, 0, 0
            
        if col == 0:
            neighbours[1], neighbours[4], neighbours[6] = 0, 0, 0
            
        if col == len(self.board[0]) -1:
            neighbours[3], neighbours[5], neighbours[8] = 0, 0, 0
            
        
        neighbour_sum = 0
        for cell in neighbours:
            if neighbours[cell] != 0:
                neighbour_sum += self.board[neighbours[cell][0]][neighbours[cell][1]].alive
        
        if neighbour_sum < 2:
            if self.is_alive(col, row):
                self.set_dead(col, row)
        elif neighbour_sum in (2, 3):
            if self.is_alive(col, row):
                self.set_alive(col, row)
        elif neighbour_sum > 3:
            if self.is_alive(col, row):
                self.set_dead(col, row)
        elif neighbour_sum == 3:
            if not self.is_alive(col, row):
                self.set_alive(col, row)
                
                
    def play(self, turns: int) -> None:

        print(self)

        for i in range(turns):
            for i in range(self.rows):
                for j in range(self.cols):
                    self._check_neighbour_sum(j, i)

            print(self)

        

    
########################################

def test_make_board():
    
    test_case = (6, 6)
    board = make_board(test_case[0], test_case[1])
    
    expected = [6, 6]
    actual = [len(board[0]), len(board)]
    
    assert actual == expected
                  
            
        
if __name__ == "__main__":
    
    #pytest.main()
    
    game = GameOfLife(6, 6)
    
    game.play(5)
    