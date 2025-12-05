"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.




"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        wordList_set = set(wordList)

        if endWord not in wordList_set:
            return 0
        
        letter_dict = defaultdict(set)

        for word in wordList:
            for i in range(n):
                letter_dict[word[:i] + "*" + word[i+1:]].add(word)

        q = deque([[beginWord, 1]])
        visited = {beginWord: True}

        while q:
            curr, step = q.popleft()

            for i in range(n):
                new_word = curr[:i] + "*" + curr[i + 1:]

                for word in letter_dict[new_word]:
                    if word == endWord:
                        return step + 1

                    if word not in visited:
                        visited[word] = True
                        q.append([word, step + 1])
                    
                    letter_dict[new_word] = set()
        return 0


""""

1. Iterate through letters and swap it with possible letters
2. If there is any valid word continue with that word

3. Track transformation count return it when endWord accomplished



defaultdict(<class 'list'>, 


{
    
'*ot': ['hot', 'dot', 'lot'], 
'h*t': ['hot'], 
'ho*': ['hot'], 



'd*t': ['dot'], 

'do*': ['dot', 'dog'], 

'*og': ['dog', 'log', 'cog'], 


'd*g': ['dog'], 
'l*t': ['lot'], 

'lo*': ['lot', 'log'], 
'l*g': ['log'], 
'c*g': ['cog'], 
'co*': ['cog']})


"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge case
        if endWord not in wordList:
            return 0

        word_list_set = set(wordList) # for faster look up

        characters_map = defaultdict(set)

        for word in wordList:
            for i in range(len(word)):
                characters_map[i].add(word[i])

        q = deque([[list(beginWord), 1]])
        seen = set()
        seen.add(beginWord)

        while q:
            curr_word, step = q.popleft()

            for index, values in characters_map.items():
                # change the index value and if it's valid add to the queue
                new_word = curr_word.copy()

                for value in values:
                    new_word[index] = value

                    new_word_str = "".join(new_word)

                    if new_word_str == endWord:
                        return step + 1

                    if new_word_str not in seen and new_word_str in word_list_set:
                        seen.add(new_word_str)
                        q.append([new_word.copy(), step + 1])

        return 0



class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge case
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                nei[pattern].append(word)

        q = deque([beginWord])
        seen = set()
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]

                    for neiWord in nei[pattern]:
                        if neiWord not in seen:
                            q.append(neiWord)
                            seen.add(neiWord)
                    
            res += 1

        return 0

"""

dot 
hog


dog
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge case
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                nei[pattern].append(word)

        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]

                    for neiWord in nei[pattern]:
                        q.append(neiWord)
                    
                    nei[pattern] = []

            res += 1

        return 0

"""

dot 
hog


dog
"""
