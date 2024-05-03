# sliding window algorithm for finding subarray problems
# find the maximum value by summing the indexes where maximum index could be 'k'

def fixed_sliding_window(arr:list[int],k:int)-> list[int]:
    currentSum = sum(arr[:k])
    result = [currentSum]
    for i in range(len(arr)-k):
        currentSum = currentSum - arr[i] + arr[i+k]

        result.append(currentSum)
        # if currentSum > result:
        #     result = currentSum

    return result

print(fixed_sliding_window([1,2,3,4,5,6,7],3))
