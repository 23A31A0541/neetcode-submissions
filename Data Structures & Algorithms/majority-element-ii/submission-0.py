
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        renums = Counter(nums)
        for i,j in renums.items():
            if len(nums)<=1:
                res.append(i)
            elif j>(len(nums)//3) :
                res.append(i)
        return res