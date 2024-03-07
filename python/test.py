def lengthOfLongestSubstringTwoSame(s):
    n = len(s)
    ans = 0
    left = 0
    count = [0] * 26
    same = 0

    for right in range(n):
        count[s[right] - 'a'] += 1
        if count[s[right] - 'a'] == 3:
            same += 1

        while same > 0:
            count[s[left] - 'a'] -= 1
            if count[s[left] - 'a'] == 2:
                same -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans

print(lengthOfLongestSubstringTwoSame("aabbczlkdtrrrrrrrrrddddddddd"))