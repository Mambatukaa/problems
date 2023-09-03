import { TreeNode } from '../lib/TreeNode';

// Space Complexity: O(n)
// Time Complexity: O(n ^ 2)
const buildTree = (inorder: number[], postorder: number[]) => {
  if(!inorder.length) {
    return;
  }

  const root: any = new TreeNode(postorder.pop());

  const idx = inorder.indexOf(root.val);

  root.right = buildTree(inorder.slice(idx + 1), postorder);
  root.left = buildTree(inorder.slice(0, idx), postorder);
   
  return root;
}

// Space Complexity: O(n)
// Time Complexity: O(n)

const buildTreeII = (inorder: number[], postorder: number[]) => {
  const hash: any = {};

  for(let i = 0; i < inorder.length; i++) {
    hash[inorder[i]] = i;
  }
  console.log(hash);

  const recurs = (start: number, end: number) => {
    if(start > end) {
      return null;
    }

    const root: any = new TreeNode(postorder.pop());
    const index = hash[root.val];

    root.right = recurs(index + 1, end);
    console.log(start, '----', index)
    root.left = recurs(start, index - 1);

    return root;
  }

  return recurs(0, inorder.length - 1);
}

const inorderRoot = [4,2,5,1];
const postorderRoot = [4,5,2,1];

console.log(buildTreeII(inorderRoot, postorderRoot));
