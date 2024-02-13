/*
 
                1
              /   \ 
             2     3
            / \
           4   5

====> 3 (5,2,1,3), (4,2,1,3);


               1
              /   
             2     
            / \ 
           4   5
          /     \
         8       9
        /         \
       10         12


    fn = (root) => {
      if(!root) {
        return -1;
      }

      const left = 1 + fn(root.left);
      const right = 1 + fn(root.right);

      max = max(left + right, max);

      return max(left, right);
    }

 
 */

class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  };
};


class BinaryTree {
  constructor() {
    this.root = null;
  };


  insert(val) {
    const newNode = new TreeNode(val);

    if(!this.root) {
      this.root = newNode;
    } else {
      const queue = [this.root];

      while(queue.length) {
        const curr = queue.shift();

        if(!curr.left) {
          curr.left = newNode;
          return;
        };

        if(!curr.right) {
          curr.right = newNode;
          return;
        };

        queue.push(curr.left);
        queue.push(curr.right);

      };

    };
  }
};

const root = new TreeNode(1);
const node2 = new TreeNode(2);

const node3 = new TreeNode(4);
const node4 = new TreeNode(5);

const node5 = new TreeNode(8);
const node6 = new TreeNode(9);

const node7 = new TreeNode(10);
const node8 = new TreeNode(12);


root.left = node2;

node2.left = node3;
node2.right = node4;

node3.left = node5;
node4.right = node6;

node5.left = node7;
node6.right = node8;


// Space Complexity: O(n)
// Time Complexity: O(n)
const diameterOfBinaryTree = (root) => {
  let answer = 0;

  const helper = (root) => {
    if(!root) {
      return -1;
    };

    const left = 1 + helper(root.left);
    const right = 1 + helper(root.right);

    answer = Math.max(left + right, answer);

    return Math.max(left, right);
  };

  helper(root);

  return answer;
};


// add left and right node with diameter to the map
// use postOrder traversal
// update the answer and update the currentNode diameter using children diameter
// Time Limit exceeded
// Space Complexity: O(n)
// Time Complexity: O(n)
const diameterOfBinaryTreeII = (root) => {
  if(!root) {
    return null;
  };

  const stack = [];
  const map = new Map();
  let diameter = 0;

  stack.push(root);

  while(stack.length) {
    const node = stack[stack.length - 1];

    if(node.left && !map.has(node.left)) {
      stack.push(node.left);
    } else if(node.right && !map.has(node.right)) {
      stack.push(node.right);
    } else {
      stack.pop();
      const leftDiameter = map.get(node.left) || 0;
      const rightDiameter = map.get(node.right) || 0;

      map.set(node, 1 + Math.max(leftDiameter, rightDiameter));

      diameter = Math.max(diameter, leftDiameter + rightDiameter);
    };

  };

  return diameter;
};

console.log(diameterOfBinaryTreeII(root));

