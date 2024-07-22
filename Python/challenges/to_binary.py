def decimal_to_binary(decimal):
    binary = []
    while(decimal > 0):
        binary.append(decimal % 2)
        decimal = decimal // 2
    binary.reverse()
    return ''.join(str(char) for char in binary)

def binary_to_decimal(binary):
    return int(binary, 2)



def main():
    input_number = input("Enter a number to convert: ")
    print(decimal_to_binary(int(input_number)))
    #print(binary_to_decimal(input_number))


if __name__ == '__main__':
    main()
