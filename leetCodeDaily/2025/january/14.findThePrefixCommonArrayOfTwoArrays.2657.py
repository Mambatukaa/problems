"""
You are given two O-indexed integer permutations A and B of length n.

    A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are
    present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

Constraints:
• 1 <= A.length == B.length == n <= 50
• 1 < A[i], B[i] <= n
• It is guaranteed that A and B are both a permutation of n integers.

"""

class Solution:
    # Naive approach
    # 11 Minutes
    # Time Complexity: O(n^2) Accepted because the n maximum length is 50
    # Space Complexity: O(n)
    def findThePrefixCommonArray(self, A, B):
        n = len(A)

        seen = [0] * n
        res = [0] * n

        for i in range(n):
            seen[A[i] - 1] += 1
            seen[B[i] - 1] += 1

            ctr = 0

            for count in seen:
                if count == 2:
                    ctr += 1
            
            res[i] = ctr

        return res
        

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findThePrefixCommonArrayII(self, A, B):
        n = len(A)

        seen = [0] * n
        res = [0] * n
        ctr = 0

        for i in range(n):
            seen[A[i] - 1] += 1

            if seen[A[i] - 1] == 2:
                ctr += 1

            seen[B[i] - 1] += 1
            
            if seen[B[i] - 1] == 2:
                ctr += 1
            
            res[i] = ctr

        return res

solution = Solution()

