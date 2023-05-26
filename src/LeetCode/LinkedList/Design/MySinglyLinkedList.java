package LeetCode.LinkedList.Design;

class MyNode {
    public int value;
    public MyNode next;
}

public class MySinglyLinkedList {
    public MyNode head;
    public int size;

    public MySinglyLinkedList() {
        head = new MyNode();
        head.value = 0;
        size = 0;
    }

    public int get(int index) {
        if (head == null || index >= size) {
            return -1;
        }

        MyNode tempNode = head;

        for (int i = 0; i < index + 1; i++) {
            tempNode = tempNode.next;
        }

        return tempNode.value;
    }

    public void addAtHead(int val) {
        addAtIndex(0, val);

    }

    public void addAtTail(int val) {
        addAtIndex(size, val);
    }

    public void addAtIndex(int index, int val) {
        if (index > size) {
            return;
        }

        if (index < 0) {
            index = 0;
        }

        MyNode pred = head;

        size++;

        for (int i = 0; i < index; i++) {
            pred = pred.next;
        }

        MyNode newNode = new MyNode();
        newNode.value = val;
        newNode.next = pred.next;

        pred.next = newNode;
    }

    public void deleteAtIndex(int index) {
        // if the index is invalid return
        if (index < 0 || index >= size) {
            System.out.println("Index not found!");
            return;
        }

        size--;

        MyNode tempNode = head;

        for (int i = 0; i < index; i++) {
            tempNode = tempNode.next;
        }

        tempNode.next = tempNode.next.next;
    }

    public void traversal() {
        if (size == 0) {
            return;
        }

        System.out.println("TRAVERSING.. ");

        MyNode node = head;

        for (int i = 0; i <= size; i++) {
            System.out.print(node.value);
            node = node.next;

            if (i != size) {
                System.out.print(" -> ");
            }

        }

        System.out.println();

    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */