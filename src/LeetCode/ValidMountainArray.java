package LeetCode;

public class ValidMountainArray {
    final int[] arr;

    public ValidMountainArray(int[] arr) {
        this.arr = arr;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public boolean solution() {
        int i = 0;
        int n = arr.length;

        // check are elements increasing
        while (i < n - 1 && arr[i] < arr[i + 1]) {
            i++;
        }

        // check are elements decreased || are elements will decrease
        if (i == 0 || i == n - 1) {
            return false;
        }

        // check are elements decreasing
        while (i < n - 1 && arr[i] > arr[i + 1]) {
            i++;
        }

        return i == n - 1;
    }

}
