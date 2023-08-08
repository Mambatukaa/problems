import { TreeNode  } from './TreeNode';


// Time Complexity: O(n)
// Space Complexity: O(n)
function levelorderTraversalRecursive(root: TreeNode | null) {
  // 1 - 2 - 3 - 4 - 5
   const levels: number[][] = [];

   if(root === null) {
     return levels
   }

   helper(root, 0);

  function helper(node: TreeNode, level: number) {
    if(levels.length === level) {
      levels.push([]);
    }

    levels[level].push(node.val);

    if(node.left) {
      helper(node.left, level + 1);
    }

    if(node.right) {
      helper(node.right, level + 1);
    }

  }

  console.log(levels);

   return levels;
}

const node1 = new TreeNode(1);
const node2 = new TreeNode(2);
const node3 = new TreeNode(3);
const node4 = new TreeNode(4);
const node5 = new TreeNode(5);
const node6 = new TreeNode(6);
const node7 = new TreeNode(7);
const node8 = new TreeNode(8);
const node9 = new TreeNode(9);
const node10 = new TreeNode(10);
const node11 = new TreeNode(11);
const node12 = new TreeNode(12);
const node13 = new TreeNode(13);
const node14 = new TreeNode(14);
const node15 = new TreeNode(15);

node1.left = node2;
node1.right = node3;


node1.left = node2;
node1.right = node3;

node2.left = node4;
node2.right = node5

node3.left = node6;
node3.left = node7;

node4.left = node8;
node4.right = node9;

node5.left = node10;
node5.right = node11;


node6.left = node12;
node6.right = node13;

node7.left = node14;
node7.right = node15;

levelorderTraversalRecursive(node1);
