"""
https://leetcode.com/problems/group-anagrams/
"""
from typing import List
import pytest

def group_anagrams(strings: List[str]) -> List[List[str]]:
    
    from collections import defaultdict
    
    _dict = defaultdict(list)
    
    for i in strings:
        _dict[tuple(sorted(i))].append(i)
        
    return list(sorted(_dict.values(), key = lambda i: len(i)))

    

########################################
def test_group_anagrams_case_one():
    
    test_case = ["eat","tea","tan","ate","nat","bat"]
    
    expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
    actual = group_anagrams(test_case)
    
    assert actual == expected
    
    
def test_group_anagrams_case_two():
    
    test_case = [""]
    
    expected = [[""]]
    actual = group_anagrams(test_case)
    
    assert actual == expected
    
    
def test_group_anagrams_case_three():
    
    test_case = ["a"]
    
    expected = [["a"]]
    actual = group_anagrams(test_case)
    
    assert actual == expected
    
    
if __name__ == "__main__":
    pytest.main()
    