# Time Complexity: O(n log n + m log m)
# Space Complexity: O(1)
# Greedy
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
      players.sort()
      trainers.sort()

      res = 0
      i = 0

      for trainer in trainers:
        if trainer >= players[i]:
          # matched
          res += 1
          i += 1

          if i == len(players):
            break

      return res
        
