import math


def largest_in_rotated_array(nums:list[int])->int:
    left,right = 0, len(nums)-1
    while left<=right:
        #print(nums[left])
        mid =  math.ceil((left+right)/2)
        if nums[mid] > nums[left]:
            left = mid
        else:
            right = mid-1
    return nums[left]

print(largest_in_rotated_array([4,5,6,7,0,1,2]))



