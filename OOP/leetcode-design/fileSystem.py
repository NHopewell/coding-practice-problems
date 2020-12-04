"""
Design a file system
--------------------

https://leetcode.com/problems/design-file-system/

"""
import pytest

class Path:
    
    def __init__(self, path: str, value: int):
        
        self.path = path
        self.value = value
        
    def __repr__(self):
        
        return f"{self.path} : {self.value}"
    
    
class FileSystem:
    
    def __init__(self):
        
        self.files = {}
        
    def _check_path(self, path: str) -> bool:
        
        if path:
            if path[0] == '/':
                return True
        return False
    
    def _check_parents(self, path: str) -> bool:
        
        depth = path.count('/')
        if depth > 1:
            parents = path.split('/')[1:-1]
            for parent in parents:
                if f"/{parent}" not in self.files.keys():
                    return False
        return True
        
        
    
    def add_path(self, path: str, value: int) -> bool:
        
        if self._check_path(path):
            if self._check_parents(path):
                self.files[path] = value
                return True
            
        return False
    
    def get(self, path: str) -> int:
        
        return self.files.get(path, False)
    
    
    
########################################################

def test_file_system_case_one():
    
    filesystem = FileSystem()
    filesystem.add_path("/shopify", 1)
    filesystem.add_path("/shopify/peopleAnalytics", 20)
    
    print(filesystem.files)
    
    test_case_one = "/shopify/peopleAnalytics"
    
    expected = 20
    actual = filesystem.get(test_case_one)
    
    assert actual == expected
    
    
def test_file_system_case_two():
    
    filesystem = FileSystem()
    
    test_case_two = "/shopify/peopleAnalytics"
    
    actual = filesystem.add_path(test_case_two, 20)
    
    expected = False
    
    assert actual == expected
    
    
    
if __name__ == "__main__":
    
    pytest.main()
    