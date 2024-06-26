# Time Complexity: O(n)
# Space Complexity: O(1)
def romanToInt(s):
  dic = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000,

      # Combinations
      "IV": 4,
      "IX": 9,

      "XL": 40,
      "XC": 90,
      "CD": 400,
      "CM": 900
      }

  res = 0

  i = 0

  while i < len(s):
    # check possiblity of 2 digits
    if i < len(s) - 1 and s[i] + s[i + 1] in dic:
      res += dic[s[i] + s[i + 1]]
      i += 1
    else:
      res += dic[s[i]]

    i += 1

  return res

print(romanToInt("MCDLXXVI"))





"""

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


III ===> 3

III = 3

LVIII ===> 58

L = 50, V = 5, III = 3


MCMXCVIII ==> 1998

M = 1000, CM = 900, XC = 90, VIII = 8

M = 1000     M > C
  CM = 900   C < M
    XC = 90  X < C
     V = 5   V > I
     I = 1   I == I
     I = 1   I == I
     I = 1   I == I



1. Create dic with roman to int values.
2. Start to check roman's from the start. Roman can be one digit or two digits.
    
    Check the roman is 1 digit or 2 digits.
     Possiblity of 2 digits ===> s[i] < s[i + 1] TWO DIGITS


Iterate through characters.
  If character has possiblity of 2 digits get 2 digits and add to the res
  else add one digit to the res

return res

"""

#NOTE
