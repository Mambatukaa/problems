const findInOrderSuccessorII = (root, inputNode) => {
  if(!root) {
    return null;
  };

  let successor = null;
  let isFound = false;

  const helper = (root) => {
    if(!root) {
      return;
    };


    helper(root.left);

    if(!successor && isFound) {
      successor = root.val;
    };

    if(root.val === inputNode) {
      isFound = true;
    };

    helper(root.right);
  };

  if(root.val <= inputNode) {
    helper(root.right);
  } else {
     helper(root.left);
  }; 

  if(isFound && !successor) {
    successor = root.val;
  };


  return successor;

};

  function findInOrderSuccessor(inputNode) {
    if (inputNode.right != null) {
     return findMinKeyWithinTree(inputNode.right)
    };

    let ancestor = inputNode.parent
    let child = inputNode

    while (ancestor != null && child == ancestor.right) {
      child = ancestor;
      ancestor = child.parent;
    };

    return ancestor
}

function findMinKeyWithinTree(inputNode) {
  while (inputNode.left != null) {
      inputNode = inputNode.left
  }

  return inputNode
}


class BinaryNode {
  constructor(val) {
    this.val = val;
    this.right = null;
    this.left = null;
    this.parent = null;
  };
};

const root = new BinaryNode(20);

const node2 = new BinaryNode(9);
const node3 = new BinaryNode(25);

const node4 = new BinaryNode(5);
const node5 = new BinaryNode(12);

const node6 = new BinaryNode(11);
const node7 = new BinaryNode(14);

root.left = node2;
root.right = node3;

node2.left = node4;
node2.right = node5;


node5.left = node6;
node5.right = node7;

node2.parent = root;
node3.parent = root;
node4.parent = node2;
node5.parent = node2;

node6.parent = node5;
node7.parent = node5;

console.log(findInOrderSuccessor(root, node2).val);

/*
                   20
                /      \
             9            25
           /   \            
         5       12   
               /    \
            11        14




in order successor (9)  ====> 11;
in order successor (14) ====> 20;

left => root => right (inorder)

inOrder ===> 5 => 9 => 11 => 12 => 14 => 20 =>


1. Do inOrder traversal if value found return next node.value
2. If value doesn't found return false;

 */
