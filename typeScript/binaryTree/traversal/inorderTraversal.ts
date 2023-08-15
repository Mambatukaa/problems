import { TreeNode } from '../lib/TreeNode';

// Time Complexity: O(n)
// Space Complexity: O(n)
function inorderTraversal(root: TreeNode | null): number[] {
  const answer: number[] = [];
  inorder(root);

  function inorder(root: TreeNode | null) {
    if(root === null) {
      return [];
    }

    inorder(root.left);
    answer.push(root.val);
    inorder(root.right);
  }

  return answer;
}


// Time Complexity: O(n)
// Space Complexity: O(n)
function inorderTraversalIteration(root: TreeNode | null): number[] {
  const answer: any[] = [];
  const stack: Array<TreeNode | null> = [];

  let curr: any = root;

  while(curr || stack.length) {

    while(curr) {
      stack.push(curr);
      curr = curr.left;
    }

    curr = stack.pop();
    answer.push(curr.val);
    curr = curr.right;
  }

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


console.log(inorderTraversal(node1));
console.log(inorderTraversalIteration(node1));
