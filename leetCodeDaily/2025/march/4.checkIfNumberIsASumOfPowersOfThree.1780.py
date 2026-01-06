""""

Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise,
return false.
An integer y is a power of three if there exists an integer x such that y == 3x.

Example 1:
    Input: n = 12
    Output: true
    Explanation: 12 = 31 + 32

Example 2:
    Input: n = 91
    Output: true

    Explanation: 91 = 30 + 32+34
Example 3:
    Input: n = 21
    Output: false


Constraints:
• 1 <= n <= 10^7

"""

class Solution:
    # Time Complexity: O(2^log3n) or O(n)
    # Space Complexity: O(log3n)
    def checkPowersOfThree(self, n: int) -> bool:
        def _check_powers_of_three_helper(power, n):
            if n == 0:
                return True

            if 3**power > n:
                return False

            add = _check_powers_of_three_helper(power + 1, n - 3**power)
            skip = _check_powers_of_three_helper(power + 1, n)

            return add or skip

        return _check_powers_of_three_helper(0, n)



""""

Intuition
To optimize the previous approach, we aim to reduce the number of cases the algorithm
checks. We can simplify the process by working in reverse, starting with the larger powers
of 3. If n is greater than or equal to the current power, skipping this power will always lead
to a false result. This is because the largest sum we can achieve with smaller powers is
the sum of all lower powers, which is always less than the current power. So, if we skip this
power, we can't form the sum n, and we must include it by subtracting it from n.

Useful formula: 30 + 31+32+.. +37-1=3-1 < 3n

If n is still greater than the current power after this, we would have to add it to the sum
again. However, we can only use each power of 3 once, so we return false in this case.

If at any point n becomes 0, it means we can write n as a sum of distinct powers of 3, and
we return true .



"""

class Solution:
    # Time Complexity: O(log3 n)
    # Space Complexity: O(1)
    def checkPowersOfThree(self, n: int) -> bool:
        power = 0

        # Find the largest power that is smaller or equal to n
        while 3**power <= n:
            power += 1

        while n > 0:
            # Subtract current power from n
            if n >= 3**power:
                n -= 3**power
            # We cannot use the same power twice
            if n >= 3**power:
                return False
            # Move to the next lower power
            power -= 1

        # n has reached 0
        return True



class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            # Check if this power should be used twice
            if n % 3 == 2:
                return False
            # Divide n by 3 to move to the next greater power
            n //= 3
        # The ternary representation of n consists only of 0s and 1s
        return True
