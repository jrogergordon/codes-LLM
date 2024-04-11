thisset = {"apple", "banana", "cherry", "apple", "apple", "apple", "banana"}

fruit_counts = {}
for fruit in thisset:
    if fruit not in fruit_counts:
        fruit_counts[fruit] = 1
    else:
        fruit_counts[fruit] += 1

print(sorted(fruit_counts.items(), key=lambda x: x[1], reverse=True))