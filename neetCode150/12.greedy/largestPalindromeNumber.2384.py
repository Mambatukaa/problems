
from collections import Counter 

# Time Complexity: O(n)
# Space Complexity: O(n)
# greedy
class Solution:
    def largestPalindromic(self, num: str) -> str:
      digit_counts = Counter(num)

      first_half = []
      center = ""


      for digit in range(9, -1, -1):
        digit_char = str(digit)

        if digit_char in digit_counts:
          digit_count = digit_counts[digit_char]

          num_pairs = digit_count // 2

          if num_pairs:
            if first_half or digit:
              first_half.append(digit_char * num_pairs)

          if digit_count % 2 and not center:
            center = digit_char

      if not first_half and not center:
        return "0"

      return "".join(first_half + [center] + first_half[::-1])



    def largestPalindromicII(self, num: str) -> str:
        count = Counter(num)
        palindrome = mid = ''

        for d in sorted(count.keys(), reverse=True):
          print(d, ":", count[d], '========', count[d] & 1)

          mid = max(mid, d * (count[d] & 1))
          palindrome += d * (count[d] // 2)

        palindrome = palindrome.lstrip('0')
        return (palindrome + mid + palindrome[::-1]) or '0'


num = "444947137"

solution = Solution()

print(solution.largestPalindromicII(num))
        
