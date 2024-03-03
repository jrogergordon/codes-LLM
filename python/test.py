def letter_combinations(digits):
    if not digits:
        return []

    digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = ''
    i = 0
    while i < len(digits):
        count = 0
        while i + count < len(digits) and digits[i + count] == digits[i]:
            count += 1
        result += digit_map[digits[i]][count-1]
        i += count

    return [result]
ans = letter_combinations("3444")
print(ans)