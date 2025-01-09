
class Solution:
    # Time Complexity: O(n * m) The outer loop iterates through each string in the array words, which takes O(n) operations. For each string, the startsWith method needs to compare characters until it reaches the end of the prefix or finds a mismatch. In the worst case, this comparison takes O(m) operations.
    # Space Complexity: O(n * m)
    # Built-in Methods
    def prefixCount(self, words: List[str], pref: str) -> int:
       res = 0 

       for word in words:
        if word.startswith(pref):
            res += 1
            
       return res
