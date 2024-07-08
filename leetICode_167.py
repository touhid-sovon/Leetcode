class Solution:
    def twoSum(self,numbers:list[int],target:int)-> list[int]:
        left,right = 0,len(numbers)-1

        while left<right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

sol = Solution()
print(sol.twoSum([2,7,9,11],9))
