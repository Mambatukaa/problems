# Time Complexity: O(n)
# Space Complexity: O(1)
class FreqStack(object):

    def __init__(self):
      self.cnt = {}
      self.maxCnt = 0
      self.stacks = {}


    def push(self, val):
      valCnt = 1 + self.cnt.get(val, 0)

      self.cnt[val] = valCnt

      if valCnt > self.maxCnt:
        self.maxCnt = valCnt
        self.stacks[valCnt] = []

      self.stacks[valCnt].append(val)

    def pop(self):
      res = self.stacks[self.maxCnt].pop()

      self.cnt[res] -= 1

      if not self.stacks[self.maxCnt]:
        self.maxCnt -= 1
      return res



freqStack = FreqStack()

freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)

print(freqStack.pop())
print(freqStack.pop())


