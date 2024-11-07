from collections import defaultdict

# Time Complexity: O(n * m log m)
# Space Complexity: O(k)
# Add solution using map
def groupAnagrams(strs):
  res = {}
  
  for item in strs:
    sortedStr = ''.join(sorted(item))
    
    if not sortedStr in res:
      res[sortedStr] = []

    res[sortedStr].append(item)

  return list(res.values())


# Time Complexity: O(n * m)
# Space Complexity: O(n)
def groupAnagramsII(strs):
  res = {}
  # res = defaultdict(list)

  for word in strs:
    counter = [0] * 26 

    for ch in word:
      counter[ord(ch) - ord("a")] += 1

    if tuple(counter) not in res:
      res[tuple(counter)] = []

    res[tuple(counter)].append(word)

  return list(res.values())


print("res:", groupAnagramsII(["eat", "tea", "tan", "ate", "nat", "bat"]))

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
