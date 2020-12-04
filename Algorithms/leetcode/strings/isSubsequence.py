"""
Problem:
    given string s and t, check if s is subsequence of t
    
Examples:

    Input: s ="abc", t = "ahbgdc"
    Output: True
    
    ------
    
    Input: s = "axc", t = "ahbgdc"
    Output: false

"""
import pytest


def is_subsequence(s: str, t: str) -> bool:
    
    LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

    p_left = p_right = 0
    while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
        # move both pointers or just the right pointer
        if s[p_left] == t[p_right]:
            p_left += 1
        p_right += 1

    return p_left == LEFT_BOUND


    
"""
    if not s:
        return True
    
    if ( len(s) == 1 ) and ( len(t) == 1 ):
        return s == t
    
    pointer1: int = 0
    pointer2: int = 0
    
    while ( pointer1 < len(s) ) and  ( pointer2 < len(t) ):
        if t[pointer2] == s[pointer1]:
            pointer1 += 1
            pointer2 += 2
        else:
            pointer2 += 2
            
    if len(s) == 2:
        return pointer1 == 2
    return pointer1 == len(s) -1
    
    
"""

    
###### TESTS ######
def test_is_substraing_true():
    
    expected = True
    actual = is_subsequence(s ="abc", t = "ahbgdc")
    
    print(f"actual: {actual}, expected: {expected}")
    assert actual == expected
    
    
def test_is_substraing_false():
    
    expected = False
    actual = is_subsequence(s = "axc", t = "ahbgdc")
    
    print(f"actual: {actual}, expected: {expected}")
    assert actual == expected
    
    
if __name__ == "__main__":
    pytest.main()
