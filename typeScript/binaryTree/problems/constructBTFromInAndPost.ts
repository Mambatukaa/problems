import { TreeNode } from '../lib/TreeNode';

const construct = (inorder: TreeNode, postorder: TreeNode) => {
  console.log(inorder, postorder);
}

const inorderRoot = new TreeNode(1);
const postorderRoot  = new TreeNode(1);

construct(inorderRoot, postorderRoot);

