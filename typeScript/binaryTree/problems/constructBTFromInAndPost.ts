import { TreeNode } from '../lib/TreeNode';

const construct = (inorder: TreeNode, postorder: TreeNode) => {
  console.log(inorder, postorder);
}


const node1 = new TreeNode(1);
const node2 = new TreeNode(1);

construct(node1, node2);

