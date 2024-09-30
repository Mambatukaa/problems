

def palindromePartitioning(s):
  

  res = []
  part = []

  def backtracking(i):
    if i == len(s):
      res.append(part.copy())

    for j in range(i, len(s)):
      part.append(s[i:j + 1])
      backtracking(j + 1)
      part.pop()


  backtracking(0)

  return res


s = "abc"

print("RES:", palindromePartitioning(s))


"""

s = "aab"

output: [["a", "a", "b"], ["aa", "b"]]





non palindrome partitions

a a b

a ab

aa b

aab



a -> 
  a b c
  a bc


        a
      b   
    c


"""
