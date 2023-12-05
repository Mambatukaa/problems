// Time Complexity: O(n)
// Space Complexity: O(n)
const minDepth = (root) => {
  let min = Infinity;
  let depth = 1;

  function minDepthBT(root, depth) {
    if(!root) {
      return depth;
    }

    if(!root.left && !root.right) {
      return depth;
    }

    const leftDepth = minDepthBT(root.left, depth + 1);
    const rightDepth = minDepthBT(root.right, depth + 1);
  }


  minDepthBT(root, depth);

  return min === Infinity ? 0 : min;
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const minDepthIterative = (root) => {
  if(!root) {
    return 0;
  }

  const stack = [[root, 1]];
  let min = Infinity;

  while(stack.length) {
    const [current, depth] = stack.pop();

    if(!current.left && !current.right) {
      if(depth < min) {
        min = depth;
      };

      continue;
    }

    if(current.left) {
      stack.push([current.left, depth + 1]);
    };

    if(current.right) {
      stack.push([current.right, depth + 1]);
    };

  };

  return min;
}

// Time Complexity: O(n)
// Space Complexity: O(n)
// DFS
const minDepthII = (root) => {
  if(!root) {
    return 0;
  };

  if(!root.left) {
    return 1 + minDepthII(root.right);
  } else if(!root.right) {
    return 1 + minDepthII(root.left);
  }

  return 1 + Math.min(minDepthII(root.left), minDepthII(root.right));
};

// Time Complexity: O(n)
// Space Complexity: O(n)
// BFS
const minDepthIteration = (root) => {
  // base case
  if(!root) {
    return 0;
  }

  const queue = [];

  let depth = 1;
  queue.push(root);

  while(queue.length) {
    let size = queue.length;

    while(size > 0) {
      size--;

      const current = queue.shift();

      if(!current.left && !current.right) {
        return depth;
      }

      if(current.left) {
        queue.push(current.left);
      }

      if(current.right) {
        queue.push(current.right);
      }

    }

    depth++;
  }
}

class BT {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const root = new BT(3);

const node1 = new BT(9);
const node2 = new BT(20);

const node3 = new BT(15);
const node4 = new BT(7);

root.left = node1;
root.right = node2;

node2.left = node3;
node2.right = node4;

console.log(minDepthIteration(null), 'hhahha');
