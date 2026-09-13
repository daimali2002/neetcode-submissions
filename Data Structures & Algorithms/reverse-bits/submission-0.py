class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        for i in range(32):
            if n & 1:
                num += 2**(31-i)
            n = n>>1
        return num  