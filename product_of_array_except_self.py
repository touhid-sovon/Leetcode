'''O(n) time complexity and O(n) space complexity'''

class Solution:
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        output = [1] * n
        j = n - 1
        # print("left,Right,Output:",left,right,output)
        for i in range(n):
            if i ==0:
                left[i] = nums[i]
            else:
                left[i] = left[i-1] * nums[i]
            if j == (n-1):
                right[j] = nums[j]
            else:
                right[j] = right[j+1] * nums[j]

            j = j-1

        for i in range(n):
            if i == 0:
                output[i] = right[i+1]
            elif i == (n-1) :
                output[i] = left[n-2]
            else:
                output[i] = left[i-1] * right[i+1]

        return output


# solution = Solution()
# print(solution.productExceptSelf([-1,1,0,-3,3]))

''' O(n) time complexity with less memory'''
class Solution:
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        n = len(nums)
        prefix = 1
        output = [1] * n

        for i in range(n):
            output[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1

        for i in range(n-1,-1,-1):
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]


        return output

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))


