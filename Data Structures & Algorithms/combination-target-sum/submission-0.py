class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start,path,rem):
            if rem == 0:
                res.append(path[:])
                return
            for i in range(start,len(nums)):
                if nums[i] > rem:
                    continue
                path.append(nums[i])
                backtrack(i,path,rem-nums[i])
                path.pop()
        backtrack(0,[],target)
        return res
        