class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = {}
        for i in strs:
            if "".join(sorted(list(i))) not in lists:
                lists["".join(sorted(list(i)))] = [i]
            else:
                lists["".join(sorted(list(i)))].append(i)
        return lists.values()
