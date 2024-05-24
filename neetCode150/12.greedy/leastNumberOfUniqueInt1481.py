

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
      c = Counter(arr)

      freq = [fre for fre in c.values()]      
      freq.sort()

      for i in range(len(freq)):
        curr = freq[i]

        if curr > k:
          return len(freq) - i
        
        k -= curr

      return 0
"""


Count duplication using map


arr = [4, 3, 1, 1, 3, 3, 2]

{
  1: 2,
  2: 1,
  3: 3,
  4: 1
}

create frequences and reduce until k == 0


1, 1, 2, 3

"""
