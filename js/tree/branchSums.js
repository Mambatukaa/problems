// Pre-order traversal
// Time Complexity: O(n)
// Space Complexity: O(n)
const solution = (root, sum) => {

  const answer = [];

  const branchSums = (root, sum, answer) => {
    if(!root) {
      return;
    }

    sum += root.value;

    if(!root.left && !root.right) {
      answer.push(sum);
    }

    branchSums(root.left, sum, answer);
    branchSums(root.right, sum, answer);
  }

  branchSums(root, 0, answer);

  return answer;
}

// Pre-order traversal // loop
// Time Complexity: O(n)
// Space Complexity: O(1)
const solutionII = (root) => {
  let sum = root.value;
  let curr = root;
  const answer = [];

  const stack = [[curr, sum]];

  while(stack.length) {
    [curr, sum] = stack.pop();


    if(!curr.left && !curr.right) {
      answer.push(sum);
      continue;
    }

    if(curr.right) {
      stack.push([curr.right, sum + curr.right.value]);
    }

    if(curr.left) {
      stack.push([curr.left, sum + curr.left.value]);
    }

  }

  return answer;
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

const node10 = new BinaryTree(10);

root.left = node2;
root.right = node3;

node2.left = node4;
node2.right = node5;

node3.left = node6;
node3.right = node7;

node4.left = node8;
node4.right = node9;

node5.left = node10;

console.log(solutionII(root));
