class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mydict = {}

        l = mymax = 0

        for r in range(len(s)):
            if s[r] in mydict:
                l = max(mydict[s[r]] + 1, l)
            
            mydict[s[r]] = r 
            mymax = max(mymax, r - l+1)
        return mymax
            
