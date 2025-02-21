""""





A happy string is a string that:
• consists only of letters of the set ['a', 'b', 'c'].
• s[i] != s[i + 1] for all values of i from 1 to s. length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbeb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
Return the th string of this list or return an empty string if there are less than k happy strings of length n.

Example 1:
    Input: n = 1, k = 3
    Output: "c"
    Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

Example 2:
    Input: n = 1, k = 4
    Output: ""
    Explanation: There are only 3 happy strings of length 1.

Example 3:
    Input: n = 3, K = 9
    Output: "cab"
    Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb",
    "cab", "cac", "cba", "cbc"]. You will find the gth string = "cab"



"""


class Solution:
    # Backtracking
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(2^n)
    def getHappyString(self, n: int, k: int) -> str:

        res = []


        def backtracking(curr):
            if len(curr) == n:
                res.append("".join(curr))
                return
            
            for letter in "abc":
                if curr and curr[-1] == letter:
                    continue
                curr.append(letter)
                backtracking(curr)
                curr.pop()
        
        backtracking([])

        if len(res) < k:
            return ""

        return res[k-1]


    # Optimized recursive
    # Time Complexity: O(k * n) or O(n * n^2)
    # Space Complexity: O(n)
    def getHappyStringII(self, n: int, k: int) -> str:
        self.res = None
        self.count = 0

        def backtracking(curr):
            if len(curr) == n:
                self.count += 1

                if self.count == k:
                    self.res = "".join(curr)
                return
            
            for letter in "abc":
                if curr and curr[-1] == letter:
                    continue
                curr.append(letter)
                backtracking(curr)

                if self.res:
                    return

                curr.pop()
        
        backtracking([])

        if not self.res:
            return ""

        return self.res

    # Time Complexity: O(k * n) or O(n * n^2)
    # Space Complexity: O(n^2)
    def getHappyStringIII(self, n: int, k: int) -> str:
        stack = [""]
        count = 0

        while stack:
            curr_string = stack.pop()

            if len(curr_string) == n:
                count += 1

                if count == k:
                    return curr_string
                continue
            
            for letter in reversed(["a", "b", "c"]):
                if curr_string and curr_string[-1] == letter:
                    continue

                stack.append(curr_string + letter)

solution = Solution()

print("res:", solution.getHappyStringIII(3, 9))
