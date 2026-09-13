class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(n: int) -> int:
            num = 0
            while n > 0:
                if n & 1 :
                    num += 1
                n = n >> 1
            return num 
        lis = []
        for i in range(n+1):
            lis.append(hammingWeight(i))
        return lis
        