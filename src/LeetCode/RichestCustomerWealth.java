package LeetCode;

public class RichestCustomerWealth {
    final private int[][] accounts;

    public RichestCustomerWealth(int[][] accounts) {
        this.accounts = accounts;
    }


    // Space complexity: O(1)
    // Time complexity: O(n x m)
    public int naive() {
        int max = 0;
        int count = 0;

        for (int[] customer : accounts) {
            for (int a : customer) {
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
