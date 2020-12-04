"""
Input: [3,[1,1],2,[1,3],[1,[2]]]
5 + 4 + 6 + 2 +6
Output: 25 
Explanation: Four 1's at depth 2, one 2 at depth 1.
"""

def check_depth(element, depth):

    _sum = 0
    while element:
        to_check = element.pop()
        if isinstance(to_check, list):
            _sum += check_depth(to_check, depth+1)
        else:
            _sum +=  (to_check * depth)
    return _sum

def depthSum(nestedList) -> int:

    if all(isinstance(i, int) for i in nestedList):
        return sum(nestedList)
    
    final_sum = 0
    for element in nestedList:
        if isinstance(element, list):
            final_sum += check_depth(element, 2)
        else:
            final_sum += element

    return final_sum


result = depthSum([3,[1,1],2,[1,3],[1,[2]]])
print(result)



        

    
        