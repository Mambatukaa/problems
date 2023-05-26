package LeetCode.LinkedList;

import org.w3c.dom.ls.LSOutput;

public class MyDoublyLinkedList {
    public int size;
    public MyDoublyNode head, tail;

    public MyDoublyLinkedList() {
        size = 0;

        head = new MyDoublyNode(0);
        tail = new MyDoublyNode(0);
        head.next = tail;
        tail.prev = head;
    }

    public int get(int index) {
        // if the index is not invalid return -1
        if (index < 0 || index > size || size == 0) {
            return -1;
        }

        MyDoublyNode pred = head;

        for (int i = 0; i <= index; i++) {
            pred = pred.next;
        }

        return pred.value;
    }


    public void addAtIndex(int index, int value) {
        if (index > size) {
            return;
        }

        // if the index less than 0 set the index to 0
        if (index < 0) {
            index = 0;
        }

        size++;

        MyDoublyNode pred = head;

        for (int i = 0; i < index; i++) {
            pred = pred.next;
        }

        MyDoublyNode newNode = new MyDoublyNode(value);

        newNode.prev = pred;
        newNode.next = pred.next;
        pred.next.prev = newNode;
        pred.next = newNode;
    }


    public void delete(int index) {
        MyDoublyNode pred = head;
        size--;

        for (int i = 0; i < index; i++) {
            pred = pred.next;
        }

        // successor
        MyDoublyNode succ = pred.next.next;

        pred.next = succ;
        succ.prev = pred;
    }

    public void addAtHead(int value) {
        MyDoublyNode pred = head, succ = head.next;

        size++;

        MyDoublyNode toAdd = new MyDoublyNode(value);

        toAdd.prev = pred;
        toAdd.next = succ;
        pred.next = toAdd;
        succ.prev = toAdd;
    }

    public void addAtTail(int value) {
        MyDoublyNode succ = tail, pred = tail.prev;

        size++;

        MyDoublyNode toAdd = new MyDoublyNode(value);

        toAdd.prev = pred;
        toAdd.next = succ;
        pred.next = toAdd;
        succ.prev = toAdd;
    }

    public void traversal() {
        MyDoublyNode pred = head;

        for (int i = 0; i <= size; i++) {
            System.out.print(pred.value);
            pred = pred.next;

            if (i != size) {
                System.out.print(" -> ");
            }


        }
    }
}

/*
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
