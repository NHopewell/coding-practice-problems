class TwoSum:


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.numbers.keys():
            self.numbers[number] = 1
        else:
            if self.numbers[number] < 2:
                self.numbers[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.numbers.keys():
            difference = value - num
            if difference in self.numbers:
                if difference != num:
                    return True
                else:
                    if self.numbers[difference] >= 2:
                        return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
