def convert_to_binary(n):
    if n == 0:
        return "0"
    
    binary_num = []
    while n > 0:
        binary_num.append(str(n % 2))
        n = n // 2

    # Reverse the list to get the correct binary representation
    binary_num.reverse()
    
    return ''.join(binary_num)

# Example usage:
number = 255

binary_representation = convert_to_binary(number)
print(f"The binary representation of {number} is {binary_representation}")