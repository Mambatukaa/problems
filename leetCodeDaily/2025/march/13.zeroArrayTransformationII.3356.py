""""
You are given an integer array nums of length n and a 2D array queries where queries (i] = [li, rio
valil.
Each queries [il represents the following action on nums :
• Decrement the value at each index in the range [li, ril in nums by at most vali.
• The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to O.
Return the minimum possible non-negative value of k, such that after processing the first k queries in
sequence, nums becomes a Zero Array. If no such k exists, return - 1.

Example 1:

    Input: nums = 12,0,21, queries = [[0,2,11,[0,2,11,[1,1,311
    Output: 2
    Explanation:
    • For i = 0 (1 = 0, r = 2, val = 1):
    • Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
    • The array will become [1, 0, 1].
    • For i = 1 (I = 0, r = 2, val = 1):
    • Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
    • The array will become 10, 0, 01, which is a Zero Array. Therefore, the minimum value of k is 2.




Example 2:
    Input: nums = [4,3,2,1], queries = [[1,3,2], [0,2,1]]
    Output: -1
    Explanation:
    • Fori= 0(1=1, r = 3, val = 2):
    • Decrement values at indices [1, 2, 3] by [2, 2, 11 respectively.
    • The array will become [4, 1, 0, 0].
    • For i= 1 (1=0, r = 2, val = 1):
    • Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
    • The array will become [3, 0, 0, 01, which is not a Zero Array.

Constraints:
• 1 < nums. length <= 105
• 0 < nums [i] <= 5 * 105
• 1 < queries. length <= 105
• queries [i]. length == 3
• 0 = li < ri < nums. length
• 1 = vali < 5
"""


class Solution:
    # TIME LIMIT EXCEEDED
    # Time Complexity: O(n * m) n nums[length] m: left to right
    # Space Complexity: O(1)
    def minZeroArray(self, nums, queries) -> int:
        ctr = 0
        zeroesCount = set()
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                zeroesCount.add(i)

        if len(zeroesCount) == n:
            return 0

        for query in queries:
            left, right, val = query
            ctr += 1

            for i in range(left, right + 1):
                nums[i] -= val


                if nums[i] <= 0 and i not in zeroesCount:
                    zeroesCount.add(i)
                
                if len(zeroesCount) == n:
                    return ctr

        return -1

class Solution:
    def minZeroArray(self, nums, queries) -> int:
        n = len(nums)
        left, right = 0, len(queries)

        # Zero array isn't formed after all queries are processed
        if not self.can_form_zero_array(nums, queries, right):
            return -1

        # Binary Search
        while left <= right:
            middle = left + (right - left) // 2
            if self.can_form_zero_array(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1

        # Return earliest query that zero array can be formed
        return left

    def can_form_zero_array(
        self, nums, queries, k: int
    ) -> bool:
        print("-----------------------")
        n = len(nums)
        total_sum = 0
        difference_array = [0] * (n + 1)

        # Process query
        for query_index in range(k):
            start, end, val = queries[query_index]

            # Process start and end of range
            difference_array[start] += val
            difference_array[end + 1] -= val

        print(difference_array)

        # Check if zero array can be formed
        for num_index in range(n):
            total_sum += difference_array[num_index]
            print("total_sum:", total_sum)
            if total_sum < nums[num_index]:
                return False
        return True
        

solution = Solution()

nums = [2,0,2]
queries = [[0,2,1],[0,2,1],[1,1,3]]
nums = [10, 8]
queries = [[0,1,5], [0,1,3], [0, 0, 2]]
print("res:", solution.minZeroArray(nums, queries))
