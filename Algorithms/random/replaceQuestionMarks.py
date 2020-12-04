"""

Consider the following bit string 11?100

you need to write a method which can replace this question mark with 1 & 0

Output should be: 110100 , 111100
This should be implemented for N number of question mark each time replaced with 1 and then with 0

"""
import pytest
from typing import Tuple


def replace_question_marks(string: str) -> Tuple[str]:
    
    
    ones_first = ""
    zeroes_first = ""
    
    swap1, swap2 = "1", "0"
    
    for i, char in enumerate(string):
        if char != "?":
            ones_first += char
            zeroes_first += char
        else:
            ones_first += swap1
            zeroes_first += swap2
            
            swap1, swap2 = swap2, swap1
    
    return (zeroes_first, ones_first)
    
    

    
#################################################
def test_replace_question_marks_case_one():
    
    test_case = "11?100"
    
    expected = ("110100", "111100")
    actual = replace_question_marks(test_case)
    
    assert actual == expected

    
def test_replace_question_marks_case_two():
    
    test_case = "1??100?10?"
    
    expected = ("1011000101", "1101001100")
    actual = replace_question_marks(test_case)
    
    assert actual == expected
    
    
if __name__ == "__main__":
    pytest.main()