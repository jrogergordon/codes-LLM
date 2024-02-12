import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 5, 1, 2, 3, 8}; // Example input array
        
        // Invoke the countUniqueElements function
        int uniqueCount = countUniqueElements(nums);
        
        // Print the output to the console
        // for (int num : nums) {
        //     System.out.println(num);
        // }
        System.out.println("Number of unique elements: " + uniqueCount);
    }
    
    public static int countUniqueElements(int[] nums) {
    // Use a Set to keep track of unique elements
    Set<Integer> uniqueElements = new HashSet<>();

    // Iterate through the input array
    for (int i = 0; i < nums.length; i++) {
        int num = nums[i];
        // If the element is already in the set, replace it with 0
        if (!uniqueElements.add(num)) {
            nums[i] = 0;
        }
    }

    // Move all 0's to the back of the array
    int numZeroes = 0;
    for (int i = 0; i < nums.length; i++) {
        if (nums[i] == 0) {
            numZeroes++;
        }
    }

    // Shift non-0 elements to the front
    int j = 0;
    for (int num : nums) {
        // System.out.println(num);
        System.out.println(numZeroes);
        
    }
    for (int i = numZeroes; i < nums.length; i++) {
        if (nums[i] != 0) {
            nums[j] = nums[i];
            j++;
            // System.out.println("mid: " + i + ", " + j);
        }
    }
    System.out.println("break");
    // for (int num : nums) {
    //     System.out.println(num);
    // }

    // Fill the remaining slots with 0's
    for (int i = j; i < nums.length; i++) {
        nums[i] = 0;
    }

    // Return the size of the set (i.e. the number of unique elements)
    return uniqueElements.size();
    }
}