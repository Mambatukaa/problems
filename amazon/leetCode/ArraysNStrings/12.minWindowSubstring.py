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

print(minimumWindow(s, t))



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
