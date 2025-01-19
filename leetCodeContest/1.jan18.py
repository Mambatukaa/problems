

# easy
def maxa(nums):
    res = abs(nums[-1] - nums[0])

    for i in range(1, len(nums)):
        diff = abs(nums[i] - (nums[i-1]))
        res = max(diff, res)

    return res


print("Res:", maxa([1, 2, 4]))


# 
def minCost(arr, brr, k):
    def calc(arr, brr):
        print("a:", arr)
        print("b:", brr)
        res = sum(abs(x - y) for x, y in zip(arr, brr))

        print(res)
        print("--------------")
        return res
    
    res = calc(arr, brr)

    arr.sort()
    brr.sort()

    res = min(res, calc(arr, brr) + k)

    return res

arr = [6, 1, 10]
brr = [8, 10, -3]
k = 4


print("res:", minCost(arr, brr, k))
