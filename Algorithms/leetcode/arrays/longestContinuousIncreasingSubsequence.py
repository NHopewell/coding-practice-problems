"""
longest continuous subarray

return len

Example:

    Input: nums = [1,3,5,4,7]
    Output: 3    
        
    Input: nums = [2,2,2,2,2]
    Output: 1
    
"""
import pytest
from typing import List

def find_longest_continuous_subarray(array: List[int]) -> int:
    
    longest_sub_array = 1
    continued = 1
    pointer1 = 0
    pointer2 = 1
    
    if not array: return 0
    
    while pointer2 < len(array):
        
        if array[pointer1] < array[pointer2]:
            continued += 1
            longest_sub_array = max(continued, longest_sub_array)
        else:
            longest_sub_array = max(continued, longest_sub_array)
            continued = 1
            
        pointer1 += 1
        pointer2 +=1
    
    return longest_sub_array
        
        

        
#############################################

def test_find_longest_continuous_subarray_case_one():
    
    array = [1,3,5,4,7]
    
    expected = 3
    actual = find_longest_continuous_subarray(array)
    
    assert actual == expected

def test_find_longest_continuous_subarray_case_two():
    
    array = [2,2,2,2,2]
    
    expected = 1
    actual = find_longest_continuous_subarray(array)
    
    assert actual == expected



if __name__ == "__main__":
    pytest.main()