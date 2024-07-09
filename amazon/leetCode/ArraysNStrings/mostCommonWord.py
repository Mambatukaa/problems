from collections import defaultdict
import re
# Time Complexity: O(n)
# Space Complexity: O(n)
def mostCommonWord(paragraph, banned):
  bannedSet = set(banned)

  words = re.findall(r'\w+', paragraph.lower())
  
  return Counter(w for w in words if w not in bannedSet).most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

mostCommonWord(paragraph, banned)
