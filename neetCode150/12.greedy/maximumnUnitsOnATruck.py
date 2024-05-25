# Time Complexity: O(n))
# Space Complexity: O(1))
# Greedy
class Solution:
  def maximumUnits(self, boxTypes, truckSize):
    boxes = [None] * 1001
    units = 0

    for i in range(len(boxTypes)):
      numOfBoxes, numOfUnits = boxTypes[i]

      if boxes[numOfUnits]:
        boxes[numOfUnits] += numOfBoxes
      else:
        boxes[numOfUnits] = numOfBoxes
    
    for i in range(len(boxes) - 1, -1, -1):
      if not boxes[i]: continue

      numOfBoxes = boxes[i]
      size = min(truckSize, numOfBoxes)

      truckSize -= size
      units += i * size

      if truckSize == 0:
        break

    return units

solution = Solution()

boxTypes = [
    [1,3],
    [5,5],
    [2,5],
    [4,2],
    [4,1],
    [3,1],
    [2,2],
    [1,3],
    [2,5],
    [3,2]]

truckSize = 35

solution.maximumUnits(boxTypes, truckSize)
