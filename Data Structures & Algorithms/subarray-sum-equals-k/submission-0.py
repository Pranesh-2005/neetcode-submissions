class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        count,prefix = 0,0
        for i in range(len(nums)):
            prefix += nums[i]
            count += mp[prefix-k]
            mp[prefix] += 1
        return count