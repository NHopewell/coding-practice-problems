"""
https://www.codewars.com/kata/590adadea658017d90000039/train/python

Slots.py
--------

Implement a basic slot machine class to simulate
playing slots with the following rules:


RULES:
======
    1. There are always exactly three reels

    2. Each reel has 10 different items.

    3. The three reel inputs may be different.

    4. The spin array represents the index of where the reels finish.

    5. The three spin inputs may be different

    6. Three of the same is worth more than two of the same

    7. Two of the same plus one "Wild" is double the score.

    8. No matching items returns 0.
    
    
"""


class Slots:
    
    
    
    options = [
        "Wild","Star","Bell","Shell","Seven",
        "Cherry","Bar","King","Queen","Jack"
    ]
    
    scores = {
        "Wild": {3: 100, 2: 10},
        "Star": {3: 90, 2: 9, 'bonus': 18},
        "Bell": {3: 80, 2: 8, 'bonus': 16},
        "Shell": {3: 70, 2: 7, 'bonus': 14},
        "Seven": {3: 60, 2: 6, 'bonus': 12},
        "Cherry": {3: 50, 2: 5, 'bonus': 10},
        "Bar": {3: 40, 2: 4, 'bonus': 8},
        "King": {3: 30, 2: 3, 'bonus': 6},
        "Queen": {3: 20, 2: 2, 'bonus': 4},
        "Jack": {3: 10, 2: 1, 'bonus': 2}
    }
    
    @staticmethod
    def spin():
        from random import choice
        from collections import Counter
        
        score = 0
        
        final_reel = [choice(Slots.options) for i in range(3)]
        counts = Counter(final_reel)
        
        if (len(counts) == 2) and ('Wild' in counts) and (counts['Wild'] == 1):
            non_wild = list(counts.keys())
            non_wild.remove('Wild')
            non_wild = non_wild[0]

            score += Slots.scores[non_wild]['bonus']

        else:
            
            for symbol, count in counts.items():
                if count in Slots.scores[symbol]:
                    score += Slots.scores[symbol][count]
        
        return (counts, score)
    
    
##############################

if __name__ == "__main__":
    
    for i in range(20):
        print(Slots.spin())   