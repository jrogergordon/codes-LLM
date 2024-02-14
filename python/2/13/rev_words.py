def reverse_words(s):
    new_s = ""
    for i, word in enumerate(s.split()):
        if word.isalpha():
            new_s += word[::-1] + " "
        else:
            word = word[::-1]
            new_s += word[1:] + word[0] + " "
    s = new_s.strip()
    return s


ans = "let. apples the,  fly"
ans = reverse_words(ans)
print(ans)