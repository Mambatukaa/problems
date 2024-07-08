def strStr(haystack, needle):
  n = len(needle)
  m = len(haystack)
  if n > m:
    return -1


  i = 0

  while i < m:

    if needle[0] == haystack[i]:
      for j in range(n):
        if i + j >= m:
          break
        if needle[j] != haystack[i + j]:
          break

        if j == n - 1:
          return i

    i += 1

  return -1

#           012345678910
haystack = "mississippi"

needle = "issipi"
print(strStr(haystack, needle))


"""

return the index of the first occurence of needle in haystack, if needle is not part of haystack return -1



Search the first letter of needle from haystack

if the first letter found start to search needle from haystack.

                 f b   f
            012345678912  
haystack = "kkkkksasbutsad"

needle = "sad"


"""
