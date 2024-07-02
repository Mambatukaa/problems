# initial
from collections import Counter

def minimumWindow(s, t):
  count = Counter(t)

  def isValid(s):
    tCount = count.copy()

    for ch in s:
      if ch in tCount:
        tCount[ch] = tCount[ch] - 1

        if tCount[ch] == 0:
          del tCount[ch]
      
      if len(tCount) == 0:
        return True

    return len(tCount) == 0


  l = 0
  res = ""
  resLength = float('inf')
  curr = [] 


  for r in range(len(s)):
    curr.append(s[r]) 

    while isValid(curr):

      if len(curr) < resLength:
        res = "".join(curr)
        resLength = len(curr)

      l += 1
      curr.pop(0)

  return res

s = "ADOBECODEBANC"
t = "ABC"



"""

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

ADOBEC
  DOBECODEBA
       ODEBA
       ODEBANC
          BANC


1. Return the minimum substring that includes t


"ADOBEC" => "BANC"

s and t consist of upper and lower english letters.


1. Count T
2. And slide the window starts from 0th index on s.
3. If window is valid that means all values in T. Shrink the window.
4. Update the answer while current window is valid



Find algorithm runs in O(m + n) time.

"""


# Time Complexity: O(m + n)
# Space Complexity: O(m + n)
def minWindow(s, t):
  countT, window = {}, {}

  for c in t:
    countT[c] = countT.get(c, 0) + 1


  l = 0

  res = [-1, -1]
  resLength = float('inf')

  have, need = 0, len(countT)

  for r in range(len(s)):
    c = s[r]

    window[c] = window.get(c, 0) + 1

    if c in countT and window[c] == countT[c]:
      have += 1

    # window has all s elements
    while have == need:
      if (r - l + 1) < resLength:
        res = [l, r]
        resLength = r - l + 1

      # pop from the left of our window
      window[s[l]] -= 1

      if s[l] in countT and window[s[l]] < countT[s[l]]:
        have -= 1

      l += 1

  l, r = res

  return s[l: r + 1] if res != float('inf') else ""
        
  # need, have

  # if need == have shrink the window

s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s, t))


