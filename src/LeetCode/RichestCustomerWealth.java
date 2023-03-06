package LeetCode;

public class RichestCustomerWealth {
    final private int[][] accounts;

    public RichestCustomerWealth(int[][] accounts) {
        this.accounts = accounts;
    }


    public int naive() {
        int max = 0;
        int count = 0;

        for (int[] account : accounts) {
            for (int a : account) {
                count += a;
            }

            if (max < count) {
                max = count;
            }

            count = 0;
        }

        return max;
    }
}
