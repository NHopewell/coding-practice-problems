import pytest
from typing import List

def is_monotonic_array(array: List[int]) -> bool:
    
    pointer1 = 0
    pointer2 = 1
    
    total_greater_than_or_equal = 0
    total_less_than_or_equal = 0
    
    while pointer2 < (len(array)):
    
        
        if array[pointer1] > array[pointer2]:

            total_less_than_or_equal += 1
        elif array[pointer1] < array[pointer2]:

            total_greater_than_or_equal += 1
        else:
            total_less_than_or_equal += 1
            total_greater_than_or_equal += 1
            
        pointer1 += 1
        pointer2 += 1
            
    return (total_less_than_or_equal == (len(array) -1)) or (total_greater_than_or_equal == (len(array) -1))
    
    
    
#############################################

def test_is_monotonic_ascending():
    in_array = [1, 2, 2, 3]
    
    expected = True
    actual = is_monotonic_array(in_array)
    
    assert actual == expected
  

def test_is_monotonic_descending():
    in_array = [6, 5, 4, 4]
    
    expected = True
    actual = is_monotonic_array(in_array)
    
    assert actual == expected

    
def test_is_not_monotonic():
    
    in_array = [2, 5, 3]
    
    expected = False
    actual = is_monotonic_array(in_array)
    
    assert actual == expected
    


if __name__ == '__main__':
    pytest.main()