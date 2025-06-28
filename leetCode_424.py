# class Solution:
#     def characterReplacement(self,s,k):
#         l = r = buffer = count = max_val = 0
#         length = len(s)
#         while (l < length):
#             if (r < len(s)):
#                 if (s[l] == s[r]):
#                     r += 1
#                     count += 1
#                 else:
#                     if(buffer != k):
#                         buffer += 1
#                         r += 1
#                         count += 1
#                         #print(f'Buffer = {buffer} and K = {k}')
#                     else:
#                         l += 1
#                         r = l
#                         count = buffer = 0
#                         #print("L updation")
#                 max_val = max(max_val,count)
#                 if (r == length):
#                     break
#                 #print(f'L = {l}, R= {r},count = {count},Max_val = {max_val}')
#         return max_val

class Solution:
    def characterReplacement(self,s:str,k:int) -> int:
        count = {}
        l = max_freq = res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            max_freq = max(max_freq,count[s[r]])
            while (r-l+1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)

        return res

sol = Solution()

print(sol.characterReplacement("AABABBA",1))
