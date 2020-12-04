from typing import List

def shortestDistance(words: List[str], word1: str, word2: str) -> int:
    
    # get index of words
    word1_indexes = [i for i, word in enumerate(words) if word == word1]
    word2_indexes = [i for i, word in enumerate(words) if word == word2]

    # find min difference between
    if len(word1_indexes) < len(word2_indexes):
        min_distance = 999
        for i, index in enumerate(word2_indexes):
            dist = ( index - word1_indexes[i] )
            if dist < min_distance:
                min_distance = dist

    else:
        
    if _min == 0:
        return len(range(_min+1, _max))
    return len(range(_min, _max))




words = ["a","c","b","a"]
word1 = "a"
word2 = "b"

print(shortestDistance(words, word1, word2))

