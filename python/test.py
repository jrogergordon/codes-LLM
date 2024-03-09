def check_characters(needle, haystack):
    # Create a dictionary to store the count of each character in haystack
    char_count = {}
    for char in haystack:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Check each character in needle
    for char in needle:
        if char in char_count and char_count[char] > 0:
            char_count[char] -= 1
        else:
            return -1
    
    return True

print(check_characters("aaaaaaaaa", "aaaaaaaa"))  