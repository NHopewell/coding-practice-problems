"""
Given two strings, a and b, of same of different lengths
return min number of deletion which can be made from
both string to make them anagrams, if possible (-1)

Example:
=======

    In: >>> a = "cde", b = "abc"
    Out: >>> 4

why? must delete d+e from a and a+b from b

"""
import pytest

def make_anagram(string1: str, string2: str) -> int:
    
    if len(string1) <= len(string2):
        shortest, longest = string1, string2
    else:
        shortest, longest = string2, string1
    
    del_shortest: int = 0
        
    for char in shortest:
        if char not in longest:
            del_shortest += 1
            
    del_longest: int = len(longest) - ( len(shortest) - del_shortest )
        
    if (len(shortest) + len(longest)) == (del_longest + del_shortest):
        return - 1
    return del_shortest + del_longest
        
    
#################################################

def test_make_anagram_case_one():
    expected = 4
    actual = make_anagram("cde", "abc")
    
    assert expected == actual

    
def test_make_anagram_case_two():
    expected = 3
    actual = make_anagram("cdev", "adc")
    
    assert expected == actual
    
    
def test_make_anagram_case_three():
    expected = -1
    actual = actual = make_anagram("cde", "axyz")
    
    assert expected == actual
    
    
if __name__ == "__main__":
    pytest.main()
    