/**
 * Definition for a binary tree node.
 */

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
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
node2.right = node5;

node3.left = node6;

const inorder = (root: TreeNode | null) => {
  let curr = root;
  let rightMost;

  while (curr) {
    if (!curr.left) {
      console.log(curr.val);
      curr = curr.right;
    } else {
      rightMost = curr.left;

      while (rightMost.right) {
        rightMost = rightMost.right;
      }

      rightMost.right = curr;

      const temp = curr.left;
      curr.left = null;
      curr = temp;
    }
  }
};

inorder(node1);
