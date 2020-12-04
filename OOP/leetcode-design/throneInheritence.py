"""
throneInheritance.py
--------------------

https://leetcode.com/problems/throne-inheritance/
"""
import pytest
from collections import defaultdict
from typing import List

class ThroneInheritance:
    
    def __init__(self, king: str):
        
        self.king = king
        self.order: List[str] = [king]
        self.num_offspring = defaultdict(int)
        
    def birth(self, parent: str, child: str) -> None:
        
        if len(self.order) == 1:
            self.order.append(child)
            self.num_offspring[self.king] += 1
        else:
            parent_index = self.order.index(parent) + (self.num_offspring[parent] + 1)
            self.order.insert(parent_index, child)
            self.num_offspring[parent] += 1
        
    def death(self, person: str) -> None:
        
        self.order.remove(person)
        
        
    def get_inheritence_order(self) -> List[str]:
        
        return self.order
        
        
        
############################

def test_throne_linear_births():
    
    #setup
    throne = ThroneInheritance("King")
    
    throne.birth("King", "Daniel")
    throne.birth("King", "John")
    throne.birth("King", "Mary")
    
    print(throne.num_offspring)
        
    expected = ["King", "Daniel", "John", "Mary"]
    actual = throne.get_inheritence_order()
    
    assert actual == expected
    
def test_throne_non_linear_births():
    
    #setup
    throne = ThroneInheritance("King")
    
    throne.birth("King", "Daniel")
    throne.birth("King", "John")
    throne.birth("King", "Mary")
    
    throne.birth("Daniel", "Catherine")
        
    expected = ["King", "Daniel", "Catherine", "John", "Mary"]
    actual = throne.get_inheritence_order()
    
    assert actual == expected


def test_throne_death():

    #setup
    throne = ThroneInheritance("King")
    
    throne.birth("King", "Daniel")
    throne.birth("King", "John")
    throne.birth("King", "Mary")
    
    throne.birth("Daniel", "Catherine")
    throne.death("John")
        
    expected = ["King", "Daniel", "Catherine", "Mary"]
    actual = throne.get_inheritence_order()
    
    assert actual == expected

    
    
if __name__ == "__main__":
    
    pytest.main()