import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[][] accounts = {{1, 2, 3}, {1, 2, 5}};

        RichestCustomerWealth richestCustomerWealth = new RichestCustomerWealth(accounts);


        System.out.println(richestCustomerWealth.naive());
    }

}
