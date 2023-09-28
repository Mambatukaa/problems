/*
 All leaf nodes in the tree represents operands, which will always be positive integers. All of the other nodes represesnt operators.
 -1: + Addition operator, adding the left and right subtrees,
 -2: - Subtraction opeartor, subtracting the right sub tree from the left subtree,
 -3: / Division operator, dividing the left subtree by the right subtree. If the result is a decimal,
 it should be roundad to zero
 -4 * Multiplication operator, multiplying the left and right subtrees.

 */

// Time Complexity: O(n)
// Space Complexity: O(h) h === height
const solution = (tree) => {
  if(tree.value >= 0) {
    return tree.value;
  }

  const leftValue = solution(tree.left);
  const rightValue = solution(tree.right);


  if(tree.value === -1) {
    return leftValue + rightValue;
  }

  if(tree.value === -2) {
    return leftValue - rightValue;
  }

  if(tree.vlaue === -3) {
    return Math.trunc(leftValue / rightValue);
  }

  return leftValue * rightValue;
}


class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
};


const root = new BinaryTree(-1);

const node1 = new BinaryTree(-2);
const node2 = new BinaryTree(-3);

const node3 = new BinaryTree(-4);
const node4 = new BinaryTree(2);

const node5 = new BinaryTree(8);
const node6 = new BinaryTree(3);

const node7 = new BinaryTree(2);
const node8 = new BinaryTree(3);


root.left = node1;
root.right = node2;

node1.left = node3;
node1.right = node4;

node2.left = node5;
node2.right = node6;

node3.left = node7;
node3.right = node8;


const testRoot = new BinaryTree(-1);

const testNode1 = new BinaryTree(-1);
const testNode2 = new BinaryTree(-2);

const testNode3 = new BinaryTree(-4);
const testNode4 = new BinaryTree(-3);

const testNode5 = new BinaryTree(6);
const testNode6 = new BinaryTree(5);

const testNode7 = new BinaryTree(5);
const testNode8 = new BinaryTree(5);

const testNode9 = new BinaryTree(8);
const testNode10 = new BinaryTree(2);

testRoot.left = testNode1;
testRoot.right = testNode2;

testNode1.left = testNode3;
testNode1.right = testNode4;

testNode2.left = testNode5;
testNode2.right = testNode6;

testNode3.left = testNode7;
testNode3.right = testNode8;

testNode4.left = testNode9;
testNode4.right = testNode10;

console.log(solution(root));
