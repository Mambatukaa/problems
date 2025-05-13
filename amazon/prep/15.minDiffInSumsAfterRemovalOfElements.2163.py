""""
You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

The first n elements belonging to the first part and their sum is sumfirst.
The next n elements belonging to the second part and their sum is sumsecond.
The difference in sums of the two parts is denoted as sumfirst - sumsecond.

For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.

 

Example 1:

Input: nums = [3,1,2]
Output: -1
Explanation: Here, nums has 3 elements, so n = 1. 
Thus we have to remove 1 element from nums and divide the array into two equal parts.
- If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
- If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
- If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
The minimum difference between sums of the two parts is min(-1,1,2) = -1. 
Example 2:

Input: nums = [7,9,5,8,1,3]
Output: 1
Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
It can be shown that it is not possible to obtain a difference smaller than 1.
 

Constraints:

nums.length == 3 * n
1 <= n <= 105
1 <= nums[i] <= 105
"""

import heapq
import math

class Solution:
    def minimumDifference(self, A) -> int:
            n = len(A) // 3
            
            # Build pre_min using min-heap.
            pre_min, cur_min = [sum(A[:n])], sum(A[:n])
            pre_hp = [-x for x in A[:n]]
            heapq.heapify(pre_hp)
            for i in range(n, 2 * n):
                cur_pop = -heapq.heappop(pre_hp)
                cur_min -= cur_pop
                cur_min += min(cur_pop, A[i])
                pre_min.append(cur_min)
                heapq.heappush(pre_hp, -min(cur_pop, A[i]))          
            
            # Build suf_max.
            suf_max, cur_max = [sum(A[2*n:])], sum(A[2*n:])
            suf_hp = [x for x in A[2*n:]]
            heapq.heapify(suf_hp)

            for i in range(2 * n - 1, n - 1, -1):
                cur_pop = heapq.heappop(suf_hp)
                cur_max -= cur_pop
                cur_max += max(cur_pop, A[i])
                suf_max.append(cur_max)
                heapq.heappush(suf_hp, max(cur_pop, A[i]))
            suf_max = suf_max[::-1]


            print(pre_min)
            print(suf_max)
            
            # Iterate over pre_min and suf_max and get the minimum difference.
            ans = math.inf
            for a, b in zip(pre_min, suf_max):
                ans = min(ans, a - b)
            return ans 


from heapq import heapify, heappop, heappush
class Solution:
    def minimumDifference(self, nums) -> int:
        l = len(nums)
        n = l // 3

        # calc min sum of the first part 0 to n + 1


        max_heap = [-num for num in nums[:n]] 
        min_sum = sum(nums[:n])
        min_sum_arr = [min_sum]

        heapify(max_heap)

        for i in range(n, n * 2):
            max_el = -heappop(max_heap)
            min_sum -= max_el
            min_sum += min(max_el, nums[i])
            min_sum_arr.append(min_sum)

            heappush(max_heap, -min(max_el, nums[i]))


        min_heap = [num for num in nums[2 * n:]]
        max_sum = sum(nums[2 * n:])
        max_sum_arr = [max_sum]

        heapify(min_heap)

        for i in range(n * 2 - 1, n - 1, - 1):
            min_el = heappop(min_heap)

            max_sum -= min_el
            max_sum += max(min_el, nums[i])

            heappush(min_heap, max(min_el, nums[i]))

            max_sum_arr.append(max_sum)

            
        max_sum_arr.reverse()

        res = float('inf')


        for a, b in zip(min_sum_arr, max_sum_arr):
            res = min(a - b, res)

        return res
        
solution = Solution()

nums = [3, 5, 2, 2, 1, 7, 3, 6, 1]

print("res:", solution.minimumDifference(nums))
            
