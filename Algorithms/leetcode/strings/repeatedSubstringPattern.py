"""
Problem:
    given a string, check if it can be constructed using 
     substring appended multiple times
     
Examples:

    Input: "abab"
    Output" True
    
    -------------
    
    Input: "aba"
    Output: False
    
    -------------
    
    Inputer: "abcabcabcabc"
    Output: True

"""
import pytest


def is_repeated_substring_pattern(s: str) -> bool:
    return s in (s + s)[1: -1]
    
"""

    smallest_window: int = 1
    current_window: int = 1
    #pointer: int = 0
    #left_bountry: int = len(s)
        
    for i, letter in enumerate(s):
        
        for next_letter in s[i+1:]:
            if letter != next_letter:
                current_window += 1
        if smallest_window > 1:
            smallest_window = min(smallest_window, current_window)
        else:
            smallest_window = current_window
            current_window = 1
            
    divided = [s[i: i+smallest_window] for i in range(0, len(s), smallest_window)]
    
    print(divided)
    
    return divided.count(divided[0]) == len(divided)
    
"""

    
    
##### TESTS #####
def test_is_repeated_substring_pattern_true():
    
    expected = True
    actual = is_repeated_substring_pattern("abcabcabcabc")
    
    assert(actual == expected)
    
def test_is_repeated_substring_pattern_false():
    
    expected = False
    actual = is_repeated_substring_pattern("aba")
    
    assert(actual == expected)
    
if __name__ == "__main__":
    pytest.main()