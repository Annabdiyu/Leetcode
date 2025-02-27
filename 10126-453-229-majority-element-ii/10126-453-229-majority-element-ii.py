from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        count=defaultdict(int)
        occurence=len(nums)/3
        result=[]
        for i in nums:
            count[i]+=1
            if count[i]>occurence and i not in result:
                result.append(i)
        return result

        
        