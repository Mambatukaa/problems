package LeetCode;

public class FinalValueOfVariableAfterPerformingOperations {
    final private String[] operations;


    public FinalValueOfVariableAfterPerformingOperations(String[] operations) {
        this.operations = operations;
    }

    // Time complexity: O(n)
    // Space complexity: O(1)
    public int naive() {
        int count = 0;

        for (String operation : operations) {
            if (operation.contains("-")) {
                count--;
            } else {
                count++;
            }

        }

        return count;
    }


    public int solutionFromDiscussion() {
        int x = 0;

        for (String o : operations) x += (44 - o.charAt(1));

        return x;
    }


}
