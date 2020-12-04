"""
Given array of ints, return 3rd largest, else largest


"""
from typing import List
import pytest

def get_3rd_largest(array: List[int]) -> int:
    
    if len(array) < 3:
        return max(array)
    
    return sorted(set(array))[-3]



################################

def test_get_3rd_largest_case_one():
    
    array = [7, 1, 3, 5, 7, 8]
    
    expected = 5
    actual = get_3rd_largest(array)
    
    assert actual == expected
    
    
def test_get_3rd_largest_case_two():
    
    array = [7, 1]
    
    expected = 7
    actual = get_3rd_largest(array)
    
    assert actual == expected
    
    
if __name__ == "__main__":
    
    pytest.main()
    