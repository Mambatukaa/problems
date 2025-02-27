""""

A sequence X1, X2, ..., Xn is Fibonacci-like if:
• n >= 3
• Xi + Xi+1 == Xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like
subsequence of arr. If one does not exist, return 0.
A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr,
without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 81.

Example 1:
    Input: arr = [1,2,3,4,5,6,7,8]
    Output: 5
    Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

Example 2:
    Input: arr = [1,3,7,11,12,14,181
Output: 3
    Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or
    [7,11,18]•



Constraints:
• 3 < arr.length <= 1000
• 1 < arr[i] < arr[i + 1] < 10^9

"""

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        # Store array elements in set for O(1) lookup
        num_set = set(arr)
        max_len = 0
        n = len(arr)

        # Try all possible first two numbers of sequence
        for start in range(n):
            for next in range(start + 1, n):
                # Start with first two numbers
                prev = arr[next]
                curr = arr[start] + arr[next]
                curr_len = 2

                # Keep finding next Fibonacci number
                while curr in num_set:
                    prev, curr = curr, curr + prev
                    curr_len += 1
                    max_len = max(max_len, curr_len)

        return max_len  
