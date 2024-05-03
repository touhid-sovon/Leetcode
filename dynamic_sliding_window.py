def dynamic_sliding_window(arr:list[int],target)-> int:
    currentSum = 0
    start = 0
    end = 0
    min_length =[]
    while end <  len(arr):
        currentSum = sum(arr[:end])
        end += 1
        while start < end and currentSum >= target:
            currentSum = currentSum - arr[start]
            start += 1

            min_length.append((end-start+1))

    return min(min_length)

print(dynamic_sliding_window([1,2,3,4,5,6],7))