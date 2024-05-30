class Solution:
  def maximum69Number(self, num):
    strNums = str(num)

    res = 0
    chance = 1

    for s in strNums:
      curr = int(s)

      if chance == 1 and curr == 6:
        chance -= 1
        curr = 9

      res *= 10
      res += curr


    return res




solution = Solution()
print(solution.maximum69Number(669))
