def longest_substring_without_repeats(s):
    """
    Find the length of the longest substring in the given string
    without repeating characters.
    """
    # Use a sliding window to keep track of the longest substring
    window = {}
    max_len = 0
    for i in range(len(s)):
        # If the current character is already in the window, shrink the window
        if s[i] in window:
            window = {s[i]: i}
        # Otherwise, expand the window
        else:
            window[s[i]] = i
            max_len = max(max_len, len(window))
    return max_len

ans = longest_substring_without_repeats("abcdeapl")
print(ans)