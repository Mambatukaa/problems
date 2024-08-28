# You must implement a solution with 0(1) time complexity for each function.


# Using one stack
# Time Complexity: O(1)
# Space Complexity: O(n)
class MinStack:
  def __init__(self):
    # [el, currMin]
    self.stack = []

    print("Successfully created min stack.")

  def push(self, val):

    # if stack has no element
    if not self.stack:
      self.stack.append([val, val])
      return

    currMin = min(val, self.stack[-1][1])
    self.stack.append([val, currMin])


  def pop(self):
    self.stack.pop()

  def top(self):
    return self.stack[-1][0]

  def getMin(self):
    return self.stack[-1][1]


# Using two stacks
# Time Complexity: O(1)
# Space Complexity: O(n)
class MinStackII:
  def __init__(self):
    self.stack = []
    self.minStack = []

  def push(self, val):
    if not self.stack:
      self.stack.append(val)

      # since stack is empty val is also min val
      self.minStack.append(val)

      return

    # add value to the stack
    self.stack.append(val)

    # since it's LAST IN FIRST OUT if value is min add to the minStack otherwise not

    if self.minStack[-1] >= val:
      self.minStack.append(val)

  def pop(self):
    curr = self.stack.pop()

    # if curr value is current min remove it from minStack
    if curr == self.minStack[-1]:
      self.minStack.pop()

  def top(self):
    return self.stack[-1]

  def getMin(self):
    return self.minStack[-1]

minStack = MinStackII()

minStack.push(-2)

minStack.push(0)

minStack.push(-3)

print(minStack.getMin())

minStack.pop()

print(minStack.top())
print(minStack.getMin())


"""

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
  • MinStack() initializes the stack object.
  • void push(int val) pushes the element val onto the stack.
  • void pop() removes the element on the top of the stack.
  • int top() gets the top element of the stack.
  • int getMin() retrieves the minimum element in the stack.

You must implement a solution with 0(1) time complexity for each function.


Constraints:

-2^31 <= val <= 2^31 - 1

  Methods pop, top and getMin operations will always be called on non-empty stacks.
  At most 3 * 10^4 calls will be made to push, pop, top, and getMin.


******************************************************************************************


STACK - LAST IN FIRST OUT



"""
