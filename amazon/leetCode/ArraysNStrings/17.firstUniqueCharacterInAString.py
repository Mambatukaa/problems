from collections import Counter

# Time Complexity: O(n)
# Space Complexity: O(1) only 26 elements
def firstUniqChar(s):
  ctr = Counter(s)

  for i in range(len(s)):
    ch = s[i]
    if ctr[ch] == 1:
      return i

  return -1

# Time Complexity: O(n)
# Space Complexity: O(1) only 26 elements
def firstUniqCharII(s):
  arr = [0] * 26

  for ch in s:
    arr[ord(ch) - ord("a")] += 1

  for i in range(len(s)):
    ch = s[i]

    if arr[ord(ch) - ord("a")] == 1:
      return i

  return -1



s = "leetcode"

print("res:", firstUniqCharII(s)  )


"""

return the index of first unique char

if there is no unique char return -1


"""
