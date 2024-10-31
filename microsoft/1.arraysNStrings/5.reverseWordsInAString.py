# Time Complexity: O(n)
# Space Complexity: O(n)
def reverseWordsInAString(s):
  words = s.split()

  l = 0
  r = len(words) - 1

  while l < r:
    words[l], words[r] = words[r], words[l]

    l += 1
    r -= 1


  return ' '.join(words)



  







s = "   the sky is blue   "
print("res:", reverseWordsInAString(s))

# "blue is sky the"
