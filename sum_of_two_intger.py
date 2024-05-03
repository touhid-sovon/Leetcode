class Solution:
    def getSum(self, a: int, b: int) -> int:
        # general solution for java and pyhton
        '''
        while (b != 0):
            temp = (a & b)<<1
            a = a ^ b
            b = temp
        return a
        '''
        # solution for python
        bit_shortener = 0xffffffff

        while (b & bit_shortener) > 0:
            temp = (a & b)<<1
            a = a ^ b
            b = temp

        return (a & bit_shortener) if b > 0 else a

