def reverse_bytes(x):
    byte_string = b''
    while x > 0:
        byte = x & 0xFF  # Extract the least significant byte
        byte_string += chr(byte).encode()  # Append the byte to the byte string
        x >>= 8  # Shift x to the right by 8 bits to get the next byte
    return byte_string

ans = reverse_bytes(0x12345678)
print(ans)