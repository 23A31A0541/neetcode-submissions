from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        res = sorted(count, key=lambda x: count[x],reverse = True)
        return res[:k]