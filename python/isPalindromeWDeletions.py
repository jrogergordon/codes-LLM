import re
def is_palindrome(s):
    s = s.lower()  # convert to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', s)  # remove non-alphanumeric characters
    rev_s = s[::-1]  # get the reversed string
    mismatch = False
    for i, c in enumerate(s):
        if c != rev_s[i]:  # check for mismatch
            if mismatch:  # if already found one mismatch, return False
                return False
            rev_s = rev_s[:i] + rev_s[i+1:]  # delete one character from the reversed string
            mismatch = True
    return s == rev_s  # if no mismatch or only one mismatch, return True

ans = is_palindrome("ab")
print(ans)