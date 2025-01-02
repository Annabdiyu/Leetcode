class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result=0
        for ops in operations:
            if ops=="--X" or ops=="X--":
                result-=1
            elif ops=="X++" or ops=="++X":
                result+=1
        return result
                
        