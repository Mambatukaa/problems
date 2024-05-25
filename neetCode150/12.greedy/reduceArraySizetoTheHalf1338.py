from collections import Counter

class Solution:
    def minSetSize(self, arr):
      cnt = Counter(arr)
      occurences = sorted(cnt.values(), reverse=True)

      print(occurences, len(arr))

      res = 0
      counter = 0

      for occ in occurences:
        if counter >= len(arr) / 2:
          return res

        counter += occ
        res += 1


      return res







solution = Solution()
arr = [1, 2, 3, 4]
print("res:", solution.minSetSize(arr))
        
# count occurences
# add elements that has most occurences until reach the size of the array half
