class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for mystr in strs:
            lis = [0] * 27
            for i in mystr:
                lis[ord(i.lower()) - 95] += 1
            mydict[tuple(lis)] = mydict.get(tuple(lis),[]) + [mystr]
        return list(mydict.values())
