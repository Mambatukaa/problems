from collections import deque

# Time Complexity: O(b) n = startGene O(bank) bank to set. Everything is constant. 
# if n = startGene O(4^n * n ^ 2 + b)
# Space Complexity: O(8(b + 4^8))
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank) -> int:
      bankSet = set(bank)
      # base case
      if endGene not in bankSet:
        return -1

      GENE_STRINGS = ['A', 'C', 'G', 'T']

      mutations = 0

      q = deque([startGene])
      seen = {startGene}

      while q:

        for _ in range(len(q)):
          node = q.popleft()

          if node == endGene:
            return mutations

          # add currentNode's valid combination neighbors to the queue
          for i in range(len(node)):

            for GENE in GENE_STRINGS:
              newNode = node[:i] + GENE + node[i + 1:]

              # check newNode is valid
              if newNode in bank and newNode not in seen:
                seen.add(newNode)
                q.append(newNode)

        mutations += 1

      return -1



solution = Solution()


startGene = "AACCTTGG"
endGene = "AATTCCGG"
bank = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]

print("res:", solution.minMutation(startGene, endGene, bank))


# return min steps to reach endGene starting from startGene
# if endGene is not in bank return -1
# start to endGene
# EVERY DIFFERENT COMBINATIONS THAT CREATE MUST BE IN THE BANK


"""

CREATE EVERY POSSIBLE COMBINATIONS USING 

IF COMBINATIONS ARE VALID CONTINUE WITH new combinations

once combinations reach the endGene return true


"A C G T"


AACCGGTT
  A:
  aACCGGTT
  AaCCGGTT
  AAaCGGTT
  AACaGGTT
  AACCaGTT
  AACCGaTT
  AACCGGaT
  AACCGGTa

  C:
  cACCGGTT
  AcCCGGTT
  AAcCGGTT
  AACcGGTT
  AACCcGTT
  AACCGcTT
  AACCGGcT
  AACCGGTc





"""
