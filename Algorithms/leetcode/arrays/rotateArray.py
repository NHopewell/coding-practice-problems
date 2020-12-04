"""
write a class that takes an array 
has rotate method
"""
import pytest
from collections import deque
from typing import Optional, List


class ArrayRotator:
    
    def __init__(self, array: Optional[List] = None):
        
        if array:
            self.array = deque(array)
        else:
            self.array = deque([])
            
    def rotate(self, direction: str, positions: int) -> None:
        
        options = ("right", "left")
        msg = "Can only rotate 'right' or 'left'."
        assert(direction in options), ValueError(msg)
        
        if direction == "right":
            self.array.rotate(positions)
        else:
            positions *= -1
            self.array.rotate(positions)
            
    
    
##################################################

def test_rotate_array_right():
    
    rotator = ArrayRotator([1, 2, 3, 4, 5, 6, 7])
    rotator.rotate("right", 3)
    
    expected = deque([ 5, 6, 7, 1, 2, 3, 4])
    actual = rotator.array
    
    assert actual == expected
    

def test_rotate_array_left():
    
    rotator = ArrayRotator([1, 2, 3, 4, 5, 6, 7])
    rotator.rotate("left", 2)
    
    expected = deque([3, 4, 5, 6, 7, 1, 2])
    actual = rotator.array 
    
    assert actual == expected
    



if __name__ == "__main__":
    pytest.main()