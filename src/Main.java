import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        String[] sentences = {"A", "A B", "A B C"};

        MaxNumberWordsFoundInSentence maxNumberWordsFoundInSentence = new MaxNumberWordsFoundInSentence(sentences);

        System.out.println(maxNumberWordsFoundInSentence.naive());
    }

}
