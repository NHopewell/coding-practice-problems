"""
https://leetcode.com/problems/rotate-image/
"""
import pytest
from typing import List

Matrix = List[List[int]]

def rotate(matrix: Matrix) -> Matrix:
    
    original_len = len(matrix)
    for i in range(original_len):
        
        matrix.append([])
        for j in range(original_len):
            matrix[-1].append(matrix[j][i])
        matrix[-1] = matrix[-1][::-1]
            
    matrix = matrix[original_len:]
    
    return matrix

################################################

def test_rotate_case_one():
    
    in_ = [[1,2,3],[4,5,6],[7,8,9]]
    
    expected = [[7,4,1],[8,5,2],[9,6,3]]
    actual = rotate(in_)
    
    assert actual == expected
    
    
def test_rotate_case_two():
    
    in_ = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    
    expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    actual = rotate(in_)
    
    assert actual == expected


if __name__ == "__main__":
    
    pytest.main()
        