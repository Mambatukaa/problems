from collections import defaultdict, Counter
import re
# Time Complexity: O(n)
# Space Complexity: O(n)
def mostCommonWord(paragraph, banned):
  bannedSet = set(banned)

  words = re.findall(r'\w+', paragraph.lower())
  
  return Counter(w for w in words if w not in bannedSet).most_common(1)[0][0]

def mostCommonWordII(paragraph, banned):
  bannedSet = set(banned)

  for i in "!.',;:?": 
    paragraph = paragraph.replace(i, ' ')

  words = paragraph.lower().split()
  
  return Counter(w for w in words if w not in bannedSet).most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print("res:", mostCommonWordII(paragraph, banned))
