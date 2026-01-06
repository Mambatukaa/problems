""""


Given two positive integers left and right, find the two integers numi and num such that:
    • left < num < num2 < right
    • Both num1 and num2 are prime numbers.
    • num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2] . If there are multiple pairs satisfying these conditions,
return the one with the smallest numi value. If no such numbers exist, return I-1, -1] .

Example 1:
    Input: left = 10, right = 19
    Output: [11,13]
    Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
    The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
    Since 11 is smaller than 17, we return the first pair.

Example 2:
    Input: left = 4, right = 6
    Output: [-1,-1]
    Explanation: There exists only one prime number in the given range, so the
    conditions cannot be satisfied.

Constraints:
• 1 < left <= right <= 10^6
"""

import math

class Solution:
    def closestPrimes(self, left: int, right: int):
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False

            print("---------------------------------")
            print(n, math.sqrt(n))

            for i in range(5, int(math.sqrt(n)) + 1, 6):
                print(i, i + 2)
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            print("True")
            return True

        res = [-1, -1]

        prev = None
        gap = float('inf')

        for num in range(left, right + 1):
            if is_prime(num):
                if prev:
                    diff = num - prev
                    if diff < gap:
                        res = [prev, num]
                        gap = diff

                    #if diff == 1 or diff == 2:
                    #    return [prev, num]

                prev = num
        return res

# Approach 1: Sieve of Eratosthenes

class Solution:
    def _sieve(self, upper_limit):
        # Create an integer list to mark prime numbers (True = prime, False = not prime)
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime

        print(upper_limit ** 0.5)

        for number in range(2, int(math.sqrt(upper_limit)) + 1):
            print("Number:", number)
            if sieve[number]:
                # Mark all multiples of 'number' as non-prime
                for multiple in range(number * number, upper_limit + 1, number):
                    print(multiple)
                    sieve[multiple] = False
        return sieve

    def closestPrimes(self, left, right):
        # Step 1: Get all prime numbers up to 'right' using sieve
        sieve_array = self._sieve(right)

        prime_numbers = [
            num for num in range(left, right + 1) if sieve_array[num]
        ]

        # Step 2: Find the closest prime pair
        if len(prime_numbers) < 2:
            return -1, -1  # Less than two primes

        min_difference = float("inf")
        closest_pair = (-1, -1)

        for index in range(1, len(prime_numbers)):
            difference = prime_numbers[index] - prime_numbers[index - 1]
            if difference < min_difference:
                min_difference = difference
                closest_pair = prime_numbers[index - 1], prime_numbers[index]

        return closest_pair

solution = Solution()

left = 1
right = 500

print("res:", solution.closestPrimes(left, right))

