""""

You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:
    1 <= n <= 104

"""
from collections import defaultdict

class Solution:
    # Time Complexity: O(n log n) sum_of_digits_calculation = O(log x)
    # Space Complexity: O(log n) hash_map contains at least 
    def countLargestGroup(self, n: int) -> int:
        counter = defaultdict(int)

        largest_size = 0

        for num in range(1, n + 1):
            # calculate the digit sum and increase the count
            digitSum = sum([int(x) for x in str(num)])

            # update the answer
            counter[digitSum] += 1

            largest_size = max(counter[digitSum], largest_size)

        res = 0

        for value in counter.values():
            if value == largest_size:
                res += 1
        
        return res
    def countLargestGroupII(self, n: int) -> int:
        def calc_digit_sum(num):
            res = 0

            while num > 0:
                res += num % 10
                num //= 10

            return res


        counter = defaultdict(int)

        largest_size = 0

        for num in range(1, n + 1):
            # calculate the digit sum and increase the count
            digitSum = calc_digit_sum(num)

            # update the answer
            counter[digitSum] += 1

            largest_size = max(counter[digitSum], largest_size)

        res = 0

        for value in counter.values():
            if value == largest_size:
                res += 1
        
        return res

solution = Solution()

print("res:", solution.countLargestGroupII(13))
