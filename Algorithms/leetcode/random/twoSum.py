class Solution:
    """
    [ 3, 5, 6, 2, 5, 8, 9, 3, 4, 6, 1 ]
    
    target = 12
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup = {}
        
        for i, num in enumerate(nums):
            difference = (target - num)
            if difference in lookup.keys():
                return [i, lookup[difference]]
            else:
                lookup[num] = i


