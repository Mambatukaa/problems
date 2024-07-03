# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
def versionNumbers(version1, version2):
  # remove leading zeroes and dots
  versions1 = [int(v) for v in version1.split(".")]
  versions2 = [int(v) for v in version2.split(".")]

  # compare each characters 
  for i in range(max(len(versions1), len(versions2))):
    v1 = versions1[i] if i < len(versions1) else 0
    v2 = versions2[i] if i < len(versions2) else 0

    if v1 > v2:
      return 1
    elif v1 < v2:
      return -1

  return 0

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
def versionNumbersII(version1, version2):
  v1 = [int(i) for i in version1.split('.')]
  v2 = [int(i) for i in version2.split('.')]

  diff = len(v1) - len(v2)

  v1 += [0] * -diff
  v2 += [0] * diff

  return (v1 > v2) - (v1 < v2)
  
print(versionNumbersII("1.1", "1.1.0.0"))

"""

1 0
1 0 0 0


7.5.3 
7.5.2.4

if version1 < version2, return -1
if version1 > version2, return 1
else:
  return 0

-------------------------------------------------------------------------------------------

version1 = "1.2"
version2 = "1.10"

version1 < version2


-------------------------------------------------------------------------------------------

version1 = "1.01"
version2 = "1.001"

version1 == version2

-------------------------------------------------------------------------------------------

version1 = "1.0"
version2 = "1.0.0.0.0.0"

version1 == version2

-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

ignore leading zeroes after dots


1. Convert each strings to integer and compare


Iterate through versions. And calculate version. If ch == 0 check is it leading or not if it's leading ignore else * 10




remove leading 0's and dots "."


compare each characters




"""
