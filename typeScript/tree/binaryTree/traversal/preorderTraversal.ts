import { TreeNode } from '../../lib/TreeNode';

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

function preOrderTraversal1(root: ITreeNode) {
  const answer: number[] = [];

  preOrder(root);

  function preOrder(root: ITreeNode | null) {
    if(root === null) {
      return [];
    }

    answer.push(root.val);
    preOrder(root.right);
    preOrder(root.left);
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
const node3 = new TreeNode(2);
const node4 = new TreeNode(3);
const node5 = new TreeNode(3);
const node6 = new TreeNode(4);
const node7 = new TreeNode(4);

node1.left = node2;
node1.right = node3;

node2.left = node4;
node2.right = node6;


node3.left = node7;
node3.right = node5;



console.log(preOrderTraversal(node1.left));
console.log(preOrderTraversal1(node1.right));
