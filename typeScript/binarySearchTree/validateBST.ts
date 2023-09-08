import { TreeNode } from '../binaryTree/lib/TreeNode';

const root = new TreeNode(0);
const node1 = new TreeNode(1);
const node2 = new TreeNode(-1);
const node3 = new TreeNode(3);


const node5 = new TreeNode(5);
const node6 = new TreeNode(6);
const node7 = new TreeNode(7);

root.right = node2;



// in order traversal
// Time Complexity: O(n)
// Space Complexity: O(n)
const isValidBST = (root: TreeNode | null) => {
  let prev: TreeNode;

  const isValid = (root: TreeNode | null) => {
    if(!root) {
      return true;
    }

    if(!isValid(root.left)) {
      return false;
    }

    console.log(root.val);

    if(prev && prev.val > root.val) {
      return false;
    }

    prev = root;


    if(!isValid(root.right)) {
      return false;
    }

    return true;
  }

  return isValid(root);
}

const isValidBSTII = (root: TreeNode | null) => {
  const isValid = (root: TreeNode | null, low: number | null, high: number | null): boolean => {
    if(!root) {
      return true;
    }

    console.log(root.val, low, high);

    if(low !== null && low >= root.val || high !== null && high <= root.val) {
      return false;
    }


    return isValid(root.left, low, root.val) && isValid(root.right, root.val, high);
  }

  return isValid(root, null, null);
}

console.log(isValidBSTII(root));
