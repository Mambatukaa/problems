from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def maximumSum(self, nums) -> int:
        pairMap = defaultdict(list)

        def calc_digits_sum(num):
            res = 0

            while num > 0:
                res += num % 10
                num //= 10
                
            return res
    
        res = -1
        
        for num in nums:
            digits_sum = calc_digits_sum(num)

            heappush(pairMap[digits_sum], num)

            if len(pairMap[digits_sum]) > 2:
                heappop(pairMap[digits_sum])

            if len(pairMap[digits_sum]) == 2:
                res = max(res, pairMap[digits_sum][0] + (pairMap[digits_sum][1]))
            
        
        return res

    # Time Complexity: O(n * m)
    # Space Complexity: O(n * m)
    def maximumSumII(self, nums) -> int:
        pairMap = defaultdict(int)

        def calc_digits_sum(num):
            res = 0

            while num > 0:
                res += num % 10
                num //= 10
                
            return res
    
        res = -1
        
        for num in nums:
            digits_sum = calc_digits_sum(num)

            if digits_sum in pairMap:
                # second time
                res = max(res, pairMap[digits_sum] + num)

            pairMap[digits_sum] = max(num, pairMap[digits_sum])
        
        return res
        
nums = [18,43,36,13,7]
nums = [464, 482, 491]
solution = Solution()

print("res:", solution.maximumSum(nums))
print("res:", solution.maximumSumII(nums))
