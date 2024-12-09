class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        min_length=float('inf')
        l=0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                min_length=min(min_length,r-l+1)
                sum-=nums[l]
                l+=1
        return min_length if min_length<float('inf') else 0

        
        
        