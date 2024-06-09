# Time Complexity: O(n)
# Space Complexity: O(1)
# Greedy
class Solution:
  def maximumEvenSplit(self, f: int):
    ans, i = [], 2

    if f % 2 == 0:
      while i <= f:
        ans.append(i)
        f -= i
        i += 2
      
      ans[-1] += f
    
    return ans

solution = Solution()
print(solution.maximumEvenSplit(28))

