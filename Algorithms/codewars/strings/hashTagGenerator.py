"""
Given a string, create a hashtag from it

"""
import pytest

class HashTagGenerator:
    
    def __init__(self, string: str):
        self.string = string

    def make_title_case(self):
        self.string = "".join([word.title() for word in self.string.split()])
    
    def make_hashtag(self):
        
        if not self.string: 
            self.string = False
        else:
            self.string = f"#{self.string}"


def test_hash_tag_generator_case_one():
    
    to_hash_tag = " Hello there thanks for trying my Kata"
    
    generator = HashTagGenerator(to_hash_tag)
    generator.make_title_case()
    generator.make_hashtag()
    
    expected = "#HelloThereThanksForTryingMyKata"
    actual = generator.string
    
    assert actual == expected
    
    
def test_hash_tag_generator_case_two():
    
    to_hash_tag = "     Hello      world " 
    
    generator = HashTagGenerator(to_hash_tag)
    generator.make_title_case()
    generator.make_hashtag()
    
    expected = "#HelloWorld"
    actual = generator.string
    
    assert actual == expected
    
    
def test_hash_tag_generator_case_three():
    
    to_hash_tag = ""
    
    generator = HashTagGenerator(to_hash_tag)
    generator.make_title_case()
    generator.make_hashtag()
    
    expected = False
    actual = generator.string
    
    assert actual == expected

    
if __name__ == "__main__":
    pytest.main()