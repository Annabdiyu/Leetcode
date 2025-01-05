class Solution:
    def removeStars(self, s: str) -> str:
        result=[]
        for i in range(len(s)):
            if s[i]!='*':
                result.append(s[i])
            else:
                result.pop()
        return "".join(result)