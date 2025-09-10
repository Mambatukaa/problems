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

        min_swap, max_swap = -1, -1

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


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]
        print(digits)

        max_so_far = 0
        max_index = -1

        min_swap, max_swap = -1, -1

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




class Solution:
    def maximumSwap(self, num: int) -> int:
        # store right most index
        arr = list(str(num))

        right_most_idx = [-1] * 10

        for i, number in enumerate(arr):
            right_most_idx[int(number)] = i

        for i, number in enumerate(arr):
            for j in range(9, int(number), -1):
                swap_idx = right_most_idx[j]
                if swap_idx > i:
                    # swap and break
                    arr[i], arr[swap_idx] = arr[swap_idx], arr[i]

                    return int("".join(arr))

        return num



""""

0  1  2  3
2, 7, 3, 6

0 1 2 3 4 5 6 7 8 9
- - 1 2 - - 3 1 - -

"""




        
                

# Second largest value
class Solution:
    def secondLargestValue(self, num):
        if len(num) <= 1:
            return []
        # build the largest value
        freq = [0] * 10

        for n in num:
            freq[n] += 1

        largest = []


        for num in range(9, -1, -1):
            count = freq[num]

            while count:
                largest.append(num)
                count -= 1


        for i in range(len(largest) - 1, 0, -1):
            if largest[i - 1] > largest[i]:
                # swap and return
                largest[i - 1], largest[i] = largest[i], largest[i - 1]
                return largest
    

        return []







num = [8, 7, 7, 7, 7]
solution= Solution()
print("res:", solution.secondLargestValue(num))

# output [7, 6, 2, 3]
