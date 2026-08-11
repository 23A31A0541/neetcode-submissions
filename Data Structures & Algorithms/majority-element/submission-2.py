from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        z = 0
        ncount = Counter(nums)
        for i,j in ncount.items():
            if len(nums)<=1:
                return i
            elif j > len(nums)//2:
                z = i
        return z