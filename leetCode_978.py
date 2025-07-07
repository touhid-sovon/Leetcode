class Solution():
    def maxTurbulenceSize(self, arr):
        def cmp(a,b):
            if a < b:
                return -1
            elif a>b:
                return 1
            return 0

        n = len(arr)
        if n < 2:
            return n

        L = 0
        max_len = 1

        for R in range(1,n):
            c = cmp(arr[R-1],arr[R])
            if c == 0:
                L = R
            elif R == n - 1 or c * cmp(arr[R],arr[R+1]) != -1:
                max_len = max(max_len,R-L+1)
                L = R

        if max_len == 1:
            return -1


sol = Solution()

# print(sol.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
print(sol.maxTurbulenceSize([2,3,4,3,4]))

