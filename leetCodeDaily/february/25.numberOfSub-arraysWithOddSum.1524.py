""""

Given an array of integers arr, return the number of subarrays with an odd sum.
Since the answer can be very large, return it modulo 109 + 7.

Example 1:
    Input: arr = [1,3,5]
    Output: 4
    Explanation: All subarrays are [[1], [1,3], [1,3,51, [3], [3,5], [5]]
    All sub-arrays sum are [1,4,9,3,8,5].
    Odd sums are [1,9,3,5] so the answer is 4.

Example 2:
    Input: arr = [2,4,6]
    Output: 0
    Explanation: All subarrays are [[21,[2,41,[2,4,61, [41, [4,61, [6]]
    All sub-arrays sum are [2,6,12,4,10,6].
    All sub-arrays have even sum and the answer is 0.

Example 3:
    Input: arr = [1,2,3,4,5,6,71
    Output: 16




Constraints:
• 1 < arr.length <= 105
•1 <= arr［i］ <= 100

"""









class Solution:
    # TIME LIMIT EXCEEDED
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def numOfSubarrays(self, arr) -> int:
        n = len(arr)

        for i in range(1, n):
            arr[i] = arr[i - 1] + arr[i]


        res = 0

        for i in range(n):
            curr = arr[i]

            if curr % 2 == 1:
                res += 1

            for j in range(i):
                if (curr - arr[j]) % 2 == 1:
                    res += 1

        return res

    # Prefix sum odd and even counter
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def numOfSubarraysII(self, arr) -> int:
        MOD = 10 ** 9 + 7

        count = prefix_sum = 0

        odd_count = 0
        # even_count starts as 1 since the initial sum (0) is even
        even_count = 1

        for num in arr:
            prefix_sum += num

            # If current prefix sum is even, add the number of odd subarrays
            if prefix_sum % 2 == 0:
                count += odd_count
                even_count += 1
            else:
                # If current prefix sum is odd, add the number of even
                # subarrays
                count += even_count
                odd_count += 1

        return count % MOD


        
        
arr = [1, 2, 3, 4, 5, 6, 7]

solution = Solution()

print("res:", solution.numOfSubarraysII(arr))
