import java.util.Arrays;

public class BubbleSortSquare {

    public static void main(String[] args) {
        int[] response = bubbleSort(new int[]{5,3,1});

        for(int i = 0; i < response.length; i++) {
            response[i] *= response[i];
        };

        System.out.println(Arrays.toString(response));
    }

    static int[] bubbleSort(int[] arr) {
        boolean swapped = true;

        while(swapped) {
            swapped = false;

            for(int i = 0; i < arr.length - 1; i++) {
                if(arr[i] > arr[i + 1]) {
                    swap(i, i+1, arr);

                    swapped = true;
                }
            }
        }

        return arr;
    }

    static void swap(int num1, int num2, int[] arr) {
        int tmp = arr[num1];

        arr[num1] = arr[num2];
        arr[num2] = tmp;
    };


}
