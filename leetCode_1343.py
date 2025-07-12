class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        L,R,count= 0,k-1,0
        n = len(arr)
        val = sum(arr[L:R+1])
        target = threshold * k
        while R<n:
            if L != 0:
                val = val + arr[R] - arr[L-1]

            if val >= target:
                count+=1
            L +=1
            R +=1
        return count

sol = Solution()
print(sol.numOfSubarrays([11,13,17,23,29,31,7,5,2,3],3,5))
