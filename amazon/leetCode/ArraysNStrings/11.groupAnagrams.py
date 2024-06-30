from collections import defaultdict
# Time Complexity: O(n * m log m)
# Space Complexity: O(n)
def groupAnagrams(strs):
  dic = defaultdict(dict)

  for s in strs:
    sortedString = "".join(sorted(s))

    if sortedString not in dic:
      dic[sortedString] = []

    dic[sortedString].append(s)

  return list(dic.values())

strs = [""]
groupAnagrams(strs)

"""
Input: strs = [ "eat", "tea", "tan", "ate", "nat", "bat" ]
Output: [ ["bat"], ["nat", "tan"], ["ate", "eat", "tea"] ]




store anagrams on map.

iterate through strs
  sort the item and add to the map


add maps values to the array and return




"""
