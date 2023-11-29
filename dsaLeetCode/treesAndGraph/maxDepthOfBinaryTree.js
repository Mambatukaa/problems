// Space Complexity: O(n)
// Time Complexity: O(n)
const maxDepth = (root) => {
  if(!root) {
    return 0;
  }

  const leftMax = maxDepth(root.left);
  const rightMax = maxDepth(root.right);

  return Math.max(leftMax, rightMax) + 1;
};

// Space Complexity: O(1)
// Time Complexity: O(n)
const maxDepthIterative = (root) => {
  if(!root) {
    return 0;
  }

  const stack = [[root, 1]];
  let maxDepth = 1;

  while(stack.length) {
    const [curr, depth] = stack.shift();

    if(curr.left) {
      stack.unshift([curr.left, depth + 1]);
    }

    if(curr.right) {
      stack.unshift([curr.right, depth + 1]);
    }

    maxDepth = Math.max(maxDepth, depth);
  }

  return maxDepth;
}


class BT {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}


const root = new BT(0);

const node1 = new BT(1);
const node2 = new BT(2);

const node3 = new BT(3);
const node4 = new BT(4);

const node5 = new BT(5);
const node6 = new BT(6);


root.left = node1;
root.right = node2;

node1.left = node3;
node1.right = node4;

node2.right = node5;
node5.right = node6;

console.log(maxDepthIterative(root));
