import LeetCode.LinkedList.Design.DoublyLinkedList;
import LeetCode.LinkedList.Design.MyDoublyLinkedList;
import LeetCode.QueueAndStack.MyCircularQueue;

import java.util.Arrays;

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


//        MyDoublyLinkedList mDLL = new MyDoublyLinkedList();
//
//        mDLL.addAtHead(1);
//        mDLL.addAtIndex(1, 2);
//        mDLL.addAtTail(3);
//
//        mDLL.delete(2);
//
//        System.out.println("size: " + mDLL.size);
//
//        mDLL.traversal();
//


//        DoublyLinkedList myDLL = new DoublyLinkedList();
//
//        System.out.println(myDLL.size);
//
//        myDLL.addAtIndex(0, 1);
//        myDLL.addAtIndex(1, 2);
//
//        System.out.println(myDLL.size);
//
//        myDLL.traversal();

        MyCircularQueue myCircularQueue = new MyCircularQueue(4);
        System.out.println("is empty: " + myCircularQueue.isEmpty());

        myCircularQueue.enQueue(1);

        System.out.println("is empty: " + myCircularQueue.isEmpty());

        myCircularQueue.enQueue(2);
        myCircularQueue.enQueue(3);
        myCircularQueue.enQueue(4);

        System.out.println("head index: " + myCircularQueue.headIndex);
        System.out.println("tail index: " + myCircularQueue.tailIndex);

        System.out.println(Arrays.toString(myCircularQueue.data));
        System.out.println("is full: " + myCircularQueue.isFull());

        myCircularQueue.deQueue();
        myCircularQueue.deQueue();

        myCircularQueue.deQueue();

        System.out.println("head index: " + myCircularQueue.headIndex);
        System.out.println("tail index: " + myCircularQueue.tailIndex);


    }

}

