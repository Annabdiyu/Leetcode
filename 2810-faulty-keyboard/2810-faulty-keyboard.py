class Solution:
    def finalString(self, s: str) -> str:
        coll=[]
        for i in s:
            if i=='i':
                coll=coll[::-1]
            else:
                coll.append(i)
        return ''.join(coll)