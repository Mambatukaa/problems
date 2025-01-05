"""


You are given a string s of lowercase English letters and a 2D integer array shifts where shifts [i] =
[starti, endi, direction 1. For every 1, shift the characters in s from the index start to the index

endi (inclusive) forward if direction = 1, or shift the characters backward if direction; = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so
that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous
letter in the alphabet (wrapping around so that 'a' becomes "z').

Return the final string after all such shifts to s are applied.


Input: 5 = "abc", shifts = [[0,1,0], [1,2,1], [0,2,1]]
Output: "ace"

Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now

s = "zac".

Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd"
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace"

print(26 % 26)
print(-1 % 26)
print(12 % 26)

print(ord("a"), ord("z")) # 97 -> 122


-1 + 26 % 26 ==== FORMULA TO RESET

"""





# Time Complexity: O(n*m) n - shift length,  m = start to end
# Space Complexity: O(k) k = string length 
# TIME LIMIT EXCEEDED 
# NAIVE APPROACH
def shiftingLettersII(s, shifts):
    s = list(s)

    for shift in shifts:
        start = shift[0]
        end = shift[1]

        direction = 1 if shift[2] == 1 else -1

        for i in range(start, end + 1):
            # chr() 0 - 25
            letter = (ord(s[i]) - 97 + direction) % 26
            s[i] = chr(letter + 97)

    return "".join(s)


# TIME LIMIT EXCEEDED
# CONVERT LETTERS TO INTEGERS
def shiftingLettersIII(s, shifts):
    sArr = [0] * len(s)

    for i in range(len(sArr)):
        sArr[i] = ord(s[i]) - 97

    for shift in shifts:
        start = shift[0]
        end = shift[1]

        direction = 1 if shift[2] == 1 else -1

        for i in range(start, end + 1):
            sArr[i] = (sArr[i] + direction + 26) % 26

    for i in range(len(sArr)):
        sArr[i] = chr(sArr[i] + 97)

    return "".join(sArr)

def shiftingLettersIV(s, shifts):
    print(s)

s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]

print("res:", shiftingLettersIII(s, shifts))

