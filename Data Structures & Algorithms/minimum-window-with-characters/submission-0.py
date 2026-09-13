class Solution:
    def minWindow(self, s: str, t: str) -> str:
        retarr = []
        l = 0

        def valid(s,t):
            k = list(t)
            for i in s:
                if i in k:
                    k.remove(i)
            return len(k) == 0

        for r in range(len(s)):
            if s[r] in set(t) and valid(s[l:r+1],t):
                retarr.append(s[l:r+1])
                while valid(s[l+1:r+1],t) and l <= r:
                    retarr.append(s[l+1:r+1])
                    l += 1
        if not retarr:
            return ""
        return min(retarr,key = len)

                
