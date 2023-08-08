
import { TreeNode } from './TreeNode';


// Top --> Bottom solution
function findMaxDepth(root: TreeNode | null): number {
  let depth: number = 1;
  let max: number = 0;

  find(root, depth);

  function find(root: TreeNode | null, depth: number) {
    if(!root) {
      return;
    }

    if(!root.right && !root.left ) {
      max = Math.max(depth, max); 
    }

    find(root.left, depth + 1);
    console.log(root.val, '------------', depth);
    find(root.right, depth + 1);
  }

  return max;
}


// Bottom --> Up solution
function maxDepth(root: TreeNode | null): number {
  if(!root) {
    return 0;
  }

  const leftDepth = maxDepth(root.left);
  const rightDepth = maxDepth(root.right);

  console.log(root.val, leftDepth, rightDepth);

  return Math.max(leftDepth, rightDepth) + 1;
}

const node1 = new TreeNode(1);
const node2 = new TreeNode(2);
const node3 = new TreeNode(3);
const node4 = new TreeNode(4);
const node5 = new TreeNode(5);

const node6 = new TreeNode(6);

node1.left = node2;
node1.right = node3;

node2.left = node4;
node2.right = node5

node4.left = node6;


console.log(maxDepth(node1));
