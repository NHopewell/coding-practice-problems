"""
https://www.codewars.com/kata/5508249a98b3234f420000fb/train/python

"""
from typing import List


def moving_shift(s: str, shift: int) -> List[str]:
    """
    moving_shift("I should have known that you would have a perfect answer for me!!!", 1)
    ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]
    """
    from string import ascii_lowercase, ascii_uppercase
    from collections import deque
    from math import floor
    
    encoded_msg = ""
    lower_to_check, upper_to_check = deque(ascii_lowercase), deque(ascii_uppercase)
    
    for letter in s:
        lower_to_check.rotate(shift * -1)
        upper_to_check.rotate(shift * -1)
        
        if letter in lower_to_check:
            index = ascii_lowercase.find(letter)
            if index != -1:
                encoded_msg += lower_to_check[index]
                #to_check.rotate(shift)
            else:
                encoded_msg += letter
        else:
            index = ascii_uppercase.find(letter)
            if index != -1:
                encoded_msg += upper_to_check[index]
                #to_check.rotate(shift)
            else:
                encoded_msg += letter
            
    num_messages = floor(len(encoded_msg) / 5) +1
    #remainder = len(encoded_msg) - (num_messages * 5)
    
    encoded_msg = [encoded_msg[i:i+num_messages] for i in range(0, len(encoded_msg), num_messages)]
        
    return encoded_msg



if __name__ == "__main__":
    
    msg = "I should have known that you would have a perfect answer for me!!!"
    shift = 1
    
    res = moving_shift(msg, shift)
    
    print(res)