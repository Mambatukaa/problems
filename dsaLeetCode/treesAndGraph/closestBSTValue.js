/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} target
 * @return {number}
 */
 // Time Complexity: O(h) h - height of tree
 // Space Complexity: O(h)
var closestValueII = function(root, target) {
  let answer = null;
  let minDiff = Infinity;

  const helper = (root) => {
    if(!root) return;

    const currDiff = Math.abs(target - root.val);

    if(currDiff < minDiff || currDiff === minDiff && root.val < answer) {
      answer = root.val;
      minDiff = currDiff;
    };

    if(root.val > target) {
      return helper(root.left)
    } else {
      return helper(root.right)
    }
  };

  helper(root);

  return answer;
};

// Time Complexity: O(h)
// Space Complexity: O(h)
var closestValueIII = function(root, target) {
  const child = root.val > target ? root.left : root.right;

  if(!child) return root.val;

  const closest = closestValue(child, target);

  const currentDiff = Math.abs(closest - target);
  const rootDiff = Math.abs(root.val - target);
  
  const isEqual = currentDiff === rootDiff;
  
  if (isEqual) {
    return closest > root.val ? root.val : closest;
  } 

  return currentDiff < rootDiff ? closest : root.val;
};


// Stack
// Time Complexity: O(h)
// Space Complexity: O(h)
const closestValueI = (root, target) => {
  const stack = [root];
  let answer = Infinity;

  while(stack.length) {
    const curr = stack.pop();

    const currDiff = Math.abs(curr.val - target);
    const minDiff = Math.abs(answer - target);

    if(currDiff < minDiff || currDiff === minDiff && curr.val < answer) {
      answer = curr.val;
    };

    if(curr.val > target) {
      // go left

      if(curr.left) {
        stack.push(curr.left);
      }

    } else {
      // go right
      if(curr.right) {
        stack.push(curr.right);
      }

    }

  };


  return answer;
};

// Time Complexity: O(h)
// Space Complexity: O(1)
const closestValue = (root, target) => {
  let closest = root.val;

  while(root) {
    const rootDiff = Math.abs(root.val - target);
    const currDiff = Math.abs(closest - target);

    if(currDiff > rootDiff || currDiff === rootDiff && root.val < closest) {
      closest = root.val;
    };

    if(root.val === target) break;

    root = root.val > target ? root.left : root.right;
  };

  return closest;
};

/*
        4
      /   \
    2       5
  /   \
1       3

target = 3.5;

root = 4;

diff = 0.5;
answer = 4;

compare target with every node and update answer using diff;
1. if (node.val > target) {
  //go left
  } else {
    //go right
  };
2. return answer

3. if currDiff === 0 return curr.node;

let minDiff = Infinity;
let answer = null;

helper = (root, target) => {
  if(!root) return;

  const currDiff = Math.abs(target - root.val);

  if(currDiff < minDiff) {
    answer = root;
    minDiff = currDiff;
  };

  if(root.val > target) {
    return helper(root.left, target)
  } else {
    return helper(root.right)
  }


};



*/
