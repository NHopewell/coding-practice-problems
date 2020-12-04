"""
Given a string which only contains A and B,
find minmum number of deletions such that there
are no repeating chars.

Example:
========
    In: "AABAAB"
    Out: 2
    
why? delete the A's at index 1 and 4, 2 deletions

"""
import pytest
    
    
    
def remove_alternating_chars(string: str) -> int:
    
    pointer1 = 0
    pointer2 = 1
    num_removes: int = 0
    
    while pointer2 < len(string):
        if string[pointer1] == string[pointer2]:
            num_removes += 1
        pointer1 += 1
        pointer2 += 1
        
    return num_removes
    
    
"""
Test Cases:
-----------

"AABAAB" => 2
"AAABBBA" => 4
"BBABABAAB" => 2
"ABAB" => 0
"""

def test_remove_alternating_chars_AABAAB():
    
    expected = 2
    actual = remove_alternating_chars("AABAAB")
    
    assert actual == expected
    
    
def test_remove_alternating_chars_AAABBBA():
    
    expected = 4
    actual = remove_alternating_chars("AAABBBA")
    
    assert actual == expected
    
    
def test_remove_alternating_chars_BBABABAAB():
    
    expected = 2
    actual = remove_alternating_chars("BBABABAAB")
    
    assert actual == expected
    
    
def test_remove_alternating_chars_ABAB():
    
    expected = 0
    actual = remove_alternating_chars("ABAB")
    
    assert actual == expected
    
    
if __name__ == "__main__":
    pytest.main()