class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.window = []
        

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.window.append(val)
            
        else:
            self.window = self.window[1:]
            self.window.append(val)
        
        return sum(self.window) / len(self.window)