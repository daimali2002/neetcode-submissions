class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""
        for i in strs:
            mystr += str(len(i)) + "#" + i
        return mystr

    def decode(self, s: str) -> List[str]:
        returnval = []
        before = 0
        for i, j in enumerate(s):
            if j == '#' and before.isdigit():
                returnval.append(s[i+1: i+int(before)+1])
            before = j
        return returnval
