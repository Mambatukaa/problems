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
 * @param {number} val
 * @return {TreeNode}
 */
// Time Complexity: O(n)
// Space Complexity: O(n)
var insertIntoBSTII = function(root, val) {
  const newNode = new TreeNode(val);

  if(!root) {
    return newNode;
  };


  if(root.val < val) {
    // go right

    if(!root.right) {
      root.right = newNode;
      return root;
    }

    insertIntoBST(root.right, val);

  } else {
    if(!root.left) {
      root.left = newNode;
      return root;
    }

    insertIntoBST(root.left, val);
  }

  return root;
};

// Time Complexity: O(n)
// Space Complexity: O(n)
const insertIntoBST = (root, val) => {
  const nodeToInsert = new TreeNode(val);

  if(!root) {
    return nodeToInsert;
  }

  const stack = [root];

  while(stack.length) {
    let curr = stack.pop();

    if(curr.val > val) {
      // go left
      if(!curr.left) {
        curr.left = nodeToInsert;
        break;
      };

      stack.push(curr.left);

    } else {
      // go right
      if(!curr.right) {
        curr.right = nodeToInsert;
        break;
      }

      stack.push(curr.right);
    };

  };
  return root;
};


// Clean code
// Time Complexity: O(n)
// Space Complexity: O(n)
var insertIntoBSTIII = function(root, val) {
  if(!root) {
    return new TreeNode(val);
  };


  if(root.val < val) {
    // go right
    root.right = insertIntoBST(root.right, val);
  } else {
    root.left = insertIntoBST(root.left, val);
  }

  return root;
};

/*


          4
        /   \
      2       7
    /  \     /
  1     3   5


*/
