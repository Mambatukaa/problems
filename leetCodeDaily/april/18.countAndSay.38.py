""""

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

 

Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:

Input: n = 1

Output: "1"

Explanation:

This is the base case.

 

Constraints:

1 <= n <= 30
 

Follow up: Could you solve it iteratively?






"""
class Solution:
    # Recursive
    # Time Complexity: O(n * m)
    # Space Complexity: O(n)
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        res = self.countAndSay(n - 1)

        curr = ""
        length = len(res)

        l = 0
        for r in range(length):
            if res[l] != res[r]:
                curr += str(r - l) + res[l]
                l = r

        curr += str(r - l + 1) + res[l]

        return curr

    # iterative solution
    def countAndSayII(self, n: int) -> str:
        if n == 1:
            return "1"

        res = "11"

        for _ in range(2, n):
            curr = ""

            l = 0

            length = len(res)

            for r in range(length):
                if res[l] == res[r]:
                    continue

                curr += str(r - l) + res[l]
                l = r

            curr += str(r - l + 1) + res[l]
            res = curr

        return res
solution = Solution()

print("res 1:", solution.countAndSay(6))
print("res:", solution.countAndSayII(6))
