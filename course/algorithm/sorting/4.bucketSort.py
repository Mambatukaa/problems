import math

# Time Complexity: O(n log n) 
# Space Complexity: O(n)
def bucketSort(arr):
  
  numberOfBuckets = math.ceil(math.sqrt(len(arr)))

  maxValue = max(arr)

  buckets = [[] for i in range(numberOfBuckets)]

  for val in arr:
    bucketNumber = math.ceil(val * numberOfBuckets / maxValue)

    buckets[bucketNumber - 1].append(val)

  print("Printing buckets before sorting: ", buckets)

  idx = 0

  for bucket in buckets:
    bucket.sort()

    # NOTE add to array
    for val in bucket:
      arr[idx] = val
      idx += 1

  print("Printing buckets after sorting: ", buckets)


  return arr

arr = [1, 2, 4, 5, 3, 8, 7, 9]


print("Res:", bucketSort(arr))



"""
When to use Bucket sort?
  - When input uniformly distributed over range.
    1, 2, 4, 5, 3, 8, 7, 9

  NOT XXXXX 1, 2, 4, 91, 93, 95


When to avoid Bucket Sort?
  - When space is concern




"""
