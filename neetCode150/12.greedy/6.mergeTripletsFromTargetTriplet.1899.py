class Solution:
    def mergeTriplets(self, triplets, target) -> bool:
      seen = set()

      for i in range(3):
        targetVal = target[i]

        # search targetVal from triplets

        for triplet in triplets:

          if triplet[i] == targetVal:
            isValid = True

            # check other values are less than targetVal
            for j in range(3):
              if i == j:
                continue

              if target[j] < triplet[j]:
                isValid = False
                break

            if isValid:
              seen.add(i)
      
      return len(seen) == 3
      


    # Optimal solution
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def mergeTripletsII(self, triplets, target):
      seen = set()

      # iterate through triplets and check is triplet is valid
      for triplet in triplets:
        if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
          continue


        # check the valid triplet is contain target value or not
        for i, v in enumerate(triplet):
          if v == target[i]:
            seen.add(i)

      return len(seen) == 3



solution = Solution()

triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]

target = [5, 5, 5]


print("res:", solution.mergeTripletsII(triplets, target))
        
