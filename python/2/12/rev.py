def reverse_array(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

arr = ["a", "b", "c", "d"]
reverse_array(arr)
print(arr)
str = "abcd"
reverse_array(str)
print(str)