import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;


/* Name of the class has to be "Main" only if the class is public. */
public class Main
{
        public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read input text
        System.out.println("Enter the text to analyze:");
        String inputText = scanner.nextLine();

        try {
            // Analyze the text
            Map<String, Integer> wordFrequencyMap = TextAnalyzer.analyzeText(inputText);

            // Display the results
            System.out.println("\nAnalysis Results:");
            System.out.println("Word count: " + TextAnalyzer.getWordCount(inputText));
            System.out.println("Character count: " + TextAnalyzer.getCharacterCount(inputText));
            System.out.println("Line count: " + TextAnalyzer.getLineCount(inputText));
            System.out.println("Unique word count: " + TextAnalyzer.getUniqueWordCount(wordFrequencyMap));
            System.out.println("Word frequency: " + TextAnalyzer.getWordFrequency(wordFrequencyMap));
            System.out.println("Most frequent word: " + TextAnalyzer.getMostFrequentWord(wordFrequencyMap));
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
}

