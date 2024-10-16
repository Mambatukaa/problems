# Time Complexity: O(n)
# Space Complexity: O(n)
# Iterative Bottom Up solution
def solvingQuestions(questions):
  n = len(questions)
  dp = [0] * n

  dp[n - 1] = questions[n - 1][0]

  for i in range(n - 2, -1, -1):

    point, brainPower = questions[i]
    
    idxAfterSkip = i + brainPower + 1 

    if idxAfterSkip < n:
      # possible to answer more questions
      point += dp[idxAfterSkip]

    dp[i] = max(point, dp[i + 1])
  
  return max(dp)


questions = [[3, 2], [4, 0], [4, 4], [10, 5]]

print("res:", solvingQuestions(questions))
"""


You are given a 0-indexed 2D integer array questions where questions [i] = [pointsi, brainpoweril.
The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision
whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri
questions. If you skip question i, you get to make the decision on the next question.

• For example, given questions = [[3, 2], [4, 3], [4, 41, [2, 5]]:
• If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
• If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.





Example 1:
Input: questions = [[3,2], [4,3], [4,4], [2,5]]
Output: 5

Explanation: The maximum points can be earned by solving questions @ and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.

"""
