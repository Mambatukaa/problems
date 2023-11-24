class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insertII(value, root = this) {
    if(!this.value) {
      this.value = value;
      return;
    }

    if(root === null) {
      return new BST(value);
    }

    if(root.value > value) {
      // go left
       root.left = this.insert(value, root.left);
       return root;
    } else {
      // go right
      root.right = this.insert(value, root.right);
      return root;
    }
  }

  insert(value) {
    if(this.value > value) {
      // go left
      
      if(!this.left) {
        this.left = new BST(value);
      } else {
        this.left.insert(value);
      }

    } else {
      // go right
      if(!this.right) {
        this.right = new BST(value);
      } else {
        this.right.insert(value);
      }
    }

    return this;
  }

  containsII(value, root = this) {
    if(root === null) {
      return false;
    }

    if(root.value === value) {
      return true;
    }

    if(root.value > value) {
      // go left
      return this.contains(value, root.left);
    } else {
      return this.contains(value, root.left);
    }
    
  }

  contains(value) {
    if(this.value > value) {
      if(!this.left) {
        return false; 
      }

      // go left
      return this.left.contains(value);

    } else if(this.value < value) {
      if(!this.right) {
        return false; 
      }

      // go right
      return this.right.contains(value);
    } else {
      return true;
    }

  }


  remove(value, parentNode = null) {
    if(!this) {
      return;
    }

    if(this.value < value) {
      // go right
      if(this.right !== null) {
        this.right.remove(value, this);
      } 
    } else if(this.value > value) {
      // go left

      if(this.left !== null) {
        this.left.remove(value, this);
      } 

    } else {
      // found value
      if(this.left !== null && this.right !== null) {
        const rightMin = this.findMinElement(this.right);
        this.value = rightMin.value;

        return this.right.remove(this.value, this);
      } else if(parentNode === null) {
        if(this.left !== null) {
          this.value = this.left.value;

          this.right = this.left.right;
          this.left = this.left.left;
        } else if(this.right !== null) {
          this.value = this.right.value;

          this.left = this.right.left;
          this.right = this.right.right
        } else {

        }

      } else if(parentNode.left === this) {
        parentNode.left = this.left ? this.left : this.right;
      } else if(parentNode.right === this) {
        parentNode.right = this.left ? this.left : this.right; 
      }
    }

    return this;

  };

  findMinElement() {
    if(this.left === null) {
      return this;
    }

    return this.left.findMinElement();
  };


  printLevelOrder() {
        var h = this.height(this);
        var i;
        for (i = 1; i <= h; i++)
            this.printCurrentLevel(this, i);
    }
 
    // Compute the "height" of a tree -- the number 
    // of nodes along the longest path
    // from the root node down to the farthest leaf node.
    height(root) {
        if (root == null)
            return 0;
        else {
            // Compute height of each subtree
            var lheight = this.height(root.left);
            var rheight = this.height(root.right);
 
            // Use the larger one
            if (lheight > rheight)
                return (lheight + 1);
            else
                return (rheight + 1);
        }
    }
 
    // Print nodes at the current level
      printCurrentLevel(root , level) {
        if (root == null)
            return;
        if (level == 1)
            console.log(root.value + " ");
        else if (level > 1) {
            this.printCurrentLevel(root.left, level - 1);
            this.printCurrentLevel(root.right, level - 1);
        }
    }

}


const bst = new BST(5);

bst.insert(2)
bst.insert(8)

bst.insert(1)
bst.insert(3)

bst.insert(6)
bst.insert(9)

bst.printLevelOrder();

bst.remove(1);
console.log('-------------');
bst.printLevelOrder();
