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

    def generate_combinations(index, current_combination):
        if index == len(digits):
            return [current_combination]
        else:
            combinations = []
            for letter in digit_map[digits[index]]:
                if index < len(digits) - 1 and digits[index] == digits[index + 1]:
                    combinations.extend(generate_combinations(index + 2, current_combination + letter))
                else:
                    combinations.extend(generate_combinations(index + 1, current_combination + letter))
            return combinations

    return generate_combinations(0, '')
ans = (3000)
print(ans)