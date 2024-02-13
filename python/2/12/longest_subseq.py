def longest_nearly_consecutive_subsequence(numbers):
    # Create a dictionary to keep track of the longest subsequence
    longest_subsequence = {}

    for num in numbers:
        # Check if the current number is part of a nearly consecutive subsequence
        if num - 2 in longest_subsequence:
            # Extend the current subsequence
            longest_subsequence[num] = longest_subsequence[num - 2] + [num]
        elif num - 1 in longest_subsequence:
            # Start a new subsequence
            longest_subsequence[num] = longest_subsequence[num - 1] + [num]
        else:
            # Start a new subsequence
            longest_subsequence[num] = [num]

    # Find the longest subsequence
    max_length = max(len(subseq) for subseq in longest_subsequence.values())
    longest_subsequence = [subseq for subseq in longest_subsequence.values() if len(subseq) == max_length]

    # Return the first longest subsequence
    return longest_subsequence[0]

numbers = [1, 3, 5, 11, 7, 13, 9]
print(longest_nearly_consecutive_subsequence(numbers))  # Output should be [5, 6, 7, 8]