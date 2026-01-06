""""

You have n tiles, where each tile has one letter tiles [il printed on it.
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:
    Input: tiles = "AAB"
    Output: 8
    Explanation: The possible sequences are "A" ', "B" ', "AA" ', "AB" ', "BA" ', "AAB" , "ABA" ', "BAA".

Example 2:
    Input: tiles = "AAABBC"
    Output: 188

Example 3:
    Input: tiles = "V"
    Output: 1

Constraints:
• 1 <= tiles.length <= 7
• tiles consists of uppercase English letters.

"""

from collections import Counter
class Solution:
    # Time Complexity: O(n*n!)
    # Space Complexity: O(n*n!)
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        seenIdx = set()

        def backtracking(idx, curr):
            if idx >= len(tiles):
                return
            
            for i in range(len(tiles)):
                if i in seenIdx:
                    continue

                curr.append(tiles[i])
                seenIdx.add(i)

                res.add("".join(curr))

                backtracking(idx + 1, curr)
                curr.pop()
                seenIdx.remove(i)
            
        backtracking(0, [])

        return len(res)

    # Time Complexity: O(n!)
    # Space Complexity: O(n)
    def numTilePossibilitiesII(self, tiles: str) -> int:
        char_count = [0] * 26

        for char in tiles:
            char_count[ord(char) - ord("A")] += 1


        def find_sequences():
            total = 0

            for pos in range(26):
                if char_count[pos] == 0:
                    continue
                print(char_count)

                total += 1

                char_count[pos] -= 1
                total += find_sequences()
                char_count[pos] += 1


            return total
        
        return find_sequences()
    
    def numTilePossibilitiesIII(self, tiles: str) -> int:
        char_count = Counter(tiles)
        print(char_count, 'initial')

        def backtracking():
            res = 0

            for c in char_count:
                print(char_count)
                if char_count[c] > 0:
                    res += 1

                    char_count[c] -= 1
                    res += backtracking()

                    char_count[c] += 1

            return res
                    
        return backtracking()
        
solution = Solution()

tiles = "AAABBC"
tiles = "AAB"
print("res:", solution.numTilePossibilities(tiles))
print("-------------------------------")
print("res:", solution.numTilePossibilitiesIII(tiles))




