class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for res in nums1:
            if res in nums2 and res not in result:
                result.append(res)
        return result
        