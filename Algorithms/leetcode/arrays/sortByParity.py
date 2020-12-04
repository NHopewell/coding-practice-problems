"""
Add elements to array
add new array
remove
sory array by parity (even or odd first)
"""
import pytest
from typing import Optional, List


class ArraySorter:
    
    _total_elements_added = 0
    _total_elements_removed = 0
    
    def __init__(self, array: Optional[List[int]] = None):
        if array:
            self.array = array
        else:
            self.array = []
            
    def __repr__(self):
        return f"ArraySorter({self.array})"
    
    def __str__(self):
        return f"ArraySorter Object containing {self.__len__} elements"
    
    def __len__(self):
        return len(self.array)
    
    @classmethod
    def total_elements_added(cls):
        return cls._total_elements_added
    
    @classmethod
    def total_elements_removed(cls):
        return cls._total_elements_removed
    
    def add(self, element: int) -> None:
        ArraySorter._total_elements_added += 1
        self.array.append(element)
        
    def remove(self, element: int) -> None:
        ArraySorter._total_elements_removed += 1
        self.array.remove(element)
        
    def update(self, array: List[int]) -> None:
        
        assert(all(isinstance(i, int) for i in array)
              ), TypeError("Expected an array of integers.")
        self.array = array
        
    def sort(self, evens_first: Optional[bool] = True) -> None:
        evens = []
        odds = []
        
        for item in self.array:
            if item % 2 == 0:
                evens.append(item)
            else:
                odds.append(item)
                
        if evens_first:
            self.array = evens + odds
        else:
            self.array = odds + evens
        

class StringArraySorter(ArraySorter):
    
    def __init__(self, array: Optional[List[str]] = None):
        
        super().__init__(array)
        
    def update(self, array: List[int]) -> None:
        
        assert(all(isinstance(i, str) for i in array)
              ), TypeError("Expected an array of strings.")
        self.array = array
        
    def sort(self, method) -> None:
        
        if not callable(method):
            raise TypeError("Must pass a function to sort method")
            
        self.array = sorted(self.array, key=method)
        
    
    
    
####################################

def test_array_add_item():
    
    array_sorter = ArraySorter([1, 2, 3])
    array_sorter.add(4)
    
    expected = [1, 2, 3, 4]
    actual = array_sorter.array
    
    assert actual == expected
  

def test_array_remove_item():
    
    array_sorter = ArraySorter([1, 2, 3, 4])
    array_sorter.remove(4)
    
    expected = [1, 2, 3]
    actual = array_sorter.array
    
    assert actual == expected
    
def test_array_sort_evens_first():
    
    array_sorter = ArraySorter([1, 2, 3, 4])
    array_sorter.sort(evens_first=True)
    
    expected = [2, 4, 1, 3]
    actual = array_sorter.array
    
    assert actual == expected
    
    
def test_array_sort_odds_first():
    
    array_sorter = ArraySorter([1, 2, 3, 4])
    array_sorter.sort(evens_first=False)
    
    expected = [1, 3, 2, 4]
    actual = array_sorter.array
    
    assert actual == expected
    
def test_array_sort_update():
    
    array_sorter = ArraySorter()
    array_sorter.update([1, 2, 3, 4])
    
    expected = [1, 2, 3, 4]
    actual = array_sorter.array
    
    assert actual == expected
    
####################################

def test_string_sorter_add_item():
    
    array_sorter = StringArraySorter(["Able", "Marty", "Bob"])
    array_sorter.add("Wendy")
    
    expected = ["Able", "Marty", "Bob", "Wendy"]
    actual = array_sorter.array
    
    assert actual == expected
    
    
def test_string_sorter_sort_by_last_letter():
    
    array_sorter = StringArraySorter(["Able", "Marty", "Bob"])
    sort_by = lambda x: x[len(x)-1]
    array_sorter.sort(sort_by)
    
    expected = ["Bob","Able", "Marty"]
    actual = array_sorter.array
    
    assert actual == expected

    
def test_string_sort_by_length():
    
    array_sorter = StringArraySorter(["Able", "Marty", "Bob"])
    sort_by = lambda x: len(x)
    array_sorter.sort(sort_by)
    
    expected = ["Bob", "Able", "Marty"]
    actual = array_sorter.array
    
    assert actual == expected

    
if __name__ == "__main__":
    pytest.main()