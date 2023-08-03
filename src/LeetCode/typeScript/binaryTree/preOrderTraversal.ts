import { TreeNode } from './TreeNode';

interface ITreeNode {
  val: number;
  left: ITreeNode | null;
  right: ITreeNode | null;
}

// Time complexity: O(n)
// Space complexity: O(n)
function preOrderTraversal(root: ITreeNode) {
  const answer: number[] = [];

  preOrder(root);

  function preOrder(root: ITreeNode | null) {
    if(root === null) {
      return [];
    }

    answer.push(root.val);
    preOrder(root.left);
    preOrder(root.right);
  }


  return answer;
}

// Time complexity: O(n)
// Space complexity: O(n)
function preOrderTraversalIteration(root: ITreeNode | null) {
  const stack: Array<ITreeNode | null> = [];
  const answer: Array<number> = [];

  stack.push(root);

  while(stack.length) {
    const currNode = stack.pop();

    if(currNode) {
      answer.push(currNode.val);
      stack.push(currNode.right);
      stack.push(currNode.left);
    }

  }

  return answer;
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

node1.left = node2;
node1.right = node3;

node2.left = node4;
node2.right = node5;


node3.left = node6;
node3.right = node7;

node4.left = node8;
node4.right = node9;

node5.left = node10;


console.log(preOrderTraversal(node1));
console.log(preOrderTraversalIteration(node1));
