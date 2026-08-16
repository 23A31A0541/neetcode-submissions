class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums = set(nums)
        long = 0

        for num in s_nums:

            if num-1 not in  s_nums:
                count = 1
                current = num

                while current+1 in s_nums:
                    count += 1
                    current += 1
                long = max(long,count)
        return long