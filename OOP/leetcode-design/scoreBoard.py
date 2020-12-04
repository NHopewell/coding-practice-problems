"""
Design a LeaderBoard
---------------------
https://leetcode.com/problems/design-a-leaderboard/



"""
from typing import Tuple

class Player:
    
    def __init__(self, id: int):
        
        self.id = id
        
    def __repr__(self):
        
        return f"Player: {self.id}"
        
    
    
    
class LeaderBoard:
    
    def __init__(self):
        
        self._board = []
        
    @property
    def board(self):
        return self._board
    
    @property
    def num_entries(self) -> int:
        return len(self.board)
    
    def add_score(self, score: Tuple[Player, int]) -> None:
        
        self._board.append(score)
        
        self._board = sorted(self._board, key = lambda x: x[1], reverse=True)
        
    def top_k(self, k: int) -> None:
        if k > self.num_entries:
            msg = f"There are only {self.num_entries} scores on the leader board"
            raise ValueError(msg)
            
        return sum([score[1] for score in self.board[:k]])
    

    def reset(self, player_id: int) -> None:
        
        for score in self.board:
            if score[0].id == player_id:
                self.board.remove(score)
    
    
    
    
###################################
if __name__ == "__main__":
    
    player1 = Player(1)
    player2 = Player(2)
    player3 = Player(3)
    
    score_one = (player1, 73)
    score_two = (player2, 56)
    score_three = (player3, 39)
    
    leader_board = LeaderBoard()
    for score in (score_one, score_two, score_three):
        leader_board.add_score(score)
        
    print(leader_board.board)
    print(leader_board.top_k(1))
    print(leader_board.top_k(3))
    leader_board.reset(1)
    print(leader_board.board)
    print(leader_board.top_k(2))