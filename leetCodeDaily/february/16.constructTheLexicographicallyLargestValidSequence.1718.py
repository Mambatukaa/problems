""""


Given an integer n, find a sequence that satisfies all of the following:
• The integer 1 occurs once in the sequence.
• Each integer between 2 and n occurs twice in the sequence.
• For every integer i between 2 and n, the distance between the two occurrences of i is exactly i .
The distance between two numbers on the sequence, a [i] and a[i], is the absolute difference of their indices, 1j - 1|.
Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.
A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number
greater than the corresponding number in b. For example, (0,1,9, 0] is lexicographically larger than 10,1,5,61 because the first position they differ is at the
third number, and 9 is greater than 5.

Example 1:
Input: n = 3
Output: [3,1,2,3,2]|
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:
Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]|

Constraints:
• 1 <= n <= 20


"""


class Solution:
    def constructDistancedSequence(self, n: int):
        count = [1] * n
        count[0] = 1
        size = n * 2 - 1

        def checkIsValid(num):
            visited = set()
            for i in range(size):
                digit = num[i]
                if digit in visited:
                    continue
                visited.add(digit)

                if digit == 1:
                    continue

                idx = i + digit

                if idx >= size or digit != num[idx]:
                    return False
            
            return True
        
        def backtracking(idx, curr):
            if not 0 in curr:
                if checkIsValid(curr):
                    return curr
                return None

            for i in range(n - 1, -1, -1):
                if count[i] > 0:
                    digit = i + 1
                    newIdx = idx + digit

                    if digit == 1:
                        newIdx = idx

                    if newIdx >= size or curr[idx] or curr[newIdx]:
                        continue

                    curr[idx] = digit
                    curr[newIdx] = digit
                    count[i] -= 1

                    j = idx + 1

                    while j < size and curr[j]:
                        j += 1

                    res = backtracking(j, curr)

                    if res:
                        return res

                    curr[idx] = 0
                    curr[newIdx] = 0
                    count[i] += 1

        curr = [0] * size
        return backtracking(0, curr)



solution = Solution()
n = 5

print("res:", solution.constructDistancedSequence(n))
