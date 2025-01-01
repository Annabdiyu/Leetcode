class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ordered=sorted(heights)
        res=0
        for i in range(len(heights)):
            if heights[i]==ordered[i]:
                continue
            else:
                res+=1
        return res
        