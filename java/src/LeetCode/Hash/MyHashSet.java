import java.util.ArrayList;
import java.util.LinkedList;


public class MyHashSet {
  LinkedList<Integer>[] hashTable;
  private int keyRange;

  public MyHashSet() {
    this.keyRange = 10;
    this.hashTable = new LinkedList[10];
  }

  public void add(int key) {
    int index = _hash(key);


    if(this.hashTable[index] == null) {
      hashTable[index] = new LinkedList<Integer>();

      hashTable[index].add(key);
    } else {
      hashTable[index].add(key);
    }

  }

  public void displayHashTable() {
    if(hashTable == null) {
      System.out.println("HashTable doesn't not exist!");

      return;
    } else {

      for(int i = 0; i < hashTable.length; i++) {
        System.out.println(hashTable[i]);
      }

    }
  }

  public void remove(int key) {
    int index = _hash(key);

    if(this.contains(key)) {
      hashTable[index].remove(key);
    }

  }

  public boolean contains(int key) {
    int index = _hash(key);
    
    if(hashTable[index] != null && hashTable[index].contains(key)) {
      return true;
    }

    return false;
  }


  protected int _hash(int key) {
    return (key % keyRange);
  }


  public static void main(String[] args) {

    System.out.println("Hello World");


    MyHashSet hash = new MyHashSet();

    hash.add(1);
    hash.add(2);
    hash.add(3);
    hash.add(11);

    hash.displayHashTable();


    System.out.println("---------------------------------------------------------------------------");

    hash.remove(11);

    hash.displayHashTable();

  }

}
