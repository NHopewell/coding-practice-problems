# https://leetcode.com/problems/design-add-and-search-words-data-structure/

"""
class that stores words

adds words

searches if words exist

if word hae '.' can match any character

"""
import pytest

class WordDictionary:
    
    def __init__(self):
        
        self.words = set()
    
    
    def add(self, word: str) -> None:
        
        self.words.add(word)
        
        
    def search(self, word: str) -> None:
        
        if '.' in word:
            num_periods = word.count('.')
            list_word = list(word)
            for i in range(0, num_periods):
                list_word.remove('.')
            word = "".join(list_word)
            
            for entry in self.words:
                if word in entry:
                    
                    return True
                
        return word in self.words
        
    

    
###################################

def test_search_true():
    word_dict = WordDictionary()
    
    words_to_add = ["bad", "dad", "mad"]
    
    for word in words_to_add:
        word_dict.add(word)
      
    expected = True
    actual = word_dict.search("bad")
    
    assert actual == expected
    

def test_search_true_with_periods():
    word_dict = WordDictionary()
    
    words_to_add = ["bad", "dad", "mad"]
    
    for word in words_to_add:
        word_dict.add(word)
      
    expected = True
    actual = word_dict.search(".ad")
    
    assert actual == expected
    
    
def test_search_false():
    
    word_dict = WordDictionary()
    
    words_to_add = ["bad", "dad", "mad"]
    
    for word in words_to_add:
        word_dict.add(word)
    
        
    expected = False
    actual = word_dict.search("pad")
    
    assert actual == expected
    
    
if __name__ == "__main__":

        
    pytest.main()
    