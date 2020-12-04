from math import floor

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.numbers = []
        

    def addNum(self, num: int) -> None:
        self.numbers.append(num)
        

    def findMedian(self) -> float:
        self.numbers.sort()
        if len(self.numbers) % 2 != 0:
            return self.numbers[floor(len(self.numbers)/2)]
        else:
            second = int(len(self.numbers)/2)
            first = second - 1
            median = (self.numbers[first] + self.numbers[second]) / 2
            
            return median
            