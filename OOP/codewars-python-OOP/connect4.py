"""
connectfour.py
--------------

This module contains classes and funtions to
support a basic connect 4 console game.


functions:
    1) matrix make_board(rows: int, cols: int)
    

classes:
    1) Player(id: int, colour: str):
        properties:
            * int id
            * str colour
            
        methods:
            * void __repr__()
            
            * void take_turn(board, row, column)  -- invoke boad._check_state()
            
            
    2) Connect4(rows: int, cols: int)
        properties:
        
            class:
                * int games_played
                * defaultdict player_stats
        
            instance:
                * matrix board
                * Player winner
                
        
        methods:
        
            class:
                * void _increment_games_played
                * void _update_player_stats
        
            instance:
            
                * void _check_state(self)  -- set winner, update stats
                * void __repr__
            
"""
import pytest, warnings
from collections import defaultdict
from typing import List, Optional

Matrix = List[List[str]]


def make_board(rows: int, cols: int, filler: Optional[str] = " ") -> Matrix:
    """
    returns a 2d array of size rows X cols, each element
    filled with "filler".
    """
    
    return [[filler for i in range(cols)] for j in range(rows)]


class Player:
    
    def __init__(self, id: int, colour: str):
        self.id = id
        self.colour = colour
        
    def __repr__(self):
        return f"Player {self.id}"
    
    def take_turn(self, board, row: int, col: int) -> None:
        """
        Fill board at position row, col with colour
        """
        board.board[row-1][col-1] = self.colour
        # board._check_state()
        
        
        
        
class Connect4:
    
    _games_played = 0
    _player_stats = defaultdict(list)
    
    def __init__(self, rows: int, cols: int):
        
        self.board = make_board(6, 7)
        self.winner = None
        
        Connect4._games_played += 1
        
        
    def __repr__(self):
        
        board = ""
        for row in self.board:
            board += f"{row}\n"
            
        return board
    
    @classmethod
    def games_played(cls):
        return cls._games_played
    
    @classmethod
    def player_stats(cls):
        return cls._player_stats
    
    def _check_state(self):
        
        # check rows
        pointer1 = 0
        pointer2 = 3
        
        msg = "Game over"
        
        for row in self.board:
            
            while pointer2 < len(self.board[0]):
                
                if set(row[pointer1:pointer2+1]) == {'R'}:
                    warnings.warn(msg)
                    return 'R'
                elif set(row[pointer1:pointer2+1]) == {'L'}:
                    warnings.warn(msg)
                    return 'L'
                pointer1 += 1
                pointer2 += 1
            pointer1 = 0
            pointer2= 3
            
    
    
    
    
    
####################################

def test_make_board():
    
    filler = "-"
    rows, cols, = 3, 3
    
    expected = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]
    
    actual = make_board(filler, rows, cols)
    
    assert actual == expected
    
    
    
if __name__ == "__main__":
    #pytest.main()
    
    game = Connect4(6, 7)
    #print(game)
    player1 = Player(1, "R")
    player2 = Player(2, "B")
    
    player1.take_turn(game, 6, 5)
    player2.take_turn(game, 6, 6)
    #print(game)
    
    player1.take_turn(game, 5, 5)
    player2.take_turn(game, 5, 6)
    #print(game)
    
    player1.take_turn(game, 4, 5)
    player2.take_turn(game, 3, 5)
    #print(game)
    
    player1.take_turn(game, 6, 4)
    player2.take_turn(game, 6, 7)
    #print(game)
    
    player1.take_turn(game, 5, 4)
    player2.take_turn(game, 5, 7)
    #print(game)
    
    player1.take_turn(game, 4, 4)
    player2.take_turn(game, 4, 7)
    #print(game)
    
    player1.take_turn(game, 6, 3)
    player1.take_turn(game, 6, 2)
    #print(game)
    game._check_state()
    
