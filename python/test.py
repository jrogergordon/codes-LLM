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
    for digit in digits:
        count = 0
        while digit == digits[count]:
            count += 1
        result += digit_map[digit][count-1]

    return [result]
ans = letter_combinations("33444")
print(ans)