class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicti = {"(": ")","{": "}","[": "]" }

        for i in s:
            if i in dicti.keys():
                stack.append(i)
            elif (len(stack) == 0 or i != dicti[stack[-1]]):
                return False
            else:
                stack.pop()
        return len(stack) == 0
        