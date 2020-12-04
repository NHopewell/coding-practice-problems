"""
phoneDirectory.py
-----------------

https://www.codewars.com/kata/56baeae7022c16dd7400086e/train/python
"""
import pytest


def _reduce_string(string: str, slice_start: int, slice_end :int) -> str:
    
    reduced = ""
    for i, char in enumerate(string):
        if i not in range(slice_start-1, slice_end+1):
            reduced += char
    return reduced

def phone(string: str, number: str) -> str:
    
    lines = string.split("\n")
    for line in lines:
        if number in line:
            name_start, name_end = line.index("<"), line.index(">")
            name = line[name_start+1:name_end]
            reduced = _reduce_string(line, name_start, name_end)
            
            number_start, number_end = reduced.index("+"), reduced.index("+") + len(number)+1
            number = reduced[number_start+1:number_end]
            reduced = _reduce_string(reduced, number_start, number_end)
            
            for char in reduced:
                try:
                    int(char)
                    address_start, address_end = reduced.index(char), reduced.index(".")+1
                    address = reduced[address_start: address_end]
                    
                    return f"Phone => {number}, Name => {name}, Address => {address}"
                except:
                    pass
    
    
    

########################################
def test_phone_case_one():
    
    test_case = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
    number = "1-541-754-3010"
    
    expected = "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
    actual = phone(test_case, number)
    
    assert actual == expected
    
    
if __name__ == "__main__":
    
        
    test_case = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
    number = "1-541-914-3010"
    
    #expected = "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
    actual = phone(test_case, number)
    
    print(actual)
    
    
    #pytest.main()