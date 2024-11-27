class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res=0
        for cos in costs:
            if cos<=coins:
                res+=1
                coins-=cos
            else:
                return res
        return res
        
            
        
        