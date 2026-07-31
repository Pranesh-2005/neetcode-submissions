class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(nums)):
            cmp = target-nums[i]
            if cmp in mp:
                return [mp[cmp],i]
            mp[nums[i]] = i
        return []
        