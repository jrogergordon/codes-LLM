public class Main {
    public static void main(String[] args) {
        System.out.println(areAllCharactersUnique("abcde"));  // true
        System.out.println(areAllCharactersUnique("abcdea")); // false
    }

    public static boolean areAllCharactersUnique(String str) {
        int[] charCount = new int[26]; // assuming only lowercase letters
        for (int i = 0; i < str.length(); i++) {
            int index = str.charAt(i) - 'a';
            if (charCount[index] > 0) {
                return false; // duplicate character found
            }
            charCount[index]++;
        }
        return true; // no duplicate characters found
    }
}