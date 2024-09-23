# Time Complexity: (2^n)
# Space Complexity: (2^n)
# Divide and Conquer
def houseRobber(houses):


  def divideNConquer(idx):
    if idx >= len(houses):
      return 0

    stealCurrent = houses[idx] + divideNConquer(idx + 2)
    skipCurrent = divideNConquer(idx + 1)

    return max(stealCurrent, skipCurrent)

  return divideNConquer(0)

houses = [30, 8, 2, 4]

print("Res:", houseRobber(houses))
