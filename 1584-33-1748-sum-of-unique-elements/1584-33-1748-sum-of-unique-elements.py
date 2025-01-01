class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result = []  
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1 and nums[i] not in result:
                result.append(nums[i])
        res = sum(result)
        return res
        