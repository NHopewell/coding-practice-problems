"""
https://leetcode.com/problems/string-to-integer-atoi/
"""
import pytest


class Atoi:
    
    def __init__(self, string: str):
        
        self.string = string
        self.check = 0
        
    def strip(self):
        
        self.string = self.string.strip()
        
    def check_for_int(self):
        
        if self.string[0] == '-':
            self.check = 1
        try:
            int(self.string[self.check])
            return True
        except ValueError:
            return False
        
    def parse(self):
        self.strip()
        
        if self.check_for_int():
            if self.check:
                to_return = "-"
            else:
                to_return = ""
            for i, char in enumerate(self.string[self.check:]):
                try:
                    int(char)
                    to_return += char
                except ValueError:
                    break  
            return int(to_return)
        else:
            return 0


    
    
    
##########################################

def test_atoi_case_one():
    test_case = "42"
    
    atoi = Atoi(test_case)
    
    
    expected = 42
    actual = atoi.parse()
    
    assert actual == expected
    
    
def test_atoi_case_two():
    test_case = "-42"
    
    atoi = Atoi(test_case)
    
    expected = -42
    actual = atoi.parse()
    
    assert actual == expected
    

def test_atoi_case_three():
    test_case = "4193 with words"
    
    atoi = Atoi(test_case)
    
    expected = 4193
    actual = atoi.parse()
    
    assert actual == expected
    
    
def test_atoi_case_four():
    """
    First non white space is not parsible to int
    """
    test_case = "words and 987"
    
    atoi = Atoi(test_case)
    
    expected = 0
    actual = atoi.parse()
    
    assert actual == expected
    
    
if __name__ == "__main__":
    
    pytest.main()