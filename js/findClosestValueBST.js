// naive
// Time Complexity: O(logn)
// Time Complexity: O(n) worst
// Space Complexity: O(1)
const findClosestValueBST = (tree, target) => {
  if(!tree) {
    return null;
  }

  let diff = Math.abs(target - tree.value);
  let closest = tree.value;
  let curr = tree;


  while(curr) {
    const value = curr.value;

    if(value === target) {
      return target;
    }

    if(Math.abs(value - target) < diff) {
      diff = Math.abs(value - target);

      closest = value;
    }

    if(value > target) {
      // goLeft 
      curr = curr.left;
    } else {
      curr = curr.right;
    }
  }

  return closest;
}


class BST {
  constructor(val) {
    this.value = val;
    this.right = null;
    this.left = null;
  }
};


const root = new BST(10);

const node2 = new BST(5);
const node3 = new BST(15);

const node4 = new BST(2);
const node5 = new BST(5);

const node6 = new BST(13);
const node7 = new BST(22);


root.left = node2;
root.right = node3;

node2.left = node4;
node2.right = node5;

node3.left = node6;
node3.right = node7;

console.log(findClosestValueBST(root, 12));
