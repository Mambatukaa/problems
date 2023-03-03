public class ThirdLargestNum {
    public static void main(String[] args) {
        int res = response(new int[]{4, 2, 3, 5});

        System.out.println(res);
    }

    static int response(int[] array) {
        // return the second-largest number in the array
        int max1 = Integer.MIN_VALUE;
        int max2 = Integer.MIN_VALUE;
        int max3 = Integer.MIN_VALUE;

        for (int i : array) {
            if (max1 < i) {
                max3 = max2;
                max2 = max1;
                max1 = i;
            } else if (max2 < i) {
                max3 = max2;
                max2 = i;
            } else if (max3 < i) {
                max3 = i;
            }
        }

        return max2;
    }
}
