def twoSum(nums, target):
  """
  if nums array sorted we can use 2 pointers
    Time Complexity: O(n)
    Space Complexity: O(1)


  BRUTE FORCE
    Time Complexity: O(n^2)
    Space Complexity: O(1)


  MAP
    Time Complexity: O(n)
    Space Complexity: O(n)

  """

  dic = {}

  for i in range(len(nums)):
    num = nums[i]

    diff = target - num

    if diff in dic:
      return [i, dic[diff]]
    
    dic[num] = i

  return [] 



print(twoSum([2, 7, 11, 15], 9))

