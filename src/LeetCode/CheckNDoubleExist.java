package LeetCode;

import java.util.Hashtable;

public class CheckNDoubleExist {
    final private int[] arr;

    public CheckNDoubleExist(int[] arr) {
        this.arr = arr;
    }

    // Time complexity: O(n^2)
    // Space complexity: O(n)

    public boolean naive() {
        Hashtable<Integer, Integer> map = new Hashtable<>();

        for (int i = 0; i < arr.length; i++) {
            map.put(arr[i], i);
        }

        System.out.println(map);

        for (int i = 0; i < arr.length; i++) {
            if (map.containsKey(arr[i] * 2) && map.get(2 * arr[i]) != i) {
                return true;
            }
        }

        return false;
    }

    // Time complexity: O(n^2)
    // Space complexity: O(1)
    public boolean bruteForceSolution() {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (i != j && arr[j] * 2 == arr[i]) {
                    return true;
                }
            }
        }

        return false;
    }

}
