class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result=[]
        for word in words:
            result.extend(word.split(separator))
        return [x for x in result if x!='']
        