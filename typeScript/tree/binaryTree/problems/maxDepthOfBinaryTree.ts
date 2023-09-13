import { TreeNode } from '../../lib/TreeNode';


// Time Complexity: O(n)
// Space Complexity: O(n)
const maxDepth = (root: TreeNode | null): number => {
  if(!root) {
    return 0;
  }

  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}

const max = (root: TreeNode | null): number => {

  return 1;
}

const node1 = new TreeNode(1);
const node2 = new TreeNode(2);
const node3 = new TreeNode(3);
const node4 = new TreeNode(4);
const node5 = new TreeNode(5);

node1.left = node2;
node1.right = node3;

node2.left = node4;
node2.right = node5


console.log(maxDepth(node1));
