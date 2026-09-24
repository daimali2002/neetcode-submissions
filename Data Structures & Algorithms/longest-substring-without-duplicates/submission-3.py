class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        l = my_max = 0
        myset.add(s[l])

        for r in range(1, len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[r])
            my_max = max(my_max, r - l + 1)
        return my_max