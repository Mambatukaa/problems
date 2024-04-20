# Time Complexity: O(n)
# Space Complexity: O(n)
# Gave up
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      n = len(s)

      answer = 0
      count = {}
      left = 0

      for right in range(n):
        count[s[right]] = count.get(s[right], 0) + 1 

        # is invalid SHRINK THE WINDOW
        # window size - count[max] > k
        while (right - left + 1) - max(count.values()) > k:
          count[s[left]] -= 1
          left += 1

        # update answer
        answer = max(answer, right - left + 1)

      return answer

