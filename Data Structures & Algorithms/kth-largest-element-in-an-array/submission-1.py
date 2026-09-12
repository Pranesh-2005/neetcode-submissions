class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        l,r = 0,len(nums) - 1
        while l<=r:
            pivot = nums[(l+(r-l) // 2)]
            low,mid,high =l,l,r
            while mid <= high:
                if nums[mid] < pivot:
                    nums[low],nums[mid] = nums[mid],nums[low]
                    low+=1
                    mid+=1
                elif nums[mid] == pivot:
                    mid += 1
                else:
                    nums[mid],nums[high] = nums[high],nums[mid]
                    high -= 1
            if target < low:
                r = low - 1
            elif target > high:
                l = high + 1
            else:
                return nums[target]
                
        