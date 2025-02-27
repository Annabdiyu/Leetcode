from collections import defaultdict
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        count=defaultdict(int)
        for i in nums:
            count[i]+=1
        result=0
        for key,values in count.items():
            if key%2==0:
                result=max(result,values)
        for key,values in count.items():
            if values==result and key%2==0:
                return key
        return -1
        