"""
Given strings s1 and s2, return True if words in s1
can be arraged to spell s2, else False


Examples:
---------
    Input: 'rkqodlw', 'world'
    Output: True
    
    
    Input: 'cedewaraaossoqqyt', 'codewars'
    Output: True
    
    
    Input: 'katas', 'steak'
    Output: False

"""
import pytest

def scramblies(s1: str, s2: str) -> bool:
    
    
    original_length = len(s1)
    s1 = list(s1)
    
    for i, letter in enumerate(s2):
        if letter in s1:
            s1.remove(letter)
            
    return len(s1) == (original_length - len(s2))
            
    
    
    
##############################################

def test_scramblies_true():
    
    expected = True
    actual = scramblies('cedewaraaossoqqyt', 'codewars')
    
    assert actual == expected
    
def test_scramblies_false():
    
    expected = False
    actual = scramblies('katas', 'steak')
    
    assert actual == expected
    
    
if __name__ == "__main__":
    pytest.main()