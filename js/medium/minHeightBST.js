const minHeight = (array) => {

}



class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }


  insert(value) {
    if(value < this.value) {
      if(this.left === null) {
        this.left = new BST(value);
      } else {
        this.left.insert(value);
      }

    } else {
      if(this.right === null) {
        this.right = new BST(value);
      } else {
        this.right.insert(value);
      }
    }

  }
}


const bst = new BST(8);

bst.insert(7);
bst.insert(9);

console.log(bst)
