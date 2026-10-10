class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res,path = [],[]
        def backtrack():
            if len(path) == n:
                res.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack()
                    path.pop()
        backtrack()
        return res