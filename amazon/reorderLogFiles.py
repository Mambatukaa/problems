# Time Complexity: O(n log n)
# Space Complexity: O(n + m)
def reorderLogFiles(logs):
  letterLogs = []
  digitLogs = []

  for log in logs:
    if log.split()[1].isnumeric():
      digitLogs.append(log)
      continue

    letterLogs.append(log)

  letterLogs.sort(key = lambda log: log.split()[0])            #when suffix is tie, sort by identifier
  letterLogs.sort(key = lambda log: log.split()[1:])           #sort by suffix

  return letterLogs + digitLogs

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

print('res:', reorderLogFiles(logs))

"""

Letter logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits



Reorder these logs so that:
1. The letter-logs come before all digit-logs.
2. The letter-logs are sorted lexicographically by their contents. 
    If their contents are the same, then sort them
      lexicographically by their identifiers.

3. The digit-logs maintain their relative ordering.


Return the final order of the logs.




1. Separate logs by letter logs and digits logs.
2. Sort the each logs.
3. Merge the logs and return

"""
