"""
Conways Game of Life
--------------------

Rules:
    Any living cell with fewer than two living neighbors dies.
    Any living cell with exactly two or exactly three living neighbors remains alive.
    Any living cell with more than three living neighbors dies.
    Any dead cell with exactly three living neighbors becomes alive.

    def sum_ad(row, col, max_rows, max_cols):
    
    keys = list(range(1, 9))
    vals = [
            [row-1][col-1],  # 1
            [row-1][col],    # 2
            [row-1][col+1],  # 3
            [row][col-1],    # 4
            [row][col+1],    # 5
            [row+1][col-1],  # 6
            [row+1][col],    # 7
            [row+1][col+1]   # 8
    ]
    
    indexes = dict(zip(keys, vals))
     
    if rows == 0:
        indexes["1"], index["2"], indexes["3"] = 0, 0, 0
    
    if cols == 0:
        indexes["1"], indexes["4"], indexes["6"] = 0, 0, 0
    
    if rows == (self.rows-1):
        indexes["7"], indexes["8"], indexes["9"] = 0, 0, 0
    
    if cols == (self.cols-1):
        indexes["3"], indexes["5"], indexes["8"] = 0, 0, 0
        
    sum_indexes = 0
    
    for val in indexes.values:
        if val != 0:
            sum_indexes += self.board[val[0]][val[1]].alive
        


    [
    self.board[row-1][col-1].alive,
    self.board[row-1][col].alive,
    self.board[row-1][col+1].alive,
    self.board[row][col-1].alive,
    self.board[row][col+1].alive,
    self.board[row+1][col-1].alive,
    self.board[row+1][col].alive,
    self.board[row+1][col+1].alive
    ]

"""
from typing import List, Any

class Cell:
    
    def __init__(self, alive: bool):
        
        self._alive = alive
        
    def __repr__(self):
        
        if self.alive:
            msg = " is alive"
        else:
            msg = " is dead"
        return f"Cell {msg}"
    
    @property
    def alive(self):
        return self._alive
    
    @alive.setter
    def alive(self, new):
        self._alive = new
        
    def kill(self):
        
        self.alive = False
        
    def revive(self):
        
        self.alive = True

        
def make_board(rows: int, cols: int) -> List[List[Any]]:
    
    from random import choice
    choices = (True, True, True, False, False)
    
    return[[Cell(choice(choices)) for i in range(cols)] for j in range(rows)]


class GameOfLife:
    
    def __init__(self, rows: int, cols: int):
        
        self.board = make_board(rows, cols)
        self._rows = rows
        self._cols = cols
        
    @property
    def rows(self):
        return self._rows
    
    @property
    def cols(self):
        return self._cols
        
    def is_alive(self, row: int, col: int) -> bool:
        
        return self.board[row][col].alive
        
    def set_alive(self, row: int, col: int) -> None:
        
        self.board[row][col].revive()
    
    def _sum(self, row, col): 
        keys = list(range(1, 9))
        vals = [
                [row-1, col-1],  # 1
                [row-1, col],    # 2
                [row-1, col+1],  # 3
                [row, col-1],    # 4
                [row, col+1],    # 5
                [row+1, col-1],  # 6
                [row+1, col],    # 7
                [row+1, col+1]   # 8
        ]

        indexes = dict(zip(keys, vals))
    
        
        if row == 0:
            indexes[1], indexes[2], indexes[3] = 0, 0, 0

        if col == 0:
            indexes[1], indexes[4], indexes[6] = 0, 0, 0

        if row == (self.rows-1):
            indexes[6], indexes[7], indexes[8] = 0, 0, 0

        if col == (self.cols-1):
            indexes[3], indexes[5], indexes[8] = 0, 0, 0
            
        sum_indexes = 0

        for val in indexes.values():
            if val != 0:
                sum_indexes += self.board[val[0]][val[1]].alive
                
        return sum_indexes
        
        
    def get_num_living_neighbours(self, row: int, col: int) -> None:
        """

        """
        cell = self.board[row][col]

        
        num_alive = self._sum(row, col)
        
        if self.is_alive(row, col):
            if num_alive < 2:
                cell.kill()
            elif num_alive > 3:
                cell.kill()
        else:
            if num_alive in (3, 2):
                cell.revive()
                
        self.board[row][col] = cell

        
    def play_game(self):
        
        for i in range(self.rows):
            for j in range(self.cols):
                self.get_num_living_neighbours(i, j)
        
        
        
#############################################

if __name__ == "__main__":
    
    game_of_life = GameOfLife(6, 6)
    
    
    for row in game_of_life.board:
        print(f"{row}\n")
    
    #print(game_of_life.board)
    
    game_of_life.play_game()
    
    print()
    print()
    
    #print(game_of_life.board)
    
    for row in game_of_life.board:
        print(f"{row}\n")
    
    