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


const node1 = new TreeNode(1);
const node2 = new TreeNode(2);
const node3 = new TreeNode(3);
const node4 = new TreeNode(4);
const node5 = new TreeNode(5);
const node6 = new TreeNode(6);
const node7 = new TreeNode(7);

node1.left = node2;
node1.right = node3;

node2.left = node4;
node2.right = node5;


node3.left = node6;
node3.right = node7;


console.log(hasPathSum(node1, 1111));
