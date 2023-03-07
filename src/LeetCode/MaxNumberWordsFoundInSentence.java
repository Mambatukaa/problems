package LeetCode;

// 2114

public class MaxNumberWordsFoundInSentence {
    final private String[] sentences;

    public MaxNumberWordsFoundInSentence(String[] sentences) {
        this.sentences = sentences;
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
    public int naive() {
        int max = 0;

        for (String sentence : sentences) {
            String[] wordsInSentence = sentence.split(" ");

            if (wordsInSentence.length > max) {
                max = wordsInSentence.length;
            }
        }

        return max;
    }


}
