#!/usr/bin/python3
def validUTF8(data):
    # Helper function to check if a given byte is a valid UTF-8 continuation byte
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    # Iterate through each byte in the data
    i = 0
    while i < len(data):
        # Check the number of bytes for the current character
        if (data[i] & 0b10000000) == 0:  # 1-byte character
            i += 1
        elif (data[i] & 0b11100000) == 0b11000000:  # 2-byte character
            if i + 1 >= len(data) or not is_continuation(data[i + 1]):
                return False
            i += 2
        elif (data[i] & 0b11110000) == 0b11100000:  # 3-byte character
            if i + 2 >= len(data) or not is_continuation(data[i + 1]) or not is_continuation(data[i + 2]):
                return False
            i += 3
        elif (data[i] & 0b11111000) == 0b11110000:  # 4-byte character
            if i + 3 >= len(data) or not is_continuation(data[i + 1]) or not is_continuation(data[i + 2]) or not is_continuation(data[i + 3]):
                return False
            i += 4
        else:
            # Invalid starting byte
            return False

    return True

# Example usage:
data = [197, 130, 1]  # Represents the UTF-8 encoding of the character 'é'
result = validUTF8(data)
print(result)