class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0
        for num in st:
            if num - 1 not in st:
                cr = num
                while cr + 1 in st:
                    cr += 1
                res = max(res,cr-num+1)
        return res
        