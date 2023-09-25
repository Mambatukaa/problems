// Time Complexity: O(n)
// Space Complexity: O(n)
const solution = (root) => {
  let sum = 0;

  const helper = (root, level) => {
    if(!root) {
      return;
    }

    sum += level;

    helper(root.left, level + 1);
    helper(root.right, level + 1);
  }

  helper(root, 0);

  return sum;
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const solutionII = (root) => {
  const queue = [];

  queue.push([root, 0]);

  let sum = 0;

  while(queue.length) {
    [curr, level] = queue.shift(); 

    sum += level;

    if(curr.left) {
      queue.push([curr.left, level + 1]);
    }

    if(curr.right) {
      queue.push([curr.right, level + 1]);
    }

  }

  console.log(sum);

  return sum;
}


class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}


const root = new BinaryTree(1);

const node2 = new BinaryTree(2);
const node3 = new BinaryTree(3);

const node4 = new BinaryTree(4);
const node5 = new BinaryTree(5);

const node6 = new BinaryTree(6);
const node7 = new BinaryTree(7);

const node8 = new BinaryTree(8);
const node9 = new BinaryTree(9);

root.left = node2;
root.right = node3;

node2.left = node4;
node2.right = node5;

node3.left = node6;
node3.right = node7;

node4.left = node8;
node5.right = node9;

solutionII(root);
