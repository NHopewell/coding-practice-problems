"""
tic tac toe
-----------

https://leetcode.com/problems/design-tic-tac-toe/

_.py

functions:
----------
    matrix make_board(size: int) -> matrix

classes:

    Player(id: int)
        
        properties  
            * id: int
            
        methods:
            * void __repr__
            
            
    TicTacToe(board_size: int)
        
        Properties
            class properties
                * int games_played
                * dict player_stats
            instance properties  
                * board: matrix
                * players: list[Player]
                * winner: none

            
        methods
            instance methods
                * void move(player: Player, row: int, col: col)
                * bool _check_state()
                * void end_game()
                * void _reset_board()
            class methods
                * void _increment_games_played()
                * void update_player_stats(winner: Player)

"""
import pytest, warnings
from typing import List
from collections import defaultdict

Matrix = List[List[str]]

def make_board(size: int) -> Matrix:
    
    filler = "-"
    return [[filler for i in range(size)] for j in range(size)]


class Player:
    
    def __init__(self, id: int):
        
        self.id = id
        self._symbol = ''
        
    def __repr__(self):
        
        return f"Player {self.id}"
    
    @property
    def symbol(self):
        return self._symbol
    
    @symbol.setter
    def symbol(self, new):
        self._symbol = new
    
    
class TicTacToe:
    
    games_played: int = 0
    player_stats = defaultdict(list)
    
    def __init__(self, board_size: int):
        
        self.board = make_board(board_size)
        self.players = []
        self.winner = None
        
        
    def __repr__(self):
        
        board = ""
        for row in self.board:
            board += f"{row}\n"
        
        return board
    
    @classmethod
    def _increment_games_played(cls):
        cls.games_played += 1
        
    @classmethod
    def _update_player_stats(cls, winner: int) -> None:
        if winner == 1:
            cls.player_stats["Player-one"].append(1)
            cls.player_stats["Player-two"].append(0)
        else:
            cls.player_stats["Player-two"].append(0)
            cls.player_stats["Player-one"].append(1)     
    
    def start_game(self, player1: Player, player2: Player) -> None:
        
        player1.symbol = 'X'
        player2.symbol = 'O'
        
        self.players.append(player1)
        self.players.append(player2)
        
        TicTacToe._increment_games_played()
        
    def move(self, player_number: int, row: int, col: int) -> None:
        
        if self.board[row][col] == '-':
            if player_number == 1:
                self.board[row][col] = self.players[0].symbol
            else:
                self.board[row][col] = self.players[1].symbol
        else:
            msg = ("That spot has alreay be used.")
            warnings.warn(msg)
            
        winner = self._check_state()
        
        if winner:
            self._end_game(winner)

                
    def _reset_board(self, size: int):
        self.board = make_board(size)
        
    def _end_game(self, winner: int) -> None:
        if winner == 1:
            TicTacToe._update_player_stats(1)
            self.winner = self.players[0]
        else:
            TicTacToe._update_player_stats(2)
            self.winner = self.players[1]
            
        self._reset_board(len(self.board))
            
        

    def _check_state(self):
        
        winner = False
        # check horizontal winner
        for row in self.board:
            if set(row) == {'X'}:
                winner = 1
                break
            elif set(row) == {'O'}:
                winner = 2
                break
        
        if not winner:
            # check for vertical winner
            column = []
            for i in range(len(self.board)):
                for j in range(len(self.board)):
                    column.append(self.board[j][i])
                    
                if set(column) == {'X'}:
                    winner = 1
                    break
                elif set(column) == {'O'}:
                    winner = 2
                    break
                else:
                    column = []
                    
        if not winner:
            # check diagonals
            diagonal_one = [
                self.board[0][0],
                self.board[1][1],
                self.board[2][2]
            ]
            
            diagonal_two = [
                self.board[0][2],
                self.board[1][1],
                self.board[2][0]
            ]
            
            if (set(diagonal_one) == {'X'}) or (set(diagonal_two) == {'X'}):
                winner = 1
            elif (set(diagonal_one) == {'O'}) or (set(diagonal_two) == {'O'}):
                winner = 2
                
        if winner:
            msg = f"Player {winner} wins!!!"
            warnings.warn(msg)
        return winner
                
    
    
    
    




####################################

def test_make_board_3_x_3():
    
    test_case = 3
    
    expected = [["-", "-", "-"], 
                ["-", "-", "-"],
                ["-", "-", "-"]]
    
    actual = make_board(test_case)
    
    assert actual == expected
    
    
def test_new_player():
    
    test_case = 1
    new_player = Player(test_case)
    
    expected = "Player 1"
    actual = new_player.__repr__()
    
    assert actual == expected
    
    
    
if __name__ == "__main__":
    
    TTT = TicTacToe(3)
    print(TTT)
    
    player1 = Player(1)
    player2 = Player(2)
    
    TTT.start_game(player1, player2)
    
    print(TTT.players)
    print(TTT.players[0].symbol)
    
    TTT.move(2, 0, 1)
    print(TTT)
    TTT.move(2, 1, 1)
    print(TTT)
    TTT.move(2, 2, 1)
    print(TTT)

    #pytest.main()
