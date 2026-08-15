class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr)//2
            i = 0
            j = 0
            left = merge(arr[:mid])
            right = merge(arr[mid:])
            res = []

            while i<len(left) and j<len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            while i<len(left):
                res.append(left[i])
                i += 1
            while j<len(right):
                res.append(right[j])
                j += 1
            return res
        return merge(nums)