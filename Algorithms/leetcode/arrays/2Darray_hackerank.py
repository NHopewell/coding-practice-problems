# https://www.hackerrank.com/challenges/2d-array/problem

from typing import List
from random import choice
import pytest

def make_2d_array_of_zeroes(rows: int, cols: int, max: int) -> List[List[str]]:
    
    msg = "The smallest size valid matrix is 3x3."
    assert((cols >= 3) and (rows >=3)), ValueError(msg)

    return [[choice(range((max+1)*-1, max+1)) for i in range(rows)] for j in range(cols)]


def calc_hourglass(matrix, row_indexes, col_indexes) -> int:
                return (
                        ( 
                            matrix[col_indexes[0]][row_indexes[0]] +  
                            matrix[col_indexes[0]][row_indexes[1]] +  
                            matrix[col_indexes[0]][row_indexes[2]]

                        ) +
                        ( 
                            matrix[col_indexes[1]][row_indexes[1]] 
                        ) +
                        (
                            matrix[col_indexes[2]][row_indexes[0]] + 
                            matrix[col_indexes[2]][row_indexes[1]] + 
                            matrix[col_indexes[2]][row_indexes[2]]

                        )

                )
    

def get_largest_hourglass(matrix: List[List[str]]) -> int:
    
    num_right_shifts = len(matrix[0]) - 3
    num_down_shifts = len(matrix) - 3
    
    row_indexes = [0, 1, 2]
    col_indexes = [0, 1, 2]
    
    hour_glass_sums = set()
    
    if num_down_shifts:
        for i in range(num_down_shifts+1):
            while num_right_shifts:
                
                current_sum = calc_hourglass(matrix, row_indexes, col_indexes)
                
                hour_glass_sums.add(current_sum)
                
                num_right_shifts -= 1
                col_indexes = [col + 1 for col in col_indexes]
                
            row_indexes = [row + 1 for row in row_indexes]
            
    elif num_right_shifts:
        for i in range(num_right_shifts+1):
                
            current_sum = calc_hourglass(matrix, row_indexes, col_indexes)

            hour_glass_sums.add(current_sum)

            col_indexes = [[index + 1] for _list in col_indexes for index in _list]
            
    else:
        current_sum = calc_hourglass(matrix, row_indexes, col_indexes)


        hour_glass_sums.add(current_sum)
        
    return max(hour_glass_sums)


class NicksTester:
    
    def __init__(self, func):
        
        self.func = func
        
        
    @property
    def expected(self):
        return self._expected
    
    @expected.setter
    def expected(self, new):
        
        self._expected = new
        
    def eval(self, *args):
        
        return self.expected == self.func(*args)
    
    
def test_hourglass():
    
    to_test = [[-4, -4, -3, -4], [-2, 0, -4, -3], [-4, -4, 3, -2], [-1, 0, -2, -1]]
    
    tester = NicksTester(get_largest_hourglass)
    tester.expected = -16
    
    actual = tester.eval(to_test)
    expected = True
    
    assert actual == expected
        
    

########################################

if __name__ == "__main__":
    pytest.main()
                        