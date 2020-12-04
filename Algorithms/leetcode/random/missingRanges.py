"""
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
"""
from typing import List

get_min_max = lambda my_list : (min(my_list), max(my_list))

def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[str]:
    
    # find out missing numbers in nums
    if not nums:
        return list(str(lower))

    entire_range = range(lower, upper+1)
    missing_nums = []
    current_range = []

    for num in entire_range:
        if num not in nums:
            current_range.append(num)
        else:
            if len(current_range) > 1:
                _min, _max = get_min_max(current_range)
                missing_nums.append(f"{_min}->{_max}")
                current_range = []
            elif len(current_range) == 1:
                missing_nums.append(str(current_range[0]))
                current_range = []
    else:
        _min, _max = get_min_max(current_range)
        missing_nums.append(f"{_min}->{_max}")

    return missing_nums

inpt = [0,1,3,50,75]

print(findMissingRanges(inpt, 0, 99))




    