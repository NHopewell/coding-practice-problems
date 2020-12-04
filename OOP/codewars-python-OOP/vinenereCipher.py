"""
Vingenete Cipher Helper
-----------------------

https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python
"""

class Cipher:
    
    def __init__(self, key: str):
        
        from string import ascii_lowercase
        from collections import deque
        
        
        self.key = key
        self.letters = deque(ascii_lowercase)
        self.letter_map = dict(zip(ascii_lowercase, range(len(ascii_lowercase))))
        
        
    
    def encode(self, text: str) -> str:
            
        encoded_msg = ""
        
        for i, letter in enumerate(text):
            positions_to_shift = self.letters.index(letter) + self.letter_map[self.key[i]]
            self.letters.rotate(positions_to_shift * -1)
            encoded_msg += self.letters[0]
            self.letters.rotate(positions_to_shift)
            
        return encoded_msg
                
            
            
    

  

if __name__ == "__main__":
    
    cipher = Cipher('password')
    
    print(cipher.encode("codewars"))
