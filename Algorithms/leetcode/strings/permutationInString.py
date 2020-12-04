"""
Details
-------

given two strings, find out if one of the permutations of the first
is contained in the second


Examples
--------

    Input: s1 = "ab", s2 = "eidbaooo"
    Out: True
    why? "ba" in s2
    
    .................................
    
    Input: s1 = "ab", s2 = "eidboaoo"
    Out: False

"""
import pytest
from itertools import permutations


def is_permutation_in_string(s1: str, s2: str) -> bool:
    
    if s1 in s2: return True
    
    s1_permutations = [''.join(permutation) for permutation in permutations(s1)]
    
    for permutation in s1_permutations:
        if permutation in s2:
            return True
    return False

    
    
    
    
    
    

#################################################

def test_is_permutation_in_string_true():
    
    expected = True
    actual = is_permutation_in_string(s1 = "ab", s2 = "eidbaooo")
    
    assert actual == expected
    
    
def test_is_permutation_in_string_false():
    
    expected = False
    actual = is_permutation_in_string(s1 = "ab", s2 = "eidboaoo")
    
    assert actual == expected
    
    
if __name__ == "__main__":
    pytest.main()
    
    