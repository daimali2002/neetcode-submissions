class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        if not s:
            return 0
        l, my_max = 0, 1
        myset.add(s[l])

        for r in range(1, len(s)):
            if s[r] in myset:
                while s[r] in myset:
                    myset.remove(s[l])
                    l += 1
                myset.add(s[r])
            else:
                myset.add(s[r])
                my_max = max(my_max, r - l + 1)
                print(my_max, r, l)
        return my_max