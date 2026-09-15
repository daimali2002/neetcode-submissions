class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for mystr in strs:
            lis = [0] * 26
            for i in mystr:
                lis[ord(i.lower()) - 96] += 1
            mydict[tuple(lis)] = mydict.get(tuple(lis),[]) + [mystr]
        return list(mydict.values())
