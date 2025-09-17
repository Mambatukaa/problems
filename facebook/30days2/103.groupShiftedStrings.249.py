"""
Perform the following shift operations on a string:

Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
We can keep shifting the string in both directions to form an endless shifting sequence.

For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...
You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:

Input: strings = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.


"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = []
        dic = defaultdict(list)

        for s in strings:
            key = ""
            left_shift = ord(s[0]) - ord("a")
            print('left:', left_shift)

            for l in s:
                encoded = ord(l) - left_shift + 26

                if encoded > 122:
                    encoded -= 26
                
                key += chr(encoded)
            dic[key].append(s)

        for val in dic.values():
            res.append(val)
        return res


"""

ASCII

iterate through the strings
    iterate throught the string
        calc left_shift = s[0] - chr("a")
        create the mapping_key by substracrting "a"


a - a = 0

a b c
0 0 0

a b c

"""        
