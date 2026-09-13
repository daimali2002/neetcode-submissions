class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        l = 0
        ch = {}

        for r in range(len(s)):
            ch[s[r]] = ch.get(s[r],0) + 1
            if (r - l + 1) - max(ch.values()) <= k:
                maxlen = max(maxlen, r - l + 1)
            else:
                ch[s[l]] -= 1
                l += 1
        return maxlen
            
