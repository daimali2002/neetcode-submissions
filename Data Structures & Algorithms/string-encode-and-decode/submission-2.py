class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string = string + "å" + i
        string += "å"
        return string
    def decode(self, s: str) -> List[str]:
        word = ""
        arr = []
        for i in range(len(list(s))):
            if list(s)[i] == "å":
                arr.append(word)
                word = ""
            else:
                word += list(s)[i]
        return arr[1:]

