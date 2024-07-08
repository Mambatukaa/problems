


# Time Complexity: O(n)
# Space Complexity: O(n)
def findJudge(n, trust):
  people = [0] * n

  for a, b in trust:
    people[a - 1] -= 1
    people[b - 1] += 1

  for i in range(n):
    trust = people[i]

    if trust == n - 1:
      return i + 1

  return -1


n = 3
trust = [[1, 3], [2,3]]

print(findJudge(n, trust))


"""

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.


"""
