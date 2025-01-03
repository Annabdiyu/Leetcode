class Solution:
    def clearDigits(self, s: str) -> str:
        result=[]
        for val in s:
            if val.isdigit():
                if result:
                    result.pop()
            else:
                result.append(val)
        return "".join(result)


        
        