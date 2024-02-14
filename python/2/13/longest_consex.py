def longest_consecutive_sequence(arr):
    # Create a dictionary to keep track of the longest sequence for each number
    seq_dict = {}
    max_len = 0
    max_seq = []

    for num in arr:
        # If the number is not in the dictionary, it's the start of a new sequence
        if num not in seq_dict:
            seq_dict[num] = 1

        # Check if the number is part of a longer sequence
        for prev_num in seq_dict:
            if num == prev_num + 1:
                # Update the sequence length and sequence
                seq_dict[prev_num] += 1
                seq_dict[num] = seq_dict[prev_num]

                # Update the maximum sequence length and sequence
                if seq_dict[prev_num] > max_len:
                    max_len = seq_dict[prev_num]
                    max_seq = [prev_num] + seq_dict[prev_num]

    return max_len, max_seq

ans = longest_consecutive_sequence([9, 8, 7,100,4,5,6,300,3,1,2, 8, 1, 0, -1])
print(ans)