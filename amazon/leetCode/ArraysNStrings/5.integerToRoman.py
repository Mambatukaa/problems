# Time Complexity: O(m * n)  m = numberalTable
# Space Complexity: O(m)
def intToRoman(num):
  numerals_table = [
    [1,    'I'],
    [4,   'IV'],
    [5,    'V'],
    [9,   'IX'],
    [10,   'X'],
    [40,  'XL'],
    [50,   'L'],
    [90,  'XC'],
    [100,  'C'],
    [400, 'CD'],
    [500,  'D'],
    [900, 'CM'],
    [1000, 'M'],
  ]
        
  numeral = []

  for s in numerals_table[::-1]:
      while num >= s[0]:
          numeral.append(s[1])
          num -= s[0]
  
  return ''.join(numeral)

print(intToRoman(1994))

"""

Symbol value:

start with 4 or 9:
   4: IV
   9: IX
  40: XL
  90: XC
 400: CD
 900: CM

  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000



  input: num = 3749
  output: MMMDCCXLIX


  3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
   700 = DCC as 500 (D) + 100 (C) + 100 (C)
    40 = XL as 10 (X) less of 50 (L)
     9 = IX as 1 (I) less of 10 (X)


  Constraints:
  1 <= num <= 3999

    

  
    



"""


