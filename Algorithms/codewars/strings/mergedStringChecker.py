"""
https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python

Merged string checker

given three strings, check if the first can be formed from the
second two by merging the second thwo strings. Must maintain 
proper order.

Example:
--------
    'codewars' is a merge from 'cdw' and 'oears':

        s:  c o d e w a r s   = codewars
    part1:  c   d   w         = cdw
    part2:    o   e   a r s   = oears
    
"""
import pytest

def check_is_merge(s: str, part1: str, part2: str) -> bool:
    
    p = 0
    i = 0
    while p < len(part2):
        while p < len(part1):
            if ( part1[p] == s[p + p] ) and ( part2[p] == s[p+p + 1] ):
                p += 1
            else:
                return False
        if part2[p] == s[(p+p)-i]:
            i += 1
            p += 1
        else:
            return False
    return True
    
  
###########################

class MyTester:
    
    tests_passed = 0
    
    def __init__(self, func):
        self.func = func
        self._expected = None
        
    @property
    def expected(self):
        return self._expected 
    
    @expected.setter
    def expected(self, value):
        self._expected = value
    
    def evaluate(self, *args) -> bool:
        
        res = self.func(*args)
        
        if res == self.expected:
            MyTester.tests_passed += 1
        
        return res
        
    
def test_check_is_merge():
    
    test = MyTester(check_is_merge)
    test.expected = True
    
    assert test.expected == test.evaluate("codewars", "cdw", "oears")
        
        

if __name__ == "__main__":
    
    pytest.main()