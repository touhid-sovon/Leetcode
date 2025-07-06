class Solution(object):
    def shuffle(self, nums: list, n: int) -> list:
        shuffled_nums = [0] * 2 * n
        l = i = 0
        r = n
        j = 1
        while  r < 2 * n:
            shuffled_nums[i] = nums[l]
            shuffled_nums[j] = nums[r]
            l += 1
            r += 1
            i += 2
            j += 2

        return shuffled_nums;


sol = Solution()

print(sol.shuffle([2,5,1,3,4,7],3))




