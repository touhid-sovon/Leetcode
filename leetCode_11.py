class Solution:
    def maxArea(self,height:list[int])->int:
        left,right = 0,len(height)-1
        max_area = 0
        while left < right:
            width = abs(right - left)
            height1 = min(height[left],height[right])
            # measuring the area of the elements
            max_area = max(max_area,(width*height1))
            # traversing
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area

sol = Solution()
print(sol.maxArea([1,1]))

