class Solution:
    # Time Complexity: O(n log n + m log m + n * m)
    # Space Complexity: O(1)
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()


        n = len(players)
        m = len(trainers)

        j = 0
        res = 0

        for player_index in range(n):
            player = players[player_index]

            for trainer_index in range(j, m):
                trainer = trainers[trainer_index]

                if player <= trainer:
                    res += 1
                    j = trainer_index + 1
                    break

                if j == m - 1:
                    break


        return res
        


# Time Complexity: O(n log n + m log m + n)
# Space Complexity: O(1)
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        n = len(players)
        m = len(trainers)

        res = i = j = 0

        while i < n and j < m:
            while j < m and players[i] > trainers[j]:
                j += 1

            if j < m:
                res += 1

            i += 1
            j += 1

        return res


"""

# trainer can be matched with at most one player
# player can be matched with at most one trainer
# they can't match if the trainers ability is less than or equal to the trainer's training capacity


players = [4, 7, 9]
trainers = [8, 2, 5, 8]

Output: 2


4 <= 8
7 <= 8

Sort the players and trainers

[4, 7, 9]

[2, 5, 8, 8]

1. Brute force

    j = 0 # matching trainer index
    a. iterate through players and find the matching trainer
        for player_index in range(n):
            for trainer_index in range(j, m):
                if player <= trainer:
                    res += 1
                    j = trainer_index
                    break

            if j == m - 1:
                break


    return res













"""