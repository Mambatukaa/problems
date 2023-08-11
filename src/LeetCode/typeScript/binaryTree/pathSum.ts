import { TreeNode } from './TreeNode';

// Time Complexity: O(n)
// Space Complexity: O(n)
const hasPathSum = (root: TreeNode | null, sum: number, pos?: string): boolean => {
  if(!root) {
    return false;
  }

  console.log(root.val, pos)
  sum -= root.val;

  if(!root.left && !root.right) {
    console.log("response: ", sum === 0)
    return sum === 0;
  }

  return hasPathSum(root.left, sum, "left") || hasPathSum(root.right, sum, "right");
}


// Time Complexity: O(n)
// Space Complexity: O(n)
const hasPathSumIteration = (root: TreeNode | null, sum: number): boolean => {
  if(!root) {
    return false;
  }

  const nodeStack: any[] = [];
  const sumStack: number[] = [];

  nodeStack.push(root);
  sumStack.push(sum - root.val);

  while(nodeStack.length) {
    const node = nodeStack.pop();
    const currSum: any = sumStack.pop();

    console.log(node.val, ' value');
    console.log(currSum, ' sum');

    if(!node.right && !node.left && currSum === 0) {
      return true;
    }

    if(node.right) {
      nodeStack.push(node.right);
      sumStack.push(currSum - node.right.val);
    }

    if(node.left) {
      nodeStack.push(node.left);
      sumStack.push(currSum - node.left.val);
    }

  }

  return false;
}

const node1 = new TreeNode(1);
const node2 = new TreeNode(-2);
const node3 = new TreeNode(-3);
const node4 = new TreeNode(1);
const node5 = new TreeNode(3);
const node6 = new TreeNode(-2);
const node7 = new TreeNode(-1);


node1.left = node2;
node1.right = node3;

node2.left = node4;
node2.right = node5;

node3.left= node6;

node4.left = node7;


console.log(hasPathSumIteration(node1, -1));
