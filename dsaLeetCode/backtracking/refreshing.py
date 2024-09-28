# create a string with n length using english vowels
# Time Complexity: O(5^n)
# Space Complexity: O(5^n)

def vowelCombinations(n):
  vowels = ["a", "e", "i", "o", "u"]
  res = []

  def backtracking(curr):
    if len(curr) == n:
      res.append("".join(curr))
      return

    for vowel in vowels:
      curr.append(vowel)
      backtracking(curr)
      curr.pop()

  backtracking([])

  return res





# return all possible palindrome partitioning of s
# Time Complexity: O(k * 2^n)
# Space Complexity: O(2^n)
def partition(s):
  res = []
  part = []

  def backtracking(idx):
    if len(s) == idx:
      res.append(part.copy())
      return
    
    for j in range(idx, len(s)):
      if isPali(s, idx, j):
        part.append(s[idx: j + 1])
        backtracking(j + 1)
        part.pop()


  def isPali(s, l, r):
    while l < r:
     if s[l] != s[r]:
       return False

     l, r = l + 1, r - 1 

    return True
  
  backtracking(0)
  return res

#print("res:", partition("aab"))

"""

s contains only lowercase english letters

s = "aab"

output: [["a","a","b"],["aa","b"]]


"""



# Permutations
class Solution:
    def permute(self, nums):

      res = []

      def backtracking(curr):
        if len(curr) == len(nums):
          res.append(curr[:])
          return
        
        for j in range(len(nums)):
          if nums[j] not in curr:
            curr.append(nums[j])
            backtracking(curr)
            curr.pop()
        
      backtracking([])

      return res

# Subsets
class Solution:
    def subsets(self, nums):

      res = []


      def backtracking(idx, curr):
        res.append(curr[:])

        if idx == len(nums):
          return

        for j in range(idx, len(nums)):
          curr.append(nums[j])
          backtracking(j + 1, curr)
          curr.pop()

      
      backtracking(0, [])

      return res
        
    

"""

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.


1 to k combinations

"""

class Solution:
  def combine(self, n: int, k: int):
    curr = []
    res = []
    
    def backtracking(idx):
      if len(curr) == k:
        res.append(curr.copy())
        return


      for j in range(idx, n + 1):
        curr.append(j)
        backtracking(j + 1)
        curr.pop()

    backtracking(1)

    return res

solution = Solution()

n = 4
k = 2

print("res:", solution.combine(n, k))
