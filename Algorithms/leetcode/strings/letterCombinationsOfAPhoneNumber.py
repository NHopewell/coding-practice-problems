"""
return all possible letter combinations when given string of digits

Example
-------
    Input: "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
    
    Input: digits = "2"
    Output: ["a","b","c"]

"""
import pytest
from typing import List
import math

def get_letter_combinations(digits: str) -> List[str]:
    
    numbers = '2 3 4 5 6 7 8 9'.split()
    
    letters = [list('abc'), list('def'), list('ghi'), 
               list('jkl'), list('mno'), list('pqrs'),
               list('tuv'), list('wxyz')]

    phone_map = {k: v for (k,v) in zip(numbers, letters)}
    
    #length = math.prod([len(phone_map[digit]) for digit in digits])
    
    combinations = []
    
    if len(digits) == 1:
        return list(phone_map[digits])
    
    for first_letter in phone_map[digits[0]]:
        for second_letter in phone_map[digits[1]]:
            to_append = f"{first_letter}{second_letter}"
            combinations.append(to_append)
            
            
    return combinations
        
            
    

    
############################

def test_get_letter_combinations_one():
    
    expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    actual = get_letter_combinations("23")
    
    assert actual == expected
    
    
def test_get_letter_combinations_two():
    
    expected = ["a","b","c"]
    actual = get_letter_combinations("2")
    
    assert actual == expected
    

if __name__ == "__main__":
    pytest.main()
    #get_letter_combinations("23")
    
