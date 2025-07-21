"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108







"""











class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]

        max_so_far = 0
        max_index = -1

        min_swap, max_swap = -1, - 1

        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] > max_so_far:
                max_so_far = digits[i]
                max_index = i
            elif digits[i] < max_so_far:
                max_swap = max_index
                min_swap = i

        # swap
        digits[min_swap], digits[max_swap] = digits[max_swap], digits[min_swap]


        return int("".join(map(str, digits)))

    

"""

1. Iterate through the backwards and track max_so_far
2. Swap the max_so_far with value which is less than max_so_far

"""


