class Solution:
    # def countKConstraintSubstrings(self, s: str, k: int) -> int:
    #     length = len(s)
    #     cnt = 0
    #     for i in range(length):
    #         count_0 = 0
    #         count_1 = 0
    #         for j in range(i,length):
    #             if s[j] == "1":
    #                 count_1 += 1
    #             if s[j] == "0":
    #                 count_0 += 1
    #             if count_1 <= k or count_0 <= k:
    #                 cnt += 1
    #     return cnt

    # one pass O(n)
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l = r = ans = zero = one = 0
        n = len(s)

        while r < n:
            if s[r] == "0":
                zero += 1
            else:
                one += 1

            while (zero > k and one > k):
                if s[l] == "0":
                    zero -= 1
                else:
                    one -= 1
                l += 1
            ans += (r-l)+1
            r += 1

        return ans


sol = Solution()
s = "10101"
print(sol.countKConstraintSubstrings(s,1))




