class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        for mystr in strs:
            lis = [0] * 26
            for i in mystr:
                lis[ord(i) - 97] += 1
            mydict[tuple(lis)].append(mystr)
        return list(mydict.values())
