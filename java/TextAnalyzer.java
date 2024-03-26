import java.util.*;
import java.lang.*;
import java.io.*;

class TextAnalyzer {
    
    public static Map<String, Integer> analyzeText(String text) {
        if (text == null || text.trim().isEmpty()) {
            throw new IllegalArgumentException("Text cannot be null or empty.");
        }

        Map<String, Integer> wordFrequencyMap = new HashMap<>();
        String[] words = text.split("\\s+");

        for (String word : words) {
            wordFrequencyMap.put(word, wordFrequencyMap.getOrDefault(word, 0) + 1);
        }

        return wordFrequencyMap;
    }

    public static int getWordCount(String text) {
        String[] words = text.split("\\s+");
        return words.length;
    }

    public static int getCharacterCount(String text) {
        return text.length();
    }

    public static int getLineCount(String text) {
        String[] lines = text.split("\n");
        return lines.length;
    }

    public static int getUniqueWordCount(Map<String, Integer> wordFrequencyMap) {
        return wordFrequencyMap.size();
    }

    public static Map<String, Integer> getWordFrequency(Map<String, Integer> wordFrequencyMap) {
        return wordFrequencyMap;
    }

    public static String getMostFrequentWord(Map<String, Integer> wordFrequencyMap) {
        String mostFrequentWord = null;
        int maxFrequency = 0;

        for (Map.Entry<String, Integer> entry : wordFrequencyMap.entrySet()) {
            if (entry.getValue() > maxFrequency) {
                mostFrequentWord = entry.getKey();
                maxFrequency = entry.getValue();
            }
        }

        return mostFrequentWord;
    }
}
