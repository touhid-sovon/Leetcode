class Solution:
    def permutation(self,nums:list[int]) -> list[list[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permutation(nums)

            for perm in perms:
                nums.append(n)
            res.extend(perms)

        return res
