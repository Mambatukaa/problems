import collections

# NOTE
# Time Complexity: O(M^2 * N) M is the lenght of each word 
    # and N is the total number of words in the input word list
    # creating new string takes O(M)
# Space Complexity: O(M^2 * N)

# Solution using BFS
def wordLatter(beginWord, endWord, wordList):
  # since we are gonna search from wordList a lot convert to the set
  wordSet = set(wordList)
  n = len(beginWord)

  # base case
  if endWord not in wordSet:
    return 0

  # create letter choices on each index
  lettersDic = collections.defaultdict(set)

  for i in range(n):
    for word in wordList:
      lettersDic[i].add(word[i])


  # to find shortest path use BFS
  # starts from beginWord and add possible neighbors that include in wordSet
  # once reach the endWord return shortestPath

  # initial path value is 1 because we have the word begin
  q = collections.deque([[beginWord, 1]])
  seen = { beginWord }

  while q:
    curr, path = q.popleft()

    for i in range(n):
      # create every combinations and add the valid WORD to the queue
      for comb in lettersDic[i]:
        newWord = curr[:i] + comb + curr[i+1:]

        if newWord == endWord:
          return path + 1

        # check new word is valid or not
        if newWord in seen or newWord not in wordSet:
          continue
        
        seen.add(newWord)
        q.append([newWord, path + 1])

  return 0



beginWord = "hit"
endWord = "cog"
#wordList = [ "hot", "dot", "dog", "lot", "log", "cog"]
wordList = ["hot","dot","tog","cog"]

print(wordLatter(beginWord, endWord, wordList))
