def can_form_palindrome(s, k):
    if len(s) < k:
        return True

    l = 0
    r = len(s) - 1
    delete_count = 0

    while l < r:
        if s[l] != s[r]:
            delete_count += 1
            if delete_count > k:
                return False
        l += 1
        r -= 1

    return True
ans = can_form_palindrome("leseli", 1)
print(ans)