# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# Backtracking
def letterCombinations(digits):
  dic = {
      "2": "abc",
      "3": "def",
      "4": "ghi",
      "5": "jkl",
      "6": "mno",
      "7": "pqrs",
      "8": "tuv",
      "9": "wxyz",
  }


  res = []

  if not digits:
    return res

  def backtracking(idx, curr):

    # base case
    if idx == len(digits):
      res.append(curr)
      return

    digit = digits[idx]

    for letter in dic[digit]:
      backtracking(idx + 1, curr + letter)

  backtracking(0, "")

  return res


print("res:", letterCombinations("234"))
"""

Given a string containing digits 2 - 9 inclusive return all possible letter 
  combinations that number could represent.

Return an answer in any order.


2: abc,
3: def,
4: ghi,
5: jkl,
6: mno,
7: pqrs
8: tuv
9: wxyz


0 <= digits.length <= 4
digits[i] is a digit in range ["2", "9"]



EXAMPLE 1:
  Input: digits = "23"

  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


23 

Decision tree 

a -> d 
  -> e
  -> f

b -> d
  -> e
  -> f

c -> d
  -> e
  -> f




Starts from first digit and collect values from next digits and when current string reaches the limit add to the answer.

BACKTRACKING


"""
