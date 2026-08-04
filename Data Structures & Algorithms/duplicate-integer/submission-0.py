class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_map = {}
        for n in nums:
            h_map[n] = h_map.get(n,0)+1
        for a in h_map.values():
            if a>1:
                return True
        return False