class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    const newNode = new BST(value);

    if(this.value === null) {
      this.value = newNode.value;

      return newNode;
    }

    let root = this;

    while(root) {
      if(root.value <= value) {
        // go right
        if(!root.right) {
          root.right = newNode;
          return;
        }

        root = root.right;
      } else {
        // go left
        if(!root.left) {
          root.left = newNode;
          return;
        }
        root = root.left;
      }

    }


    return newNode;
  }

  levelOrder() {
    const queue = [];

    queue.push(this);

    while(queue.length) {
      const curr = queue.shift();

      console.log(curr.value)

      if(curr.left) {
        queue.push(curr.left);
      }

      if(curr.right) {
        queue.push(curr.right);
      }
    }

    return false;

  }

  contains(value) {
    let curr = this;

    while(curr) {
      if(curr.value === value) {
        return true;
      }

      if(curr.value > value) {
        curr = curr.left;
      } else {
        curr = curr.right;
      }
    }

    return false;
  }


  findMinNode(root = this) {
    let curr = root;

    while(curr.left) {
      curr = curr.left;
    }

    return curr;
  }

  remove(value, parentNode = null) {
    let currentNode = this;

    while(currentNode) {
      // search value
      if(currentNode.value > value) {
        parentNode = currentNode;
        currentNode = currentNode.left;
      } else if(currentNode.value < value) {
        parentNode = currentNode;
        currentNode = currentNode.right;
      } else {
        // found value;
        if(currentNode.left !== null && currentNode.right !== null) {
          // replace currentNode to currentNode right tree's min element
          const rightMinNode = this.findMinNode(currentNode.right);

          currentNode.value = rightMinNode.value;
          currentNode.right.remove(currentNode.value, currentNode);
        } else if(parentNode === null) {
          // if there root node with no left or right child
          if(currentNode.left !== null) {
            currentNode.value = currentNode.left.value;
            currentNode.right = currentNode.left.right;
            currentNode.left = currentNode.left.left;
          } else if(currentNode.right !== null){
            currentNode.value = currentNode.right.value;
            currentNode.left = currentNode.right.left;
            currentNode.right = currentNode.right.right;
          } else {
            // this is a single node tree; do nothing
          }

        } else if(parentNode.left === currentNode) {
          parentNode.left = currentNode.left ? currentNode.left : currentNode.right;
        } else if(parentNode.right === currentNode) {
          parentNode.right = currentNode.left ? currentNode.left : currentNode.right;
        }

        break;
      }
    }

  }


}

const bst = new BST(5);

bst.insert(3);
bst.insert(8);
bst.insert(1);
bst.insert(4);
bst.insert(7);
bst.insert(10);
bst.insert(6);

console.log(bst.levelOrder());
bst.remove(5);
console.log('-------------');
console.log(bst.levelOrder())
