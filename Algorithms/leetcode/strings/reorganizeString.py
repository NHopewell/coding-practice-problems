"""
https://leetcode.com/problems/reorganize-string/

can you reorganize a  string such that there are no repeating
characters? if not return ""

"""
import pytest
from collections import Counter


def reorganize_string(string: str) -> str:
    
    counter = Counter(string)
    most_common = counter.most_common(1)[0]
    most_common_letter, most_common_count = most_common[0], most_common[1]
    rest = sum(counter.values()) - most_common_count
    
    if most_common_count > (rest +1):
        return ""
    
    first = most_common_letter * most_common_count
    second = string.replace(most_common_letter, "")
    reorganized = ""
    p1 = 0
    
    while (p1 < len(first)) and (p1 < len(second)):
        reorganized += first[p1]
        reorganized += second[p1]
        p1 += 1
        
    if len(second) > len(first):
        reorganized += second[p1:]
    else:
        reorganized += first[-1]
    
    return reorganized
    
    
    
##########################################

def test_reorganize_string_case_one():
    
    test_case = "aab"
    
    expected = "aba"
    actual = reorganize_string(test_case)
    
    assert actual == expected
    
def test_reorganize_string_case_two():
    
    test_case = "aaabc"
    
    expected = "abaca"
    actual = reorganize_string(test_case)
    
    assert actual == expected
    
def test_reorganize_string_case_three():
    
    test_case = "aaab"
    
    expected = ""
    actual = reorganize_string(test_case)
    
    assert actual == expected
    
    
def test_reorganize_string_case_four():
    
    test_case = "aaabbcde"
    
    expected = ("ababacde", "acadabeb")
    actual = reorganize_string(test_case)
    
    assert actual in expected
    
    
if __name__ == "__main__":
    pytest.main()