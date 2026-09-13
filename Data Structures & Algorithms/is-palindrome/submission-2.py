class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for i in list(s):
            if i.isalnum():
                newstr+=i.lower()
        return newstr == newstr[::-1]
        