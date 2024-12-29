class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product=1
        for i in range(len(nums)):
            product*=nums[i]
        def signFunc(product):
            if product>0:
                return 1
            elif product<0:
                return -1
            else:
                return 0
        return signFunc(product)


        