class Solution:
    ''' My Solution'''
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0] * (n+2)
        sum = 0
        for i,num in enumerate(nums):
            sum += num
            prefix[i+1] = sum

        for i in range(1,len(prefix)-1):
            if prefix[i-1] == (prefix[n] - prefix[i]):
                return i-1

        return -1

class Solution:
    ''' Optimal Solution'''
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i,num in enumerate(nums):
            if left_sum == total-left_sum -x :
                return i
            left_sum+=num
        return -1







sol = Solution()

#print(sol.pivotIndex([1, 7, 3,6, 5,6]))
print(sol.pivotIndex([1,-1,2]))

