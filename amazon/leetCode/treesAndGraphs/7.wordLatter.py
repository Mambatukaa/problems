import string
from collections import deque, defaultdict
def wordLadder(beginWord, endWord, wordList):
  # since we are check newWord from wordList every time. Convert wordList to set to improve time complexity
  wordListSet = set(wordList)

  if endWord not in wordListSet:
    return 0 

  q = deque([[beginWord, 1]])
  seen = set()
  seen.add(beginWord)

  while q:
    curr, counter = q.popleft()

    # add valid curr neighbors to the queue
    for i in range(len(curr)):
      for combination in string.ascii_lowercase:

        neighbor = curr[:i] + combination + curr[i+1:]

        # NOTE vaild neighbors
        if neighbor in wordListSet and neighbor not in seen:

          if neighbor == endWord:
            return counter + 1

          seen.add(neighbor)
          q.append([neighbor, counter + 1])

  return 0 

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot" ,"dog","lot","log","cog"]


print("res:", wordLadder(beginWord, endWord, wordList))


"""

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord 
-> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest 
transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. 
Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot" ,"dog","lot","log","cog"].
Output: [["hit", "hot","dot","dog", "cog"], ["hit", "hot","lot","log". ,"cog" ]]

Explanation: There are 2 shortest transformation sequences:
"hit" → "hot" →> "dot" →> "dog" → "cog"
"hit" → "hot" →> "lot" →> "log" →> "cog"


beginWord does not to be in wordList.
endWord does neet to be in wordList.


newWord must be in wordList


currentWord can change only one letter at a time.



"""

