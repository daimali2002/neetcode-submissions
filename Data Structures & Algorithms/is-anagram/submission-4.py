class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_a = dict()
        dict_b = dict()

        for i in s:
            dict_a[i] = dict_a.get(i,0) + 1
        for j in t:
            dict_b[j] = dict_b.get(j,0) + 1
        
        return dict_a == dict_b
        
        