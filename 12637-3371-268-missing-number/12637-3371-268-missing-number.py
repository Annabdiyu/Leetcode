class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        
        n = len(nums)
        if nums[-1] != n:
            return n
        
        for i in range(nums[0], nums[-1] + 1):
            if i not in nums:
                return i

        
        