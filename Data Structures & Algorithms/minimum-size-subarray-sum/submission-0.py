class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        tsum = 0
        minsum = float('inf')
        for r in range(len(nums)):
            tsum += nums[r]
            while tsum >= target:
                minsum = min(minsum,r-l+1)
                tsum -= nums[l]
                l += 1
        
        return 0 if minsum==float('inf') else minsum
            