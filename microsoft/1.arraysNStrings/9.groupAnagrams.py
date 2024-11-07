# Time Complexity: O(n * m log m)
# Space Complexity: O(k)
# Add solution using map
def groupAnagrams(strs):
  res = {}
  
  for item in strs:
    sortedStr = ''.join(sorted(item))
    
    if not sortedStr in res:
      res[sortedStr] = [item]
    else:
      res[sortedStr].append(item)

  return list(res.values())


print("res:", groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

"""
Example 1:

  Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
  Output: [["bat"], ["nat", "tan"], ["ate" ,"eat" ,"tea"]]
  Explanation: 
  • There is no string in strs that can be rearranged to form "bat" .
  • The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
  • The strings "ate" , "eat" , and "tea" are anagrams as they can be rearranged to form each other.



create maps

1. sort the str and add to the map as a key.
  if sorted str is already exists in the map add regular str to the map


2. return map values

Time Complexity: O(n * m log m)
Space Complexity: O(k)


"""
