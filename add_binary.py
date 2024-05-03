class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len1,len2 = len(a),len(b)
        n = max(len1,len2)
        if len1 > len2:
            b = b[::-1]
            for i in range(len1-len2):
                b = b + '0'
            b = b[::-1]
        if len2 > len1:
            a = a[::-1]
            for i in range(len2-len1):
                a = a + '0'
            a = a[::-1]
        sum = ""
        carry = "0"


        for i in range(n-1,-1,-1):
            if carry == '0':
                if a[i] == '1' and b[i] == '1':
                    sum = sum + "0"
                    carry = "1"
                elif a[i] == '1' or b[i] == '1':
                    sum = sum + '1'
                else:
                    sum = sum + '0'
            elif carry == '1':
                if a[i] == '1' and b[i] == '1':
                    sum = sum + "1"
                    carry = "1"
                elif a[i] == '1' or b[i] == '1':
                    sum = sum + '0'
                    carry = '1'
                else:
                    sum = sum + '1'
                    carry = '0'

        if carry == '1':
            sum = sum + carry


        return sum[::-1]

sol = Solution()

print(sol.addBinary('100','110010'))

