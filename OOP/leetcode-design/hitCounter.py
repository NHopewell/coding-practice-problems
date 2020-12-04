"""
hitcounter.py
=============

https://leetcode.com/problems/design-hit-counter/


"""
import pytest
from collections import defaultdict

class HitCounter:
    
    seconds_in_past_5_minutes = 300
    
    def __init__(self):
        self.hits = defaultdict(int)
    
    
    def get_hit(self, timestamp: int) -> None:
        
        self.hits[timestamp] += 1
        
        
    def get_hits(self, timestamp: int) -> int:
        
        """
        301
        """
        total_hits = 0
        
        counter = timestamp - HitCounter.seconds_in_past_5_minutes
        
        if counter > 0:
            for timestamp in range((timestamp - HitCounter.seconds_in_past_5_minutes) + 1, timestamp):
                if timestamp in self.hits:
                    total_hits += self.hits[timestamp]
        else:
            for timestamp in self.hits:
                total_hits += self.hits[timestamp]
                
                
        return total_hits
    
    
    
    
################################################

def test_hit_counter_case_one():
    
    counter = HitCounter()
    counter.get_hit(1)
    counter.get_hit(2)
    counter.get_hit(3)
    
    expected = 3
    actual = counter.get_hits(4)
    
    assert actual == expected
    
    
def test_hit_counter_case_two():
    
    counter = HitCounter()
    counter.get_hit(1)
    counter.get_hit(2)
    counter.get_hit(3)
    
    counter.get_hit(300)
    
    expected = 4
    actual = counter.get_hits(300)
    
    assert actual == expected
    
def test_hit_counter_case_three():
    
    counter = HitCounter()
    counter.get_hit(1)
    counter.get_hit(2)
    counter.get_hit(3)
    
    counter.get_hit(300)
    
    expected = 3
    actual = counter.get_hits(301)
    
    assert actual == expected
    
    
if __name__ == "__main__":
    pytest.main()

