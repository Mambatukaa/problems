


class Solution:
    # Time Complexity: O(4^n * n) n is the length of digits
    # Space Complexity: O(n)
    def letterCombinations(self, digits):
        # Edge case
        if not digits:
            return []

        digitsMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        self.res = []

        def backtracking(idx, curr): 
            if len(digits) == len(curr):
                self.res.append("".join(curr))
                return
            
            letters = digitsMap[digits[idx]]

            for letter in letters:
                curr.append(letter)

                backtracking(idx + 1, curr)

                curr.pop()
            


        backtracking(0, [])


        return self.res

solution = Solution()

print("Res:", solution.letterCombinations("23"))
"""

digits = "23"


output: ["ad", "ae", "bd", "be", "bf", "cd", "ce", "cf"]


digitsMap = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}



Time complexity: O(4 
N
 ⋅N), where N is the length of digits. Note that 4 in this expression is referring to the maximum value length in the hash map, and not to the length of the input.

The worst-case is where the input consists of only 7s and 9s. In that case, we have to explore 4 additional paths for every extra digit. Then, for each combination, it costs up to N to build the combination. This problem can be generalized to a scenario where numbers correspond with up to M digits, in which case the time complexity would be O(M 
N
 ⋅N). For the problem constraints, we're given, M=4, because of digits 7 and 9 having 4 letters each.

Space complexity: O(N), where N is the length of digits.

Not counting space used for the output, the extra space we use relative to input size is the space occupied by the recursion call stack. It will only go as deep as the number of digits in the input since whenever we reach that depth, we backtrack.

As the hash map does not grow as the inputs grows, it occupies O(1) space.

"""



