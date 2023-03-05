import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        String[] operations = {"--X", "X++", "X++"};

        FinalValueOfVariableAfterPerformingOperations finalValueOfVariableAfterPerformingOperations = new FinalValueOfVariableAfterPerformingOperations(operations);

        System.out.println(finalValueOfVariableAfterPerformingOperations.naive());
    }

}
