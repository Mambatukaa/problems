# Time Complexity: (2^n)
# Space Complexity: (2^n)
# Divide and Conquer
# ADD MEMO
def houseRobber(houses):


  memo = {}

  def divideNConquer(idx):
    if idx >= len(houses):
      return 0

    if idx in memo:
      return memo[idx]

    stealCurrent = houses[idx] + divideNConquer(idx + 2)
    skipCurrent = divideNConquer(idx + 1)

    memo[idx] = max(stealCurrent, skipCurrent)

    return max(stealCurrent, skipCurrent)

  return divideNConquer(0)

houses = [1,3,5,6, 88, 12,12,24,5663,2123,1235,6,456,3245,1,3,5,6, 88, 12,12,24,5663,2123,1235,6,456,3245,1,3,5,6, 88, 12,12,24,5663,2123,1235,6,456,3245,1,3,5,6, 88, 12,12,24,5663,2123,1235,6,456,3245,1,3,5,6, 88, 12,12,24,5663,2123,1235,6,456,3245,1,3,5,6, 88, 12,12,24,5663,2123,1235,6,456,3245,1,3,5,6, 88, 12,12,24,5663,2123,1235,6,456,3245,1,3,5,6, 88, 12,12,24,5663,2123,1235,6,456,3245,1,3,5,6, 88, 12,12,24,5663,2123,1235,6,456,3245,1,3,5,6, 88, 12,12,24,5663,2123,1235,6,456,3245,1,3,5,6, 88, 12,12,24,5663,2123,1235,6,456,3245,1,3,5,6, 88, 12,12,24,5663,2123,1235,6,456,3245]

print("Res:", houseRobber(houses))
