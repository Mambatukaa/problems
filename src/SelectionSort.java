import java.util.Arrays;

public class SelectionSort {

    public static void main(String[] args) {
        int[] response = selectionSort(new int[]{3, 0, -4, 1, 100});

        System.out.println(Arrays.toString(response));
    }

    static int[] selectionSort(int[] arr) {
        for(int i = 0; i < arr.length - 1; i++) {
            int minIndex = i;

            for(int j = i + 1; j < arr.length; j++) {
                if(arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            swap(i, minIndex, arr);
        }

        return arr;
    }

    static void swap(int num1, int num2, int[] arr) {
        int tmp = arr[num1];

        arr[num1] = arr[num2];
        arr[num2] = tmp;
    }


}
