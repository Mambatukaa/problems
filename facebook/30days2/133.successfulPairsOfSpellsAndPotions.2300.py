"""
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
 

Constraints:

n == spells.length
m == potions.length
1 <= n, m <= 105
1 <= spells[i], potions[i] <= 105
1 <= success <= 1010

"""

"""
Complexity Analysis
Here, n is the number of elements in the spells array, and m is the number of elements in the potions array.

Time complexity: O(nlogn+mlogm)

We create an array sortedSpells which takes O(n) time, and then sort the sortedSpells and potions arrays which take O(nlogn) and O(mlogm) time respectively.
Then using two pointers we iterate on each element of the sortedSpells and potions arrays once which will take O(n+m) time.
Thus, overall we take O(nlogn+mlogm) time.
Space complexity: O(n+logm) or O(n+m)

The output array answer is not considered as additional space usage.
But we create an additional array sortedSpells which will take O(n) space.
And some extra space is used when we sort the sortedSpells and potions array in place. The space complexity of the sorting algorithm depends on the programming language.
In Python, the sort() method sorts a list using the Timsort algorithm which has O(m) additional space where m is the number of the elements.
In C++ and Swift, the sort() function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with a worst-case space complexity of O(logm).
In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm which has a space complexity of O(logm).
In JavaScript, the space complexity of sort() is O(logm).
Thus, sorting uses either O(logn+logm) or O(n+m) space.
In Swift, we need to create an additional array for keeping sorted potions which will take an additional O(m) space.
So, overall we usem O(n+logn+logm)=O(n+logm) or O(n+n+m)=O(n+m) space.


"""
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sortedSpells = [(spell, index) for index, spell in enumerate(spells)]

        # Sort the 'spells with index' and 'potions' array in increasing order.
        sortedSpells.sort()
        potions.sort()

        answer = [0] * len(spells)
        m = len(potions)
        potionIndex = m - 1
        
        # For each 'spell' find the respective 'minPotion' index.
        for spell, index in sortedSpells:
            while potionIndex >= 0 and (spell * potions[potionIndex]) >= success:
                potionIndex -= 1
            answer[index] = m - (potionIndex + 1)
        
        return answer


"""


spells = [5,1,3], 
potions = [1,2,3,4,5], 
success = 7


spells_sorted = (1, 1), (3, 2), (5, 0)
potions_sorted = [1, 2, 3, 4, 5]

"""





"""

Complexity Analysis
Here, n is the number of elements in the spells array, and m is the number of elements in the potions array.

Time complexity: O((m+n)⋅logm)

We sort the potions array which takes O(mlogm) time.
Then, for each element of the spells array using binary search we find the respective minPotion which takes O(logm) time. So, for n elements it takes O(nlogm) time.
Thus, overall we take O(mlogm+nlogm) time.
Space complexity: O(logm) or O(m)

The output array answer is not considered as additional space usage.
But some extra space is used when we sort the potions array in place. The space complexity of the sorting algorithm depends on the programming language.
In Python, the sort() method sorts a list using the Timsort algorithm which has O(m) additional space where m is the number of the elements.
In C++ and Swift, the sort() function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with a worst-case space complexity of O(logm).
In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm which has a space complexity of O(logm).
In JavaScript, the space complexity of sort() is O(logm).
In Swift, we need to create an additional array for keeping sorted potions which will take O(m) space.

"""
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        # sort potions 
        # and find the left most successfull position
        # spells will be successfull after left most location to n
        potions.sort()
        n = len(potions)


        def findLeftMost(spell):
            l = 0
            r = n - 1

            while l < r:
                mid = l + (r - l) // 2

                is_successful = potions[mid] * spell >= success

                if is_successful:
                    # go left
                    r = mid
                else:
                    # go right
                    l = mid + 1
            
            return r

        res = []
        maxPotion = potions[n - 1]

        for spell in spells:
            # spell * minPotion ≥ success VALID 
            minPotion = math.ceil(success / spell)
            if minPotion > maxPotion:
                res.append(0)
                continue

            # find the left most on each spell and add to range to the answer
            # left_most = findLeftMost(spell)

            # We can use the found potion, and all potion in its right
            # (as the right potions are greater than the found potion).
            index = bisect.bisect_left(potions, minPotion)

            res.append(n - index)

        return res




        
"""
s = 5
success = 7


    L
M
  R
1 2 3 4 5 
0 1 2 3 4

5 - 1 = 4

3 * 5 = 15 >= 7
2 * 5 = 10 >= 7
1 * 5 = 5 >= 7 FALSE


          L 
        M
        R
1 2 3 4 5 
0 1 2 3 4



[1,2,3,4,5,6,7]

spell = 4
success = 25

            L           
            M
            R
1 2 3 4 5 6 7 
0 1 2 3 4 5 6

4 * 4 = 16 >= 25 F
6 * 4 = 24 >= 25 F


"""