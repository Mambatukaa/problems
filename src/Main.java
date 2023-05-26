import LeetCode.LinkedList.Design.MyDoublyLinkedList;

class Main {
    public static void main(String[] args) {
//        BinarySearchTree newBST = new BinarySearchTree();
//
//        newBST.insert(5);
//        newBST.insert(2);
//        newBST.insert(1);
//        newBST.insert(3);
//        newBST.insert(4);
//
//
//        newBST.insert(8);
//        newBST.insert(7);
//        newBST.insert(6);
//        newBST.insert(9);
//        newBST.insert(10);
//
//        newBST.preOrder(newBST.root);
//        System.out.println();
//        newBST.inOrder(newBST.root);
//
//        System.out.println();
//        newBST.post(newBST.root);
//
//        System.out.println();
//        newBST.levelOrder();
//        System.out.println();
//
//        System.out.println(newBST.search(1));
//
//        System.out.println("recursive: " + newBST.searchRecursive(newBST.root, 12));


        MyDoublyLinkedList mDLL = new MyDoublyLinkedList();

        mDLL.addAtHead(1);
        mDLL.addAtIndex(1, 2);
        mDLL.addAtTail(3);

        mDLL.delete(2);

        System.out.println("size: " + mDLL.size);

        mDLL.traversal();

    }

}

