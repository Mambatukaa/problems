# Greedy
# Two pointers
class Solution:
    def numRescueBoats(self, people, limit):
      people.sort()

      l = 0
      r = len(people) - 1

      counter = 0

      while l <= r:
        pair = people[l] + people[r]

        if pair <= limit:
          l += 1

        r -= 1

        counter += 1

      return counter


solution = Solution()

people = [2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10]
limit = 50

solution.numRescueBoats(people, limit)


"""
                   l
                      r
people = [1, 1, 2, 3, 3] limit = 8

two pointers 

  if they fit together 
    move 2 pointers
  
  if they don't fit
    move the right pointer
  



"""
        
