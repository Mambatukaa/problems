import java.util.Arrays;

public class Test5 {
    static int[] compare(int[] first, int[] second) {
        if(first == null || second == null) return null;
        if(first.length == 0 || second.length == 0) return new int[0];

        int minIndex = (first.length > second.length) ? second.length : first.length;
        int[] a,b;

        if(minIndex == first.length) {
            a = first;
            b = second;
        } else {
            a = second;
            b = first;
        }

        int index = 0;
        int[] copyArr = new int[minIndex];

        for (int i : a) {
            for (int j : b) {
                if (i == j) {
                    copyArr [index] = j;
                    index++;
                }
            }
        }

        int[] response = new int[index];

        for(int i = 0; i < response.length; i++) {
            response[i] = copyArr[i];
            System.out.println(copyArr[i]);
        }

        return response;
    }


    public static void main(String[] args) {
        int[] response = compare(new int[]{1,8,3,2}, new int[]{4,2,1});

        System.out.println(Arrays.toString(response));
    }
}
