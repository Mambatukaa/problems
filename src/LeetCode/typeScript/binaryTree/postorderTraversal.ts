import { TreeNode } from './TreeNode';

// Time Complexity: O(n)
// Space Complexity: O(n)
function postorderTraversalRecursive(root: TreeNode | null) {
  const answer: number[] = [];

  function postorder(root: TreeNode | null) {
    if(root === null) {
      return [];
    }

    postorder(root.left);
    postorder(root.right);
    answer.push(root.val);
  }

  postorder(root);

  return answer;
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

console.log(postorderTraversalRecursive(node1));
