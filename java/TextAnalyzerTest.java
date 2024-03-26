import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Map;
import java.util.HashMap;

class TextAnalyzerTest {

    @Test
    void analyzeText_normalInput() {
        String text = "This is a test string.";
        Map<String, Integer> expected = new HashMap<>();
        expected.put("This", 1);
        expected.put("is", 1);
        expected.put("a", 1);
        expected.put("test", 1);
        expected.put("string", 1);

        Map<String, Integer> actual = TextAnalyzer.analyzeText(text);
        assertEquals(expected, actual);
    }

    @Test
    void analyzeText_emptyString() {
        assertThrows(IllegalArgumentException.class, () -> TextAnalyzer.analyzeText(""));
    }

    @Test
    void analyzeText_nullInput() {
        assertThrows(IllegalArgumentException.class, () -> TextAnalyzer.analyzeText(null));
    }

    @Test
    void analyzeText_withRepeatingWords() {
        String text = "This is a test test string string string.";
        Map<String, Integer> expected = new HashMap<>();
        expected.put("This", 1);
        expected.put("is", 1);
        expected.put("a", 1);
        expected.put("test", 2);
        expected.put("string", 3);

        Map<String, Integer> actual = TextAnalyzer.analyzeText(text);
        assertEquals(expected, actual);
    }

    @Test
    void getWordCount_normalInput() {
        String text = "This is a test string.";
        int expected = 5;
        int actual = TextAnalyzer.getWordCount(text);
        assertEquals(expected, actual);
    }

    @Test
    void getWordCount_emptyString() {
        String text = "";
        int expected = 0;
        int actual = TextAnalyzer.getWordCount(text);
        assertEquals(expected, actual);
    }

    @Test
    void getCharacterCount_normalInput() {
        String text = "This is a test string.";
        int expected = 21;
        int actual = TextAnalyzer.getCharacterCount(text);
        assertEquals(expected, actual);
    }

    @Test
    void getCharacterCount_emptyString() {
        String text = "";
        int expected = 0;
        int actual = TextAnalyzer.getCharacterCount(text);
        assertEquals(expected, actual);
    }

    @Test
    void getLineCount_normalInput() {
        String text = "This is a test string.\nThis is another line.";
        int expected = 2;
        int actual = TextAnalyzer.getLineCount(text);
        assertEquals(expected, actual);
    }

    @Test
    void getLineCount_emptyString() {
        String text = "";
        int expected = 1;
        int actual = TextAnalyzer.getLineCount(text);
        assertEquals(expected, actual);
    }

    @Test
    void getUniqueWordCount_normalInput() {
        Map<String, Integer> wordFrequencyMap = new HashMap<>();
        wordFrequencyMap.put("This", 1);
        wordFrequencyMap.put("is", 1);
        wordFrequencyMap.put("a", 1);
        wordFrequencyMap.put("test", 2);
        wordFrequencyMap.put("string", 3);

        int expected = 5;
        int actual = TextAnalyzer.getUniqueWordCount(wordFrequencyMap);
        assertEquals(expected, actual);
    }

    @Test
    void getWordFrequency_normalInput() {
        Map<String, Integer> wordFrequencyMap = new HashMap<>();
        wordFrequencyMap.put("This", 1);
        wordFrequencyMap.put("is", 1);
        wordFrequencyMap.put("a", 1);
        wordFrequencyMap.put("test", 2);
        wordFrequencyMap.put("string", 3);

        Map<String, Integer> expected = wordFrequencyMap;
        Map<String, Integer> actual = TextAnalyzer.getWordFrequency(wordFrequencyMap);
        assertEquals(expected, actual);
    }

    @Test
    void getMostFrequentWord_normalInput() {
        Map<String, Integer> wordFrequencyMap = new HashMap<>();
    }
}