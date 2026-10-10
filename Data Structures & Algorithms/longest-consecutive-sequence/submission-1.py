class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0
        for num in st:
            if num - 1 not in st:
                cur = num
                while cur+1 in st:
                    cur += 1
                res = max(res,cur-num+1)
        return res