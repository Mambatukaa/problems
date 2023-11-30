// Recursive
// Time Complexity: O(n)
// Space Complexity: O(n)
const countGoodNodes = (root) => {
  const count = (root, currMax) => {
    // base case
    if(!root) {
      return 0;
    }

    const left = count(root.left, Math.max(root.val, currMax));
    const right = count(root.right, Math.max(root.val, currMax));

    let answer = left + right;

    if(root.val >= currMax) {
      answer++;
    }

    return answer;
  }

  count(root, -Infinity);
}

// Iterative
// Time Complexity: O(n)
// Space Complexity: O(1)
const countGoodNodesII = (root) => {
  if(!root) {
    return 0;
  }

  let counter = 0;

  const stack = [[root, -Infinity]];

  while(stack.length) {
    let [curr, currMax] = stack.pop();

    if(curr.val >= currMax) {
      counter++;
    };

    if(curr.left) {
      stack.push([curr.left, Math.max(curr.val, currMax)])
    }

    if(curr.right) {
      stack.push([curr.right, Math.max(curr.val, currMax)])
    }
  }

  return counter;
}

class BT {
  constructor(val) {
    this.val = val;

    this.left = null;
    this.right = null;
  }
}

const root = new BT(3);

const node1 = new BT(1);
const node2 = new BT(4);

const node3 = new BT(4);
const node4 = new BT(5);

root.left = node1;
root.right = node2;

node1.left = node3;
node2.right = node4;

console.log('answer:', countGoodNodesII(root));
