import java.util.Arrays;

public class InsertionSort {
    void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;

            while(j >= 0 && arr[j] > key) {
                // swap
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        InsertionSort obj = new InsertionSort ();

        int[] arr = new int[]{3, 2, 1, -1, 5};

        obj.insertionSort(arr);

        System.out.println(Arrays.toString(arr));
    }
}
