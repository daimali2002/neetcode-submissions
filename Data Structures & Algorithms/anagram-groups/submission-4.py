class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        for mystr in strs:
            lis = [0] * 27
            for i in mystr:
                lis[ord(i.lower()) - 96] += 1
            mydict[tuple(lis)].append(mystr)
        return list(mydict.values())
