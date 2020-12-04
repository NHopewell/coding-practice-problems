"""
josephus_survivor(7,3) => means 7 people in a circle;

one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor!

"""
import pytest
from typing import List
from collections import deque

def find_josephus_survivor(people_in_circle: int, steps: int) -> List[int]:
    
    people_in_circle = deque(range(1, people_in_circle+1))
    steps = (steps -1) * -1
    
    while len(people_in_circle) > 1:
        
        people_in_circle.rotate(steps)
        people_in_circle.popleft()
        
    return list(people_in_circle)

    
#####################################################################

def test_find_josephus_survivor_7_3():
    
    expected = [4]
    actual = find_josephus_survivor(7,3)
    
    assert actual == expected
    
if __name__ == "__main__":
    pytest.main()