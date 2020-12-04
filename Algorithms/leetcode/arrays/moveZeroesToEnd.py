"""
solution.py

Given an array which may contain 0's,
move zeroes to end of array, if any exist
"""
import pytest
from typing import List, Any

def move_zeroes_to_end(array: List[Any]) -> List[Any]:
    
    zero_array = sorted(array, key = lambda x: x == 0 and not isinstance(x, bool))
    
    return zero_array

                

######################################################
def test_move_zeroes_to_end_mixed_types():
    original = [False, 0, 0, 2, 4, 0, 1, 'a']
    
    expected = [False, 2, 4, 1, 'a', 0, 0, 0]
    actual = move_zeroes_to_end(original)
    
    assert actual == expected

    
def test_move_zeroes_to_end_all_ints():  
    original = [6, 0, 0, 2, 4, 0, 1, 7]
    
    expected = [6, 2, 4, 1, 7, 0, 0, 0]
    actual = move_zeroes_to_end(original)
    
    assert actual == expected

    
def test_move_zeroes_to_end_no_zeroes():
    original = [False, 2, 4, 1, 'a']
    
    expected = [False, 2, 4, 1, 'a']
    actual = move_zeroes_to_end(original)
    
    assert actual == expected  


if __name__ == "__main__":
    
    pytest.main()